# Postman: com_fields, Joomla 6.2.0

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 55. Операций компонента, отсутствующих в коллекции: 20.

## Замечания к телам

- POST /v1/fields/groups/contacts/contact: params.display_readonly; enum; '2' is not one of [0, 1, '0', '1']
- POST /v1/fields/groups/contacts/contact: params; additionalProperties; Additional properties are not allowed ('class', 'display', 'hint', 'label_class', 'label_render_class', 'layout', 'prefix', 'render_class', 'show_on', 'showlabel', 'suffix' were unexpected)
- POST /v1/fields/groups/contacts/contact: (корень тела); additionalProperties; Additional properties are not allowed ('context', 'default_value', 'group_id', 'label', 'name', 'required', 'type' were unexpected)
- POST /v1/fields/groups/contacts/contact: params.display_readonly; enum; '2' is not one of [0, 1, '0', '1']
- POST /v1/fields/groups/contacts/contact: params; additionalProperties; Additional properties are not allowed ('class', 'display', 'hint', 'label_class', 'label_render_class', 'layout', 'prefix', 'render_class', 'show_on', 'showlabel', 'suffix' were unexpected)
- POST /v1/fields/groups/contacts/contact: (корень тела); additionalProperties; Additional properties are not allowed ('context', 'default_value', 'group_id', 'label', 'name', 'required', 'type' were unexpected)
- POST /v1/fields/groups/contacts/contact: params.display_readonly; enum; '2' is not one of [0, 1, '0', '1']
- POST /v1/fields/groups/contacts/contact: params; additionalProperties; Additional properties are not allowed ('class', 'display', 'hint', 'label_class', 'label_render_class', 'layout', 'prefix', 'render_class', 'show_on', 'showlabel', 'suffix' were unexpected)
- POST /v1/fields/groups/contacts/contact: (корень тела); additionalProperties; Additional properties are not allowed ('context', 'default_value', 'group_id', 'label', 'name', 'required', 'type' were unexpected)
- POST /v1/fields/groups/content/articles: (корень тела); additionalProperties; Additional properties are not allowed ('checked_out', 'context', 'required' were unexpected)
- POST /v1/fields/groups/users: (корень тела); additionalProperties; Additional properties are not allowed ('checked_out', 'context', 'required' were unexpected)

## Операции вне коллекции

- GET /v1/fields/contacts/mail
- POST /v1/fields/contacts/mail
- GET /v1/fields/contacts/mail/{id}
- PATCH /v1/fields/contacts/mail/{id}
- DELETE /v1/fields/contacts/mail/{id}
- GET /v1/fields/groups/contacts/mail
- POST /v1/fields/groups/contacts/mail
- GET /v1/fields/groups/contacts/mail/{id}
- PATCH /v1/fields/groups/contacts/mail/{id}
- DELETE /v1/fields/groups/contacts/mail/{id}
- GET /v1/fields/groups/contacts/categories
- POST /v1/fields/groups/contacts/categories
- GET /v1/fields/groups/contacts/categories/{id}
- PATCH /v1/fields/groups/contacts/categories/{id}
- DELETE /v1/fields/groups/contacts/categories/{id}
- GET /v1/fields/groups/content/categories
- POST /v1/fields/groups/content/categories
- GET /v1/fields/groups/content/categories/{id}
- PATCH /v1/fields/groups/content/categories/{id}
- DELETE /v1/fields/groups/content/categories/{id}

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
