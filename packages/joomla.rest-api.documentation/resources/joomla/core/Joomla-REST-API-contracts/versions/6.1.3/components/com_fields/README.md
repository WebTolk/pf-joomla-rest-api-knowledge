# com_fields REST API — Joomla 6.1.3

Пакет joomla.rest-api.fields. Версия ядра: 6.1.3.

Определение поля, группа и значение поля у владельца — разные сущности.
Контекст задан маршрутом: com_content.article/categories, com_contact.contact/categories/mail,
com_users.user. name — ключ значения; id — ID определения. assigned_cat_ids
ограничивает применимость. fieldparams выбирается по типу из plugins/fields.
params описывает отображение/поведение. Значения передаются через com_fields
в операции владельца; поддерживаемые контроллеры также принимают имя поля сверху.
Subform сохраняет строки целиком; частичный merge rowN ядром не гарантируется.
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
|GET|/v1/fields/contacts/contact|fields.displayList|source-derived|
|GET|/v1/fields/contacts/contact/{id}|fields.displayItem|source-derived|
|POST|/v1/fields/contacts/contact|fields.add|source-derived|
|PATCH|/v1/fields/contacts/contact/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/contacts/contact/{id}|fields.delete|source-derived|
|GET|/v1/fields/contacts/mail|fields.displayList|source-derived|
|GET|/v1/fields/contacts/mail/{id}|fields.displayItem|source-derived|
|POST|/v1/fields/contacts/mail|fields.add|source-derived|
|PATCH|/v1/fields/contacts/mail/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/contacts/mail/{id}|fields.delete|source-derived|
|GET|/v1/fields/contacts/categories|fields.displayList|source-derived|
|GET|/v1/fields/contacts/categories/{id}|fields.displayItem|source-derived|
|POST|/v1/fields/contacts/categories|fields.add|source-derived|
|PATCH|/v1/fields/contacts/categories/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/contacts/categories/{id}|fields.delete|source-derived|
|GET|/v1/fields/groups/contacts/contact|groups.displayList|source-derived|
|GET|/v1/fields/groups/contacts/contact/{id}|groups.displayItem|source-derived|
|POST|/v1/fields/groups/contacts/contact|groups.add|source-derived|
|PATCH|/v1/fields/groups/contacts/contact/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/contacts/contact/{id}|groups.delete|source-derived|
|GET|/v1/fields/groups/contacts/mail|groups.displayList|source-derived|
|GET|/v1/fields/groups/contacts/mail/{id}|groups.displayItem|source-derived|
|POST|/v1/fields/groups/contacts/mail|groups.add|source-derived|
|PATCH|/v1/fields/groups/contacts/mail/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/contacts/mail/{id}|groups.delete|source-derived|
|GET|/v1/fields/groups/contacts/categories|groups.displayList|source-derived|
|GET|/v1/fields/groups/contacts/categories/{id}|groups.displayItem|source-derived|
|POST|/v1/fields/groups/contacts/categories|groups.add|source-derived|
|PATCH|/v1/fields/groups/contacts/categories/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/contacts/categories/{id}|groups.delete|source-derived|
|GET|/v1/fields/content/articles|fields.displayList|source-derived|
|GET|/v1/fields/content/articles/{id}|fields.displayItem|source-derived|
|POST|/v1/fields/content/articles|fields.add|source-derived|
|PATCH|/v1/fields/content/articles/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/content/articles/{id}|fields.delete|source-derived|
|GET|/v1/fields/content/categories|fields.displayList|source-derived|
|GET|/v1/fields/content/categories/{id}|fields.displayItem|source-derived|
|POST|/v1/fields/content/categories|fields.add|source-derived|
|PATCH|/v1/fields/content/categories/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/content/categories/{id}|fields.delete|source-derived|
|GET|/v1/fields/groups/content/articles|groups.displayList|source-derived|
|GET|/v1/fields/groups/content/articles/{id}|groups.displayItem|source-derived|
|POST|/v1/fields/groups/content/articles|groups.add|source-derived|
|PATCH|/v1/fields/groups/content/articles/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/content/articles/{id}|groups.delete|source-derived|
|GET|/v1/fields/groups/content/categories|groups.displayList|source-derived|
|GET|/v1/fields/groups/content/categories/{id}|groups.displayItem|source-derived|
|POST|/v1/fields/groups/content/categories|groups.add|source-derived|
|PATCH|/v1/fields/groups/content/categories/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/content/categories/{id}|groups.delete|source-derived|
|GET|/v1/fields/users|fields.displayList|source-derived|
|GET|/v1/fields/users/{id}|fields.displayItem|source-derived|
|POST|/v1/fields/users|fields.add|source-derived|
|PATCH|/v1/fields/users/{id}|fields.edit|source-derived|
|DELETE|/v1/fields/users/{id}|fields.delete|source-derived|
|GET|/v1/fields/groups/users|groups.displayList|source-derived|
|GET|/v1/fields/groups/users/{id}|groups.displayItem|source-derived|
|POST|/v1/fields/groups/users|groups.add|source-derived|
|PATCH|/v1/fields/groups/users/{id}|groups.edit|source-derived|
|DELETE|/v1/fields/groups/users/{id}|groups.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
