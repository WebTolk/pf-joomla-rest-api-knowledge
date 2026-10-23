# Postman: com_modules, Joomla 6.1.3

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 12. Операций компонента, отсутствующих в коллекции: 0.

## Замечания к телам

- POST /v1/modules/administrator: assigned; type; ['101', '105'] is not of type 'string'
- POST /v1/modules/administrator: client_id; enum; '0' is not one of [1, '1']
- PATCH /v1/modules/administrator/{id}: client_id; enum; '0' is not one of [1, '1']

## Операции вне коллекции

Нет; либо у компонента нет самостоятельных REST-маршрутов.

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
