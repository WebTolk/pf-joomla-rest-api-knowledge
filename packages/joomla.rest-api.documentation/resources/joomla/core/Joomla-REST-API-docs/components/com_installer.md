# com_installer REST API — Joomla 6.2.0

Пакет joomla.rest-api.installer. Версия ядра: 6.2.0.

GET extensions перечисляет расширения; GET languages — доступные языковые пакеты.
POST languages -> languages.install зарегистрирован, но метод install отсутствует
в API LanguagesController и ApiController этих снимков. Он отмечен как
registered-unimplemented: успешный ответ не выдумывается. Установка через UI
требует соответствующей области задания.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_installer/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_installer/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_installer/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_installer/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_installer/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_installer/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/extensions|manage.displayList|source-derived|
|GET|/v1/languages|languages.displayList|source-derived|
|POST|/v1/languages|languages.install|registered-unimplemented|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
