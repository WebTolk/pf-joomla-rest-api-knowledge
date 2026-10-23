# Postman: com_languages, Joomla 6.1.3

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 16. Операций компонента, отсутствующих в коллекции: 1.

## Замечания к телам

- POST /v1/languages/content: (корень тела); additionalProperties; Additional properties are not allowed ('metakey', 'ordering' were unexpected)
- PATCH /v1/languages/content/{id}: (корень тела); additionalProperties; Additional properties are not allowed ('metakey' was unexpected)

## Операции вне коллекции

- GET /v1/languages/content/{id}

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
