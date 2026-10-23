# com_languages REST API — Joomla 6.2.0

Пакет joomla.rest-api.languages. Версия ядра: 6.2.0.

lang_code — тег языка, sef — сегмент URL, title_native — родное название.
Пути overrides/{site|administrator}/{lang_code} создаются для установленных языков.
ID override — строковая константа [A-Z0-9_]+. Запись: key/override; ответ: value.
Сохранение OverridesController читает app/lang_code из post input. ApiApplication
помещает параметры маршрута в post для POST, но в общий input для PATCH. Поэтому
POST получает правильный контекст, а PATCH не гарантирует его из одного route/JSON.
При неподдерживаемом сохранении использовать UI fallback, сохранив клиент/язык.
Поиск требует searchstring и searchtype=constant|value.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_languages/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_languages/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_languages/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_languages/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_languages/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_languages/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/languages/content|languages.displayList|source-derived|
|POST|/v1/languages/content|languages.add|source-derived|
|GET|/v1/languages/content/{id}|languages.displayItem|source-derived|
|PATCH|/v1/languages/content/{id}|languages.edit|source-derived|
|DELETE|/v1/languages/content/{id}|languages.delete|source-derived|
|POST|/v1/languages/overrides/search|strings.search|source-derived|
|POST|/v1/languages/overrides/search/cache/refresh|strings.refresh|source-derived|
|GET|/v1/languages/overrides/site/{lang_code}|overrides.displayList|source-derived|
|POST|/v1/languages/overrides/site/{lang_code}|overrides.add|source-derived|
|GET|/v1/languages/overrides/site/{lang_code}/{id}|overrides.displayItem|source-derived|
|PATCH|/v1/languages/overrides/site/{lang_code}/{id}|overrides.edit|source-derived|
|DELETE|/v1/languages/overrides/site/{lang_code}/{id}|overrides.delete|source-derived|
|GET|/v1/languages/overrides/administrator/{lang_code}|overrides.displayList|source-derived|
|POST|/v1/languages/overrides/administrator/{lang_code}|overrides.add|source-derived|
|GET|/v1/languages/overrides/administrator/{lang_code}/{id}|overrides.displayItem|source-derived|
|PATCH|/v1/languages/overrides/administrator/{lang_code}/{id}|overrides.edit|source-derived|
|DELETE|/v1/languages/overrides/administrator/{lang_code}/{id}|overrides.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
