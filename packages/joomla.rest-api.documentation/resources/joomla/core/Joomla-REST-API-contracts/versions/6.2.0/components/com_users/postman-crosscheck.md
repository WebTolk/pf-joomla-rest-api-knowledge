# Postman: com_users, Joomla 6.2.0

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 15. Операций компонента, отсутствующих в коллекции: 0.

## Замечания к телам

- POST /v1/users: params; additionalProperties; Additional properties are not allowed ('helpsite' was unexpected)
- POST /v1/users: (корень тела); additionalProperties; Additional properties are not allowed ('id', 'lastResetTime', 'lastvisitDate', 'password2', 'registerDate', 'resetCount' were unexpected)
- POST /v1/users/levels: rules; type; '[1]' is not of type 'array'

## Операции вне коллекции

Нет; либо у компонента нет самостоятельных REST-маршрутов.

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
