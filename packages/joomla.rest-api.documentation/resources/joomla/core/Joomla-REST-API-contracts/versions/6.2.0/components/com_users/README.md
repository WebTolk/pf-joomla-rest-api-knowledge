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
|GET|/v1/users|users.displayList|source-derived|
|GET|/v1/users/{id}|users.displayItem|source-derived|
|POST|/v1/users|users.add|source-derived|
|PATCH|/v1/users/{id}|users.edit|source-derived|
|DELETE|/v1/users/{id}|users.delete|source-derived|
|GET|/v1/users/groups|groups.displayList|source-derived|
|GET|/v1/users/groups/{id}|groups.displayItem|source-derived|
|POST|/v1/users/groups|groups.add|source-derived|
|PATCH|/v1/users/groups/{id}|groups.edit|source-derived|
|DELETE|/v1/users/groups/{id}|groups.delete|source-derived|
|GET|/v1/users/levels|levels.displayList|source-derived|
|GET|/v1/users/levels/{id}|levels.displayItem|source-derived|
|POST|/v1/users/levels|levels.add|source-derived|
|PATCH|/v1/users/levels/{id}|levels.edit|source-derived|
|DELETE|/v1/users/levels/{id}|levels.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
