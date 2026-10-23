# com_newsfeeds REST API — Joomla 5.4.8

Пакет joomla.rest-api.newsfeeds. Версия ядра: 5.4.8.

См. форму и схему ответа endpoint.
Для снимка 5.4.8 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

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
|GET|/v1/newsfeeds/feeds|feeds.displayList|source-derived|
|GET|/v1/newsfeeds/feeds/{id}|feeds.displayItem|source-derived|
|POST|/v1/newsfeeds/feeds|feeds.add|source-derived|
|PATCH|/v1/newsfeeds/feeds/{id}|feeds.edit|source-derived|
|DELETE|/v1/newsfeeds/feeds/{id}|feeds.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
