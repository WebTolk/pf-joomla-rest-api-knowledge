# com_categories REST API — Joomla 6.2.0

Пакет joomla.rest-api.categories. Версия ядра: 6.2.0.

Контекст категории фиксируется defaults.extension маршрута: com_content, com_contact,
com_newsfeeds или com_banners. parent_id относится к дереву того же extension.
lft/rgt/level — вычисляемые данные. location/location_reference читаются из тела
JSON после сохранения для перемещения в дереве; это отдельная операция setLocation.
Параметры категории могут дополняться формами конкретного компонента.
В 6.2.0 GET списка поддерживает filter[state] (INT), который передаётся в filter.published модели.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_categories/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_categories/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_categories/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_categories/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_categories/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_categories/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/banners/categories|categories.displayList|source-derived|
|POST|/v1/banners/categories|categories.add|source-derived|
|GET|/v1/banners/categories/{id}|categories.displayItem|source-derived|
|PATCH|/v1/banners/categories/{id}|categories.edit|source-derived|
|DELETE|/v1/banners/categories/{id}|categories.delete|source-derived|
|GET|/v1/contacts/categories|categories.displayList|source-derived|
|POST|/v1/contacts/categories|categories.add|source-derived|
|GET|/v1/contacts/categories/{id}|categories.displayItem|source-derived|
|PATCH|/v1/contacts/categories/{id}|categories.edit|source-derived|
|DELETE|/v1/contacts/categories/{id}|categories.delete|source-derived|
|GET|/v1/content/categories|categories.displayList|source-derived|
|POST|/v1/content/categories|categories.add|source-derived|
|GET|/v1/content/categories/{id}|categories.displayItem|source-derived|
|PATCH|/v1/content/categories/{id}|categories.edit|source-derived|
|DELETE|/v1/content/categories/{id}|categories.delete|source-derived|
|GET|/v1/newsfeeds/categories|categories.displayList|source-derived|
|POST|/v1/newsfeeds/categories|categories.add|source-derived|
|GET|/v1/newsfeeds/categories/{id}|categories.displayItem|source-derived|
|PATCH|/v1/newsfeeds/categories/{id}|categories.edit|source-derived|
|DELETE|/v1/newsfeeds/categories/{id}|categories.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
