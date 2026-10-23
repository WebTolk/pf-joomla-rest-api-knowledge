# com_config REST API — Joomla 5.4.8

Пакет joomla.rest-api.config. Версия ядра: 5.4.8.

GET application возвращает коллекцию, где ресурс содержит ОДНУ настройку.
PATCH application принимает плоский объект настроек.
GET config/{component_name} также возвращает настройки отдельными ресурсами.
PATCH компонента принимает плоские параметры, не {params:{...}}, и накладывает
их на существующие до валидации. PATCH не возвращает новый объект конфигурации.
Схема выбирается по component_name из Config_com_*; сторонний компонент
требует отдельной схемы. Реальные пароли и локальные пути в примерах отсутствуют.
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
|GET|/v1/config/application|application.displayList|source-derived|
|PATCH|/v1/config/application|application.edit|source-derived|
|GET|/v1/config/{component_name}|component.displayList|source-derived|
|PATCH|/v1/config/{component_name}|component.edit|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
