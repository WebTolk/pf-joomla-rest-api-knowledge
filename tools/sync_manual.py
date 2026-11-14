"""Project the pinned Joomla Manual specification into the PF component contracts.

The official snapshot is kept verbatim. Component documents retain PF metadata,
core extension parameter schemas and the two components without standalone routes.
Shared response/parameter references and schema aliases are expanded so each
component remains independently readable without another installed component.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "packages/joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts"
VERSION = CONTRACTS / "versions/6.2.0"
SOURCE = VERSION / "openapi.json"
METHODS = {"get", "post", "patch", "delete", "put", "head", "options", "trace"}
MANUAL_REF = "ab18edff1038bdd2d70b3983a8bbc3e43c7d7cec"
MANUAL_URL = f"https://github.com/joomla/Manual/blob/{MANUAL_REF}/static/openapi/joomla-6.2.0.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def resolve(document, value):
    """Resolve a reference object, retaining any JSON Schema sibling keywords."""
    value = copy.deepcopy(value)
    seen = set()
    while isinstance(value, dict) and "$ref" in value:
        ref = value.pop("$ref")
        assert ref.startswith("#/"), ref
        assert ref not in seen, f"Cyclic alias: {ref}"
        seen.add(ref)
        target = document
        for part in ref[2:].split("/"):
            target = target[part.replace("~1", "/").replace("~0", "~")]
        value = copy.deepcopy(target) | value
    return value


def expand_references(document, value):
    """Inline reusable parameters/responses; keep recursive schema references."""
    if isinstance(value, list):
        return [expand_references(document, item) for item in value]
    if not isinstance(value, dict):
        return value
    if "$ref" in value and not value["$ref"].startswith("#/components/schemas/"):
        value = resolve(document, value)
    return {key: expand_references(document, item) for key, item in value.items()}


def references(value):
    if isinstance(value, list):
        for item in value:
            yield from references(item)
    elif isinstance(value, dict):
        if "$ref" in value:
            yield value["$ref"]
        for item in value.values():
            yield from references(item)


def correct_guidance(component, operation):
    # The merged component guides fix these statements, but the aggregate
    # specification still repeats older prose in operation descriptions.
    text = operation.get("description", "")
    if component == "com_fields":
        text = text.replace(
            "The route fixes the context: article, category, contact, contact-mail and user fields have separate collections.",
            "The route selects the context for reading. When creating a field or field group, also send context matching the route: it is not applied when saving. Without context the record can be saved but the response is 404. A field also needs description and non-empty params; a group needs description. Field names must be unique across contexts.",
        )
    elif component == "com_modules":
        text = text.replace(
            "Site routes set client_id=0; administrator routes set client_id=1.",
            "Site and administrator routes select client_id=0/1 for reading. On POST /modules/administrator explicitly send client_id: 1; otherwise a site module can be saved and the response is 404. A new module also needs language and non-empty params.",
        )
    elif component == "com_menus" and operation["operationId"] == "com_menus_post_v1_menus_administrator":
        text += "\n\nSend client_id: 1 explicitly. Without it this route can return 200 while creating a site menu."
    operation["description"] = text


def fixtures(document):
    result = []
    for item in document["paths"].values():
        for method, operation in item.items():
            if method not in METHODS:
                continue
            contents = [("request", None, operation.get("requestBody", {}).get("content", {}))]
            contents.extend(("response", int(status), response.get("content", {}))
                            for status, response in operation["responses"].items() if status.isdigit() and int(status) < 300)
            for direction, status, content in contents:
                for media_type, media in content.items():
                    examples = media.get("examples", {})
                    if "example" in media:
                        examples = {"default": {"value": media["example"]}} | examples
                    for name, example in examples.items():
                        if "value" not in example:
                            continue
                        entry = {"operationId": operation["operationId"], "direction": direction,
                                 "media_type": media_type, "example": name,
                                 "value": example["value"],
                                 "provenance": "upstream-captured" if name == "captured" else "upstream-example",
                                 "source": MANUAL_URL}
                        if status is not None:
                            entry["status"] = status
                        schema = media.get("schema", {})
                        if "$ref" in schema:
                            entry["schema"] = schema["$ref"].rsplit("/", 1)[-1]
                        result.append(entry)
    return result


def update_field_tables(path: Path, document):
    """Refresh only REST sections; leave the separate XML/UI inventory intact."""
    lines = path.read_text(encoding="utf-8").splitlines()
    output = []
    schema = None
    in_table = False
    row_names = set()

    def finish_table():
        nonlocal in_table
        if in_table and schema:
            for name, field in schema.get("properties", {}).items():
                if name in row_names:
                    continue
                required = "да" if name in schema.get("required", []) else "нет"
                kind = json.dumps(field.get("type", "anyOf"))
                description = field.get("description", "Context matching the route; send explicitly when creating.").replace("|", "/").replace("\n", " ")
                output.append(f'|{name}|{kind}|{required}|""|{description}||')
        in_table = False

    for line in lines:
        if line.startswith("## "):
            finish_table()
            if output and output[-1].startswith("|"):
                output.append("")
            schema = None
            row_names = set()
            if line.startswith("## REST "):
                _, _, method, route = line.split(" ", 3)
                operation = document["paths"].get(route, {}).get(method.lower(), {})
                media = operation.get("requestBody", {}).get("content", {}).get("application/json")
                if media:
                    schema = resolve(document, media["schema"])
        if line.startswith("| Поле |") and schema is not None:
            in_table = True
            output.append(line)
            continue
        if in_table and line.startswith("|---"):
            output.append(line)
            continue
        if in_table and line.startswith("|"):
            parts = line.split("|")
            field = parts[1]
            row_names.add(field)
            if field in schema.get("properties", {}):
                parts[3] = "да" if field in schema.get("required", []) else "нет"
            output.append("|".join(parts))
            continue
        if in_table:
            finish_table()
        output.append(line)
    finish_table()
    path.write_text("\n".join(output) + "\n", encoding="utf-8", newline="\n")


def main():
    official = load(SOURCE)
    counts = {}
    for path in sorted((VERSION / "components").glob("*/openapi.json")):
        document = load(path)
        component = path.parent.name
        paths = {}
        for route, item in official["paths"].items():
            operations = {method: expand_references(official, copy.deepcopy(operation))
                          for method, operation in item.items() if method in METHODS
                          and operation.get("x-route-defaults", {}).get("component") == component}
            for operation in operations.values():
                correct_guidance(component, operation)
            if operations:
                paths[route] = operations
        document["paths"] = paths
        document["servers"] = copy.deepcopy(official["servers"])
        document["security"] = copy.deepcopy(official["security"])
        schemas = document["components"]["schemas"]
        for name in list(schemas):
            if name in official["components"]["schemas"]:
                schemas[name] = resolve(official, {"$ref": f"#/components/schemas/{name}"})
        document["components"]["securitySchemes"] = copy.deepcopy(official["components"]["securitySchemes"])
        while True:
            missing = {ref.rsplit("/", 1)[-1] for ref in references(document)
                       if ref.startswith("#/components/schemas/") and ref.rsplit("/", 1)[-1] not in schemas}
            if not missing:
                break
            for name in sorted(missing):
                schemas[name] = resolve(official, {"$ref": f"#/components/schemas/{name}"})
        document["tags"] = [tag for tag in official["tags"] if tag["name"] in {
            tag for item in paths.values() for operation in item.values() for tag in operation.get("tags", [])}]
        document["x-documentation-source"] = {"url": MANUAL_URL, "pull_request": 724,
            "guide_corrections": "context and client_id on create, from merged fork PRs #1 and #2"}
        save(path, document)
        save(path.with_name("examples.json"), fixtures(document))
        update_field_tables(path.with_name("fields.md"), document)
        counts[component] = sum(len(item) for item in paths.values())
    print(json.dumps({"component_operations": counts, "total": sum(counts.values())}))


if __name__ == "__main__":
    main()
