# com_fields REST API — Joomla 6.2.0

Пакет joomla.rest-api.fields. Версия ядра: 6.2.0.

Определение поля, группа и значение поля у владельца — разные сущности.
Контекст задан маршрутом: com_content.article/categories, com_contact.contact/categories/mail,
com_users.user. name — ключ значения; id — ID определения. assigned_cat_ids
ограничивает применимость. fieldparams выбирается по типу из plugins/fields.
params описывает отображение/поведение. Значения передаются через com_fields
в операции владельца; поддерживаемые контроллеры также принимают имя поля сверху.
Subform сохраняет строки целиком; частичный merge rowN ядром не гарантируется.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_fields/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_fields/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_fields/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_fields/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_fields/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_fields/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/fields/contacts/contact|fields.displayList|source-derived|
|POST|/v1/fields/contacts/contact|fields.add|source-derived|
|GET|/v1/fields/contacts/contact/{id}|fields.displayItem|source-derived|
|PATCH|/v1/fields/contacts/contact/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/contacts/contact/{id}|fields.delete|source-derived|
|GET|/v1/fields/contacts/mail|fields.displayList|source-derived|
|POST|/v1/fields/contacts/mail|fields.add|source-derived|
|GET|/v1/fields/contacts/mail/{id}|fields.displayItem|source-derived|
|PATCH|/v1/fields/contacts/mail/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/contacts/mail/{id}|fields.delete|source-derived|
|GET|/v1/fields/contacts/categories|fields.displayList|source-derived|
|POST|/v1/fields/contacts/categories|fields.add|source-derived|
|GET|/v1/fields/contacts/categories/{id}|fields.displayItem|source-derived|
|PATCH|/v1/fields/contacts/categories/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/contacts/categories/{id}|fields.delete|source-derived|
|GET|/v1/fields/groups/contacts/contact|groups.displayList|source-derived|
|POST|/v1/fields/groups/contacts/contact|groups.add|source-derived|
|GET|/v1/fields/groups/contacts/contact/{id}|groups.displayItem|source-derived|
|PATCH|/v1/fields/groups/contacts/contact/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/contacts/contact/{id}|groups.delete|source-derived|
|GET|/v1/fields/groups/contacts/mail|groups.displayList|source-derived|
|POST|/v1/fields/groups/contacts/mail|groups.add|source-derived|
|GET|/v1/fields/groups/contacts/mail/{id}|groups.displayItem|source-derived|
|PATCH|/v1/fields/groups/contacts/mail/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/contacts/mail/{id}|groups.delete|source-derived|
|GET|/v1/fields/groups/contacts/categories|groups.displayList|source-derived|
|POST|/v1/fields/groups/contacts/categories|groups.add|source-derived|
|GET|/v1/fields/groups/contacts/categories/{id}|groups.displayItem|source-derived|
|PATCH|/v1/fields/groups/contacts/categories/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/contacts/categories/{id}|groups.delete|source-derived|
|GET|/v1/fields/content/articles|fields.displayList|source-derived|
|POST|/v1/fields/content/articles|fields.add|source-derived|
|GET|/v1/fields/content/articles/{id}|fields.displayItem|source-derived|
|PATCH|/v1/fields/content/articles/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/content/articles/{id}|fields.delete|source-derived|
|GET|/v1/fields/content/categories|fields.displayList|source-derived|
|POST|/v1/fields/content/categories|fields.add|source-derived|
|GET|/v1/fields/content/categories/{id}|fields.displayItem|source-derived|
|PATCH|/v1/fields/content/categories/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/content/categories/{id}|fields.delete|source-derived|
|GET|/v1/fields/groups/content/articles|groups.displayList|source-derived|
|POST|/v1/fields/groups/content/articles|groups.add|source-derived|
|GET|/v1/fields/groups/content/articles/{id}|groups.displayItem|source-derived|
|PATCH|/v1/fields/groups/content/articles/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/content/articles/{id}|groups.delete|source-derived|
|GET|/v1/fields/groups/content/categories|groups.displayList|source-derived|
|POST|/v1/fields/groups/content/categories|groups.add|source-derived|
|GET|/v1/fields/groups/content/categories/{id}|groups.displayItem|source-derived|
|PATCH|/v1/fields/groups/content/categories/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/content/categories/{id}|groups.delete|source-derived|
|GET|/v1/fields/users|fields.displayList|source-derived|
|POST|/v1/fields/users|fields.add|source-derived|
|GET|/v1/fields/users/{id}|fields.displayItem|source-derived|
|PATCH|/v1/fields/users/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/users/{id}|fields.delete|source-derived|
|GET|/v1/fields/groups/users|groups.displayList|source-derived|
|POST|/v1/fields/groups/users|groups.add|source-derived|
|GET|/v1/fields/groups/users/{id}|groups.displayItem|source-derived|
|PATCH|/v1/fields/groups/users/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/users/{id}|groups.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
