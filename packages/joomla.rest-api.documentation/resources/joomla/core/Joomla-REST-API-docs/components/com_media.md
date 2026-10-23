# com_media REST API — Joomla 6.2.0

Пакет joomla.rest-api.media. Версия ядра: 6.2.0.

path включает адаптер, например local-images:/example.webp; ID адаптера — данные сайта.
GET files/{path}/ с завершающим / возвращает список, без / — элемент.
POST требует path; для файла нужен base64 content, для папки content отсутствует.
POST override по умолчанию false; PATCH override по умолчанию true: для запрета
перезаписи явно передавать false. В PATCH path тела — новый путь, URL path — старый.
Нужен хотя бы path или content. Не передавать multipart, data: URL или сырые байты.
Лимиты размера, допустимые MIME/расширения и возможности определяются настройками
и адаптером. content/url/tempUrl в ответе условны.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_media/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_media/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_media/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_media/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_media/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_media/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/media/adapters|adapters.displayList|source-derived|
|GET|/v1/media/adapters/{id}|adapters.displayItem|source-derived|
|GET|/v1/media/files|media.displayList|source-derived|
|POST|/v1/media/files|media.add|source-derived|
|GET|/v1/media/files/{path}/|media.displayList|source-derived|
|GET|/v1/media/files/{path}|media.displayItem|source-derived|
|PATCH|/v1/media/files/{path}|media.edit|source-derived|
|DELETE|/v1/media/files/{path}|media.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
