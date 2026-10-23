# Postman: com_templates, Joomla 6.1.3

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 10. Операций компонента, отсутствующих в коллекции: 0.

## Замечания к телам

- POST /v1/templates/styles/site: params; additionalProperties; Additional properties are not allowed ('sidebarLeftWidth', 'sidebarRightWidth' were unexpected)
- POST /v1/templates/styles/administrator: params; additionalProperties; Additional properties are not allowed ('sidebarLeftWidth', 'sidebarRightWidth' were unexpected)

## Операции вне коллекции

Нет; либо у компонента нет самостоятельных REST-маршрутов.

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
