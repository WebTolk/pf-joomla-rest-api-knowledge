# com_users REST API — Joomla 6.2.0

Пакет joomla.rest-api.users. Версия ядра: 6.2.0.

Пароли не возвращаются GET. POST при наличии password копирует его в password2.
PATCH с пропущенным password сохраняет пароль. Пропущенные groups восстанавливает
специальный обработчик. groups — ID групп; viewlevels.rules — группы доступа,
что отличается от вложенных правил ACL.
Фильтры registrationDateStart/End и lastVisitDateStart/End требуют RFC3339.
Для viewlevels POST rules — массив ID групп, PATCH rules — JSON-строка массива
(например "[2,3]"): API-контроллер вызывает json_decode до фильтра формы.
Массив в PATCH вызывает TypeError; пропуск rules использует сохранённую строку.
Профиль и custom fields могут расширяться user-плагинами.
В 6.2.0 создание, изменение и удаление viewlevels требует core.admin на com_users. Права групп также проверяются через core.admin.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_users/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_users/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_users/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_users/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_users/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_users/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/users|users.displayList|source-derived|
|POST|/v1/users|users.add|source-derived|
|GET|/v1/users/{id}|users.displayItem|source-derived|
|PATCH|/v1/users/{id}|users.edit|source-derived|
|DELETE|/v1/users/{id}|users.delete|source-derived|
|GET|/v1/users/groups|groups.displayList|source-derived|
|POST|/v1/users/groups|groups.add|source-derived|
|GET|/v1/users/groups/{id}|groups.displayItem|source-derived|
|PATCH|/v1/users/groups/{id}|groups.edit|source-derived|
|DELETE|/v1/users/groups/{id}|groups.delete|source-derived|
|GET|/v1/users/levels|levels.displayList|source-derived|
|POST|/v1/users/levels|levels.add|source-derived|
|GET|/v1/users/levels/{id}|levels.displayItem|source-derived|
|PATCH|/v1/users/levels/{id}|levels.edit|source-derived|
|DELETE|/v1/users/levels/{id}|levels.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
