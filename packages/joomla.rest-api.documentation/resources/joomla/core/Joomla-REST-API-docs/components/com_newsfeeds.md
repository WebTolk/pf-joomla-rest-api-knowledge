# com_newsfeeds REST API — Joomla 6.2.0

Пакет joomla.rest-api.newsfeeds. Версия ядра: 6.2.0.

См. форму и схему ответа endpoint.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_newsfeeds/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_newsfeeds/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_newsfeeds/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_newsfeeds/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_newsfeeds/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_newsfeeds/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/newsfeeds/feeds|feeds.displayList|source-derived|
|POST|/v1/newsfeeds/feeds|feeds.add|source-derived|
|GET|/v1/newsfeeds/feeds/{id}|feeds.displayItem|source-derived|
|PATCH|/v1/newsfeeds/feeds/{id}|feeds.edit|source-derived|
|DELETE|/v1/newsfeeds/feeds/{id}|feeds.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
