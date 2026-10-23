# com_templates REST API — Joomla 6.2.0

Пакет joomla.rest-api.templates. Версия ядра: 6.2.0.

См. форму и схему ответа endpoint.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_templates/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_templates/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_templates/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_templates/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_templates/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_templates/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/templates/styles/site|styles.displayList|source-derived|
|POST|/v1/templates/styles/site|styles.add|source-derived|
|GET|/v1/templates/styles/site/{id}|styles.displayItem|source-derived|
|PATCH|/v1/templates/styles/site/{id}|styles.edit|source-derived|
|DELETE|/v1/templates/styles/site/{id}|styles.delete|source-derived|
|GET|/v1/templates/styles/administrator|styles.displayList|source-derived|
|POST|/v1/templates/styles/administrator|styles.add|source-derived|
|GET|/v1/templates/styles/administrator/{id}|styles.displayItem|source-derived|
|PATCH|/v1/templates/styles/administrator/{id}|styles.edit|source-derived|
|DELETE|/v1/templates/styles/administrator/{id}|styles.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
