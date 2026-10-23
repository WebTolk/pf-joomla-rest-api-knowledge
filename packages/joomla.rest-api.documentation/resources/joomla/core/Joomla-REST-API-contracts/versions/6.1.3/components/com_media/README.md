# com_media REST API — Joomla 6.1.3

Пакет joomla.rest-api.media. Версия ядра: 6.1.3.

path включает адаптер, например local-images:/example.webp; ID адаптера — данные сайта.
GET files/{path}/ с завершающим / возвращает список, без / — элемент.
POST требует path; для файла нужен base64 content, для папки content отсутствует.
POST override по умолчанию false; PATCH override по умолчанию true: для запрета
перезаписи явно передавать false. В PATCH path тела — новый путь, URL path — старый.
Нужен хотя бы path или content. Не передавать multipart, data: URL или сырые байты.
Лимиты размера, допустимые MIME/расширения и возможности определяются настройками
и адаптером. content/url/tempUrl в ответе условны.
Для снимка 6.1.3 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Состав

- [openapi.json](openapi.json): схемы запросов/ответов, параметры, коды и примеры.
- [fields.md](fields.md): типы, обязательность, enum/default, правила форм/showon.
- [extension-parameters.json](extension-parameters.json): параметры штатных расширений.
- [examples.json](examples.json): синтетические request/response fixtures.
- [errors.md](errors.md), [browser-fallback.md](browser-fallback.md).
- [coverage.json](coverage.json), [source-evidence.json](source-evidence.json): покрытие/SHA-256.
- [Общие правила](../../../../common/README.md).

## Маршруты

| Метод | Путь | Действие | Поддержка |
|---|---|---|---|
|GET|/v1/media/adapters|adapters.displayList|source-derived|
|GET|/v1/media/adapters/{id}|adapters.displayItem|source-derived|
|GET|/v1/media/files|media.displayList|source-derived|
|GET|/v1/media/files/{path}/|media.displayList|source-derived|
|GET|/v1/media/files/{path}|media.displayItem|source-derived|
|POST|/v1/media/files|media.add|source-derived|
|PATCH|/v1/media/files/{path}|media.edit|source-derived|
|DELETE|/v1/media/files/{path}|media.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
