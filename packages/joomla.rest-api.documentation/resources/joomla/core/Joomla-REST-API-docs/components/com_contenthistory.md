# com_contenthistory REST API — Joomla 6.2.0

Пакет joomla.rest-api.contenthistory. Версия ядра: 6.2.0.

GET history использует ID владельца и type_alias/type_id из маршрута.
PATCH history/keep и DELETE history используют числовой сегмент как ID версии;
одно имя id не означает одну сущность у всех действий.
keep переключает keep_forever, а не принимает вымышленное {keep:true}.
version_data — JSON-строка снимка. Перед использованием raw-источника проверить
соответствие текущей версии и изменяемой записи.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contenthistory/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contenthistory/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contenthistory/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contenthistory/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contenthistory/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contenthistory/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/banners/{id}/contenthistory|history.displayList|source-derived|
|DELETE|/v1/banners/{id}/contenthistory|history.delete|source-derived|
|PATCH|/v1/banners/{id}/contenthistory/keep|history.keep|source-derived|
|GET|/v1/contacts/{id}/contenthistory|history.displayList|source-derived|
|DELETE|/v1/contacts/{id}/contenthistory|history.delete|source-derived|
|PATCH|/v1/contacts/{id}/contenthistory/keep|history.keep|source-derived|
|GET|/v1/content/articles/{id}/contenthistory|history.displayList|source-derived|
|DELETE|/v1/content/articles/{id}/contenthistory|history.delete|source-derived|
|PATCH|/v1/content/articles/{id}/contenthistory/keep|history.keep|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
