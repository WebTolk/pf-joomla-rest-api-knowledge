# com_languages REST API — Joomla 6.1.3

Пакет joomla.rest-api.languages. Версия ядра: 6.1.3.

lang_code — тег языка, sef — сегмент URL, title_native — родное название.
Пути overrides/{site|administrator}/{lang_code} создаются для установленных языков.
ID override — строковая константа [A-Z0-9_]+. Запись: key/override; ответ: value.
Сохранение OverridesController читает app/lang_code из post input. ApiApplication
помещает параметры маршрута в post для POST, но в общий input для PATCH. Поэтому
POST получает правильный контекст, а PATCH не гарантирует его из одного route/JSON.
При неподдерживаемом сохранении использовать UI fallback, сохранив клиент/язык.
Поиск требует searchstring и searchtype=constant|value.
Для снимка 6.1.3 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Состав

- [openapi.json](openapi.json): схемы запросов/ответов, параметры, коды и примеры.
- [fields.md](fields.md): типы, обязательность, enum/default, правила форм/showon.
- [extension-parameters.json](extension-parameters.json): параметры штатных расширений.
- [examples.json](examples.json): синтетические request/response fixtures.
- [errors.md](errors.md), [browser-fallback.md](browser-fallback.md).
- [coverage.json](coverage.json), [source-evidence.json](source-evidence.json): покрытие/SHA-256.
- [Общие правила](../../../../common/README.md).

## Маршруты

| Метод | Путь | Действие | Поддержка |
|---|---|---|---|
|GET|/v1/languages/content|languages.displayList|source-derived|
|GET|/v1/languages/content/{id}|languages.displayItem|source-derived|
|POST|/v1/languages/content|languages.add|source-derived|
|PATCH|/v1/languages/content/{id}|languages.edit|source-derived|
|DELETE|/v1/languages/content/{id}|languages.delete|source-derived|
|POST|/v1/languages/overrides/search|strings.search|source-derived|
|POST|/v1/languages/overrides/search/cache/refresh|strings.refresh|source-derived|
|GET|/v1/languages/overrides/site/{lang_code}|overrides.displayList|source-derived|
|GET|/v1/languages/overrides/site/{lang_code}/{id}|overrides.displayItem|source-derived|
|POST|/v1/languages/overrides/site/{lang_code}|overrides.add|source-derived|
|PATCH|/v1/languages/overrides/site/{lang_code}/{id}|overrides.edit|source-derived|
|DELETE|/v1/languages/overrides/site/{lang_code}/{id}|overrides.delete|source-derived|
|GET|/v1/languages/overrides/administrator/{lang_code}|overrides.displayList|source-derived|
|GET|/v1/languages/overrides/administrator/{lang_code}/{id}|overrides.displayItem|source-derived|
|POST|/v1/languages/overrides/administrator/{lang_code}|overrides.add|source-derived|
|PATCH|/v1/languages/overrides/administrator/{lang_code}/{id}|overrides.edit|source-derived|
|DELETE|/v1/languages/overrides/administrator/{lang_code}/{id}|overrides.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
