# Postman: com_joomlaupdate, Joomla 6.1.3

Сравнивается авторский экспорт, связанный с Documenter. [Источник, метод и ограничения](../../../../common/postman-crosscheck.md).

Сопоставлений с операциями компонента: 0. Операций компонента, отсутствующих в коллекции: 6.

## Замечания к телам

Замечаний по сопоставленным телам нет; это не подтверждает runtime-успех.

## Операции вне коллекции

- GET /v1/joomlaupdate/healthcheck
- GET /v1/joomlaupdate/getUpdate
- POST /v1/joomlaupdate/prepareUpdate
- POST /v1/joomlaupdate/finalizeUpdate
- POST /v1/joomlaupdate/notificationSuccess
- POST /v1/joomlaupdate/notificationFailed

Параметризованный app проверяется для обеих ветвей. Лишние ключи могут игнорироваться сервером. Точный контракт и версия имеют приоритет над примером коллекции.
