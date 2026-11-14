# com_media REST API — Joomla 6.2.0

Пакет joomla.rest-api.media. Версия ядра: 6.2.0.

path включает адаптер, например local-images:/example.webp; ID адаптера — данные сайта.
GET files/{path} описывает файл и каталог: завершающий / в path выбирает список.
В URL-пути не кодировать разделители / как %2F: Apache может вернуть 404 до Joomla.
Для чтения также доступен GET files?path=...; в query закодированные слеши допустимы.
Без query path список GET files пуст. Размер каталога в ответе может быть пустой строкой.
POST требует path; для файла нужен base64 content, для папки content отсутствует.
POST override по умолчанию false; PATCH override по умолчанию true: для запрета
перезаписи явно передавать false. В PATCH path тела — новый путь, URL path — старый.
Нужен хотя бы path или content. Не передавать multipart, data: URL или сырые байты.
Лимиты размера, допустимые MIME/расширения и возможности определяются настройками
и адаптером. content/url/tempUrl в ответе условны.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Состав

- [openapi.json](openapi.json): схемы запросов/ответов, параметры, коды и примеры.
- [fields.md](fields.md): типы, обязательность, enum/default, правила форм/showon.
- [extension-parameters.json](extension-parameters.json): параметры штатных расширений.
- [examples.json](examples.json): примеры запросов/ответов с указанным происхождением.
- [errors.md](errors.md), [browser-fallback.md](browser-fallback.md).
- [coverage.json](coverage.json), [source-evidence.json](source-evidence.json): покрытие/SHA-256.
- [Общие правила](../../../../common/README.md).

## Маршруты

Таблица ниже сохраняет 8 исходных регистраций маршрутов. В OpenAPI их представляют 7 операций: каталоговый GET объединён с файловым через завершающий / в path.

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

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
