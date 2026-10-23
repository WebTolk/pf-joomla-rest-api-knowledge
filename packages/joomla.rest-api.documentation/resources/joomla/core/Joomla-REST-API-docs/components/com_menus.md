# com_menus REST API — Joomla 6.2.0

Пакет joomla.rest-api.menus. Версия ядра: 6.2.0.

site/administrator разделяют клиентов. menutype — ключ меню; parent_id — родитель
пункта; type определяет форму параметров. Для component используются link/request
и параметры соответствующего view. GET items/types имеет отдельную структуру.
SEF URL зависит от дерева, языка и router, не только alias.
published/home/browserNav/access/template_style_id — самостоятельные настройки.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_menus/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_menus/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_menus/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_menus/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_menus/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_menus/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/menus/site|menus.displayList|source-derived|
|POST|/v1/menus/site|menus.add|source-derived|
|GET|/v1/menus/site/{id}|menus.displayItem|source-derived|
|PATCH|/v1/menus/site/{id}|menus.edit|source-derived|
|DELETE|/v1/menus/site/{id}|menus.delete|source-derived|
|GET|/v1/menus/administrator|menus.displayList|source-derived|
|POST|/v1/menus/administrator|menus.add|source-derived|
|GET|/v1/menus/administrator/{id}|menus.displayItem|source-derived|
|PATCH|/v1/menus/administrator/{id}|menus.edit|source-derived|
|DELETE|/v1/menus/administrator/{id}|menus.delete|source-derived|
|GET|/v1/menus/site/items|items.displayList|source-derived|
|POST|/v1/menus/site/items|items.add|source-derived|
|GET|/v1/menus/site/items/{id}|items.displayItem|source-derived|
|PATCH|/v1/menus/site/items/{id}|items.edit|source-derived|
|DELETE|/v1/menus/site/items/{id}|items.delete|source-derived|
|GET|/v1/menus/administrator/items|items.displayList|source-derived|
|POST|/v1/menus/administrator/items|items.add|source-derived|
|GET|/v1/menus/administrator/items/{id}|items.displayItem|source-derived|
|PATCH|/v1/menus/administrator/items/{id}|items.edit|source-derived|
|DELETE|/v1/menus/administrator/items/{id}|items.delete|source-derived|
|GET|/v1/menus/site/items/types|items.getTypes|source-derived|
|GET|/v1/menus/administrator/items/types|items.getTypes|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
