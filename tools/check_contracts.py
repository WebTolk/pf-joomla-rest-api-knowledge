"""Validate the pinned Manual snapshot, component schemas and executable examples.

No Joomla site, credentials or network requests are required. The test covers all
archived contracts too, but never rewrites their source or acceptance evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator
from openapi_spec_validator import validate as validate_openapi

from sync_manual import CONTRACTS, METHODS, SOURCE, VERSION, load, references, resolve


def operations(document):
    for path, item in document["paths"].items():
        for method, operation in item.items():
            if method in METHODS:
                yield method, path, operation


def validator(document, schema):
    return Draft202012Validator({"components": document["components"], **schema})


def check_document(document, label, counts):
    validate_openapi(document)
    counts["openapi_documents"] += 1
    ids = [operation["operationId"] for _, _, operation in operations(document)]
    assert len(ids) == len(set(ids)), f"Duplicate operation IDs: {label}"
    counts["operations"] += len(ids)
    for ref in references(document):
        assert ref.startswith("#/"), f"External reference in {label}: {ref}"
        # Resolve only the pointer here; recursive JSON Schema references are valid.
        target = document
        for part in ref[2:].split("/"):
            target = target[part.replace("~1", "/").replace("~0", "~")]
        counts["local_references"] += 1
    for name, schema in document["components"]["schemas"].items():
        Draft202012Validator.check_schema(schema)
        counts["schema_definitions"] += 1
    for _, path, operation in operations(document):
        contents = [("request", operation.get("requestBody", {}).get("content", {}))]
        contents += [(status, resolve(document, response).get("content", {}))
                     for status, response in operation["responses"].items()]
        for direction, content in contents:
            for media in content.values():
                check = validator(document, media["schema"])
                examples = [media["example"]] if "example" in media else []
                examples += [example["value"] for item in media.get("examples", {}).values()
                             if "value" in (example := resolve(document, item))]
                for example in examples:
                    errors = list(check.iter_errors(example))
                    assert not errors, f"{label} {path} {direction}: {errors[0].message if errors else ''}"
                    counts["embedded_examples"] += 1


def check_fixtures(document, fixtures, label, counts):
    by_id = {operation["operationId"]: operation for _, _, operation in operations(document)}
    for fixture in fixtures:
        operation = by_id[fixture["operationId"]]
        if fixture["direction"] == "request":
            content = operation["requestBody"]["content"]
        else:
            content = resolve(document, operation["responses"][str(fixture["status"])])["content"]
        media = content.get(fixture.get("media_type")) or next(iter(content.values()))
        errors = list(validator(document, media["schema"]).iter_errors(fixture["value"]))
        assert not errors, f"{label} {fixture['operationId']}: {errors[0].message if errors else ''}"
        counts["fixtures"] += 1
        if fixture["provenance"] == "upstream-captured":
            counts["upstream_captured_fixtures"] += 1


def check_field_tables(document, path, counts):
    schema = None
    rows = {}

    def check_rows():
        if schema is None:
            return
        assert schema.get("properties", {}).keys() <= rows.keys(), f"Missing REST field rows: {path}"
        for name in schema.get("properties", {}):
            expected = "да" if name in schema.get("required", []) else "нет"
            assert rows[name] == expected, f"Wrong required flag for {name}: {path}"
            counts["field_table_rows"] += 1

    for line in path.read_text(encoding="utf-8").splitlines() + ["## end"]:
        if line.startswith("## "):
            check_rows()
            schema, rows = None, {}
            if line.startswith("## REST "):
                _, _, method, route = line.split(" ", 3)
                operation = document["paths"].get(route, {}).get(method.lower(), {})
                media = operation.get("requestBody", {}).get("content", {}).get("application/json")
                if media:
                    schema = resolve(document, media["schema"])
        elif schema is not None and line.startswith("|") and not line.startswith(("| Поле |", "|---")):
            parts = line.split("|")
            rows[parts[1]] = parts[3]


def check_corrections(documents, official, counts):
    provenance = load(CONTRACTS / "common/manual-provenance.json")
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == provenance["sha256"]
    assert len(list(operations(official))) == 235
    actual = {(method, path): operation for document in documents.values() for method, path, operation in operations(document)}
    expected = {(method, path): operation for method, path, operation in operations(official)}
    assert actual.keys() == expected.keys()
    for key, operation in expected.items():
        local = actual[key]
        assert local["operationId"] == operation["operationId"]
        if "requestBody" in operation:
            upstream_schema = resolve(official, operation["requestBody"]["content"]["application/json"]["schema"])
            component = operation["x-route-defaults"]["component"]
            local_schema = resolve(documents[component], local["requestBody"]["content"]["application/json"]["schema"])
            assert local_schema == upstream_schema, f"Request schema differs from Manual: {key}"
    for document in documents.values():
        assert document["security"] == [{"BearerAuth": []}, {"JoomlaToken": []}, {"BasicAuth": []}]
        for _, _, operation in operations(document):
            if operation["operationId"].startswith("com_joomlaupdate_"):
                assert operation["security"] == [{"JUpdateToken": []}]
                assert not any(parameter.get("name") == "X-JUpdate-Token" for parameter in operation["parameters"])

    # Omission regressions: XML defaults cannot satisfy the API's create contract.
    for component, route, fields in [
        ("com_content", "/v1/content/articles", {"language"}),
        ("com_tags", "/v1/tags", {"parent_id", "description", "language"}),
        ("com_modules", "/v1/modules/administrator", {"client_id", "language", "params"}),
        ("com_menus", "/v1/menus/administrator", {"client_id"}),
    ]:
        document = documents[component]
        media = document["paths"][route]["post"]["requestBody"]["content"]["application/json"]
        schema = resolve(document, media["schema"])
        assert fields <= set(schema["required"])
        body = media.get("example") or media["examples"]["minimal"]["value"]
        for field in fields:
            omitted = {key: value for key, value in body.items() if key != field}
            assert not validator(document, media["schema"]).is_valid(omitted)
            counts["omission_regressions"] += 1
    fields = documents["com_fields"]
    for method, route, operation in operations(fields):
        if method != "post":
            continue
        media = operation["requestBody"]["content"]["application/json"]
        schema = resolve(fields, media["schema"])
        required = {"context", "description"} | ({"params"} if "/groups/" not in route else set())
        assert required <= set(schema["required"])
        body = media.get("example") or media["examples"]["minimal"]["value"]
        assert body["context"] == operation["x-route-defaults"]["context"]
        for field in required:
            assert not validator(fields, media["schema"]).is_valid({key: value for key, value in body.items() if key != field})
            counts["omission_regressions"] += 1
    media = documents["com_media"]
    assert "/v1/media/files/{path}/" not in media["paths"]
    assert len(media["paths"]["/v1/media/files/{path}"]["get"]["responses"]["200"]["content"]["application/vnd.api+json"]["schema"]["oneOf"]) == 2
    assert any(parameter.get("name") == "path" and parameter["in"] == "query"
               for parameter in media["paths"]["/v1/media/files"]["get"]["parameters"])
    # Runtime captures need to be accepted by strict response schemas too.
    counts["manual_operations_matched"] = len(actual)


def main(args):
    counts = Counter()
    official = load(SOURCE)
    check_document(official, "Joomla Manual snapshot", counts)
    current = {}
    for path in sorted((CONTRACTS / "versions").glob("*/components/*/openapi.json")):
        document = load(path)
        check_document(document, str(path.relative_to(CONTRACTS)), counts)
        check_fixtures(document, load(path.with_name("examples.json")), path.parent.name, counts)
        check_field_tables(document, path.with_name("fields.md"), counts)
        if path.parents[2].name == "6.2.0":
            current[path.parent.name] = document
    check_corrections(current, official, counts)
    result = {"status": "pass", "scope": "OpenAPI 3.1, JSON Schema, embedded examples and fixtures; no live Joomla requests",
              "manual_ref": "ab18edff1038bdd2d70b3983a8bbc3e43c7d7cec", "counts": dict(counts), "errors": []}
    if args.report:
        Path(args.report).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--report")
    main(parser.parse_args())
