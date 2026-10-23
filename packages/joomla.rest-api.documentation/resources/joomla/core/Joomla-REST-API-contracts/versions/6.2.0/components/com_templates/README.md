# com_templates REST API — Joomla 6.2.0

Пакет joomla.rest-api.templates. Версия ядра: 6.2.0.

См. форму и схему ответа endpoint.
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
|GET|/v1/templates/styles/site|styles.displayList|source-derived|
|GET|/v1/templates/styles/site/{id}|styles.displayItem|source-derived|
|POST|/v1/templates/styles/site|styles.add|source-derived|
|PATCH|/v1/templates/styles/site/{id}|styles.edit|source-derived|
|DELETE|/v1/templates/styles/site/{id}|styles.delete|source-derived|
|GET|/v1/templates/styles/administrator|styles.displayList|source-derived|
|GET|/v1/templates/styles/administrator/{id}|styles.displayItem|source-derived|
|POST|/v1/templates/styles/administrator|styles.add|source-derived|
|PATCH|/v1/templates/styles/administrator/{id}|styles.edit|source-derived|
|DELETE|/v1/templates/styles/administrator/{id}|styles.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
