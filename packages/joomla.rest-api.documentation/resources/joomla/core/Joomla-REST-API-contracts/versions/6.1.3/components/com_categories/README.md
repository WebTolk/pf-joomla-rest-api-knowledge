# com_categories REST API — Joomla 6.1.3

Пакет joomla.rest-api.categories. Версия ядра: 6.1.3.

Контекст категории фиксируется defaults.extension маршрута: com_content, com_contact,
com_newsfeeds или com_banners. parent_id относится к дереву того же extension.
lft/rgt/level — вычисляемые данные. location/location_reference читаются из тела
JSON после сохранения для перемещения в дереве; это отдельная операция setLocation.
Параметры категории могут дополняться формами конкретного компонента.
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
