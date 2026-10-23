# com_privacy REST API — Joomla 6.2.0

Пакет joomla.rest-api.privacy. Версия ядра: 6.2.0.

Списки/элементы запросов и согласий, а также экспорт требуют core.admin
на com_privacy в API-контроллерах. Удаление consent не имеет REST-маршрута.
Экспорт требует request_type=export и подтверждённый status=1; иначе модель
не возвращает данные, представление вызывает RouteNotFoundException.
Результат формируется privacy-плагинами; REST export не равнозначен файлу
экспорта в админке. Подробности фактической сериализации см. в схеме ответа.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_privacy/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_privacy/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_privacy/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_privacy/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_privacy/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_privacy/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/privacy/requests|requests.displayList|source-derived|
|POST|/v1/privacy/requests|requests.add|source-derived|
|GET|/v1/privacy/requests/{id}|requests.displayItem|source-derived|
|GET|/v1/privacy/requests/export/{id}|requests.export|source-derived|
|GET|/v1/privacy/consents|consents.displayList|source-derived|
|GET|/v1/privacy/consents/{id}|consents.displayItem|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
