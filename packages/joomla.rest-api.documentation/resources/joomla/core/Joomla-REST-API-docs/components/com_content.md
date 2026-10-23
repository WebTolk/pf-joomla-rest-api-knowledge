# com_content REST API — Joomla 6.2.0

Пакет joomla.rest-api.content. Версия ядра: 6.2.0.

catid — ID категории записи; category в ответе — отношение, не ключ записи catid.
Для создания черновика явно передавать state=0: default XML равен 1.
Для исходного текста PATCH использовать introtext/fulltext. articletext — редакторское
поле с readmore; на PATCH оно может быть перекрыто догруженными колонками.
GET text обработан контентными плагинами и не является надёжным raw HTML.
Использовать сохранённый исходник, актуальную contenthistory.version_data либо
разрешённую форму UI. images/urls/metadata/attribs — вложенные структуры.
created_by и metadata.author различаются; API-пользователь не обязательно автор.
Доступность state зависит от workflow и ACL. schemaorg и languageAssociations
условны: зависят от плагинов и многоязычности.
В 6.2.0 list/item содержат introtext и fulltext. text помечен deprecated с удалением в 8.0; для нового клиента выбирать отдельные поля. onContentPrepare всё ещё может изменять объект статьи: это не гарантия неизменённых БД-байтов.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_content/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_content/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_content/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_content/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_content/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_content/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/content/articles|articles.displayList|source-derived|
|POST|/v1/content/articles|articles.add|source-derived|
|GET|/v1/content/articles/{id}|articles.displayItem|source-derived|
|PATCH|/v1/content/articles/{id}|articles.edit|source-derived|
|DELETE|/v1/content/articles/{id}|articles.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
