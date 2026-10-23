# Postman: com_messages, Joomla 5.4.8

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 5. Операций компонента, отсутствующих в коллекции: 0.

## Замечания к телам

- POST /v1/messages: (корень тела); additionalProperties; Additional properties are not allowed ('state', 'user_id_from' were unexpected)
- PATCH /v1/messages/{id}: (корень тела); additionalProperties; Additional properties are not allowed ('user_id_from' was unexpected)

## Операции вне коллекции

Нет; либо у компонента нет самостоятельных REST-маршрутов.

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
