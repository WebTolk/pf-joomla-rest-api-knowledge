# Postman: com_contenthistory, Joomla 6.1.3

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 6. Операций компонента, отсутствующих в коллекции: 6.

## Замечания к телам

- PATCH /v1/banners/{id}/contenthistory/keep: (корень тела); body-not-consumed; Controller action has no documented JSON body; extra properties do not imply saved values.
- PATCH /v1/banners/{id}/contenthistory/keep: (корень тела); body-not-consumed; Controller action has no documented JSON body; extra properties do not imply saved values.

## Операции вне коллекции

- GET /v1/contacts/{id}/contenthistory
- DELETE /v1/contacts/{id}/contenthistory
- PATCH /v1/contacts/{id}/contenthistory/keep
- GET /v1/content/articles/{id}/contenthistory
- DELETE /v1/content/articles/{id}/contenthistory
- PATCH /v1/content/articles/{id}/contenthistory/keep

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
