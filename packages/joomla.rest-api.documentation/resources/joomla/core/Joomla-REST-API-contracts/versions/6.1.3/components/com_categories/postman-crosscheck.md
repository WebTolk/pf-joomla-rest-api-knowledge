# Postman: com_categories, Joomla 6.1.3

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 15. Операций компонента, отсутствующих в коллекции: 5.

## Замечания к телам

- POST /v1/banners/categories: params; additionalProperties; Additional properties are not allowed ('workflow_id' was unexpected)
- POST /v1/contacts/categories: params; additionalProperties; Additional properties are not allowed ('workflow_id' was unexpected)

## Операции вне коллекции

- GET /v1/newsfeeds/categories
- POST /v1/newsfeeds/categories
- GET /v1/newsfeeds/categories/{id}
- PATCH /v1/newsfeeds/categories/{id}
- DELETE /v1/newsfeeds/categories/{id}

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
