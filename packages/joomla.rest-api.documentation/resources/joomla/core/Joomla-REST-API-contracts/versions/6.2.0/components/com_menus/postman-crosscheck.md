# Postman: com_menus, Joomla 6.2.0

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 22. Операций компонента, отсутствующих в коллекции: 0.

## Замечания к телам

- POST /v1/menus/administrator: client_id; enum; 0 is not one of [1, '1']
- POST /v1/menus/administrator/items: (корень тела); additionalProperties; Additional properties are not allowed ('associations', 'publish_down', 'publish_up', 'toggle_modules_assigned', 'toggle_modules_published' were unexpected)

## Операции вне коллекции

Нет; либо у компонента нет самостоятельных REST-маршрутов.

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
