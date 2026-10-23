# com_config REST API — Joomla 6.2.0

Пакет joomla.rest-api.config. Версия ядра: 6.2.0.

GET application возвращает коллекцию, где ресурс содержит ОДНУ настройку.
PATCH application принимает плоский объект настроек.
GET config/{component_name} также возвращает настройки отдельными ресурсами.
PATCH компонента принимает плоские параметры, не {params:{...}}, и накладывает
их на существующие до валидации. PATCH не возвращает новый объект конфигурации.
Схема выбирается по component_name из Config_com_*; сторонний компонент
требует отдельной схемы. Реальные пароли и локальные пути в примерах отсутствуют.
В 6.2.0 smtpauth — варианты 0/1/2 (отключено, пароль, OAuth 2.0), включая числовые строки; прежний boolean-контракт не применять. Поля smtp_oauth2_* описаны в форме. REST-запись настроек сама по себе не выполняет браузерное согласие OAuth.
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
|GET|/v1/config/application|application.displayList|source-derived|
|PATCH|/v1/config/application|application.edit|source-derived|
|GET|/v1/config/{component_name}|component.displayList|source-derived|
|PATCH|/v1/config/{component_name}|component.edit|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
