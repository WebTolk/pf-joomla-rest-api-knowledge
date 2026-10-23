# com_modules REST API — Joomla 6.2.0

Пакет joomla.rest-api.modules. Версия ядра: 6.2.0.

Маршруты site/administrator задают client_id=0/1. module — машинное имя mod_*.
params выбирается по module и client_id, а не только ID экземпляра.
assignment/assigned задают назначение на меню; пустой набор нельзя автоматически
считать «везде». position — позиция установленного шаблона.
GET types возвращает типы, а не экземпляры; ответ имеет отдельную схему.
Схемы стандартных параметров включены; сторонние типы требуют своего пакета.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_modules/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_modules/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_modules/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_modules/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_modules/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_modules/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/modules/types/site|modules.getTypes|source-derived|
|GET|/v1/modules/types/administrator|modules.getTypes|source-derived|
|GET|/v1/modules/site|modules.displayList|source-derived|
|POST|/v1/modules/site|modules.add|source-derived|
|GET|/v1/modules/site/{id}|modules.displayItem|source-derived|
|PATCH|/v1/modules/site/{id}|modules.edit|source-derived|
|DELETE|/v1/modules/site/{id}|modules.delete|source-derived|
|GET|/v1/modules/administrator|modules.displayList|source-derived|
|POST|/v1/modules/administrator|modules.add|source-derived|
|GET|/v1/modules/administrator/{id}|modules.displayItem|source-derived|
|PATCH|/v1/modules/administrator/{id}|modules.edit|source-derived|
|DELETE|/v1/modules/administrator/{id}|modules.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
