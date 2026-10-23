# com_users REST API — Joomla 6.1.3

Пакет joomla.rest-api.users. Версия ядра: 6.1.3.

Пароли не возвращаются GET. POST при наличии password копирует его в password2.
PATCH с пропущенным password сохраняет пароль. Пропущенные groups восстанавливает
специальный обработчик. groups — ID групп; viewlevels.rules — группы доступа,
что отличается от вложенных правил ACL.
Фильтры registrationDateStart/End и lastVisitDateStart/End требуют RFC3339.
Для viewlevels POST rules — массив ID групп, PATCH rules — JSON-строка массива
(например "[2,3]"): API-контроллер вызывает json_decode до фильтра формы.
Массив в PATCH вызывает TypeError; пропуск rules использует сохранённую строку.
Профиль и custom fields могут расширяться user-плагинами.
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
