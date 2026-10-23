# com_banners REST API — Joomla 6.1.3

Пакет joomla.rest-api.banners. Версия ядра: 6.1.3.

См. форму и схему ответа endpoint.
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
|GET|/v1/banners|banners.displayList|source-derived|
|GET|/v1/banners/{id}|banners.displayItem|source-derived|
|POST|/v1/banners|banners.add|source-derived|
|PATCH|/v1/banners/{id}|banners.edit|source-derived|
|DELETE|/v1/banners/{id}|banners.delete|source-derived|
|GET|/v1/banners/clients|clients.displayList|source-derived|
|GET|/v1/banners/clients/{id}|clients.displayItem|source-derived|
|POST|/v1/banners/clients|clients.add|source-derived|
|PATCH|/v1/banners/clients/{id}|clients.edit|source-derived|
|DELETE|/v1/banners/clients/{id}|clients.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
