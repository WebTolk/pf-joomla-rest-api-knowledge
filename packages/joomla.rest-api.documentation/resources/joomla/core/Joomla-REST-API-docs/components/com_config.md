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


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_config/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_config/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_config/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_config/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_config/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_config/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/config/application|application.displayList|source-derived|
|PATCH|/v1/config/application|application.edit|source-derived|
|GET|/v1/config/{component_name}|component.displayList|source-derived|
|PATCH|/v1/config/{component_name}|component.edit|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
