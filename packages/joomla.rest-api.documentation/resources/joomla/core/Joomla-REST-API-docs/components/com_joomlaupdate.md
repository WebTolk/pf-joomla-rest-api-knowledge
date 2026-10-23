# com_joomlaupdate REST API — Joomla 6.2.0

Пакет joomla.rest-api.joomlaupdate. Версия ядра: 6.2.0.

Требуется X-JUpdate-Token и включённое автообновление с допустимыми
updatesource/minimum_stability. Это отдельный токен, не X-Joomla-Token.
Неверный/пропущенный token вызывает InvalidParameterException с code=403,
но обработчик выставляет HTTP 400. HTTP и внутренний code различаются.
prepareUpdate требует доступную targetVersion; иначе generic Exception с code=410
преобразуется стандартным fallback formatter в HTTP 500 и code=500.
finalizeUpdate принимает fromVersion/updateFileName; имя очищается до basename.
success=false/errors при HTTP 200 означает неуспешное действие.
password prepareUpdate — временный секрет, в артефакты реальные значения не входят.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_joomlaupdate/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_joomlaupdate/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_joomlaupdate/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_joomlaupdate/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_joomlaupdate/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_joomlaupdate/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/joomlaupdate/healthcheck|healthcheck.show|source-derived|
|GET|/v1/joomlaupdate/getUpdate|updates.getUpdate|source-derived|
|POST|/v1/joomlaupdate/prepareUpdate|updates.prepareUpdate|source-derived|
|POST|/v1/joomlaupdate/finalizeUpdate|updates.finalizeUpdate|source-derived|
|POST|/v1/joomlaupdate/notificationSuccess|notification.success|source-derived|
|POST|/v1/joomlaupdate/notificationFailed|notification.failed|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
