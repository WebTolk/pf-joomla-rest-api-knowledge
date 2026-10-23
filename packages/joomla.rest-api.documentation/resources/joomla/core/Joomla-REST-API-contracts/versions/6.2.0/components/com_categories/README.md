# com_categories REST API — Joomla 6.2.0

Пакет joomla.rest-api.categories. Версия ядра: 6.2.0.

Контекст категории фиксируется defaults.extension маршрута: com_content, com_contact,
com_newsfeeds или com_banners. parent_id относится к дереву того же extension.
lft/rgt/level — вычисляемые данные. location/location_reference читаются из тела
JSON после сохранения для перемещения в дереве; это отдельная операция setLocation.
Параметры категории могут дополняться формами конкретного компонента.
В 6.2.0 GET списка поддерживает filter[state] (INT), который передаётся в filter.published модели.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

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
|GET|/v1/banners/categories|categories.displayList|source-derived|
|GET|/v1/banners/categories/{id}|categories.displayItem|source-derived|
|POST|/v1/banners/categories|categories.add|source-derived|
|PATCH|/v1/banners/categories/{id}|categories.edit|source-derived|
|DELETE|/v1/banners/categories/{id}|categories.delete|source-derived|
|GET|/v1/contacts/categories|categories.displayList|source-derived|
|GET|/v1/contacts/categories/{id}|categories.displayItem|source-derived|
|POST|/v1/contacts/categories|categories.add|source-derived|
|PATCH|/v1/contacts/categories/{id}|categories.edit|source-derived|
|DELETE|/v1/contacts/categories/{id}|categories.delete|source-derived|
|GET|/v1/content/categories|categories.displayList|source-derived|
|GET|/v1/content/categories/{id}|categories.displayItem|source-derived|
|POST|/v1/content/categories|categories.add|source-derived|
|PATCH|/v1/content/categories/{id}|categories.edit|source-derived|
|DELETE|/v1/content/categories/{id}|categories.delete|source-derived|
|GET|/v1/newsfeeds/categories|categories.displayList|source-derived|
|GET|/v1/newsfeeds/categories/{id}|categories.displayItem|source-derived|
|POST|/v1/newsfeeds/categories|categories.add|source-derived|
|PATCH|/v1/newsfeeds/categories/{id}|categories.edit|source-derived|
|DELETE|/v1/newsfeeds/categories/{id}|categories.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
