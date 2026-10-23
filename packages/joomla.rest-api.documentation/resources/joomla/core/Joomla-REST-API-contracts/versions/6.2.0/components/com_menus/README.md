# com_menus REST API — Joomla 6.2.0

Пакет joomla.rest-api.menus. Версия ядра: 6.2.0.

site/administrator разделяют клиентов. menutype — ключ меню; parent_id — родитель
пункта; type определяет форму параметров. Для component используются link/request
и параметры соответствующего view. GET items/types имеет отдельную структуру.
SEF URL зависит от дерева, языка и router, не только alias.
published/home/browserNav/access/template_style_id — самостоятельные настройки.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

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
|GET|/v1/menus/site|menus.displayList|source-derived|
|GET|/v1/menus/site/{id}|menus.displayItem|source-derived|
|POST|/v1/menus/site|menus.add|source-derived|
|PATCH|/v1/menus/site/{id}|menus.edit|source-derived|
|DELETE|/v1/menus/site/{id}|menus.delete|source-derived|
|GET|/v1/menus/administrator|menus.displayList|source-derived|
|GET|/v1/menus/administrator/{id}|menus.displayItem|source-derived|
|POST|/v1/menus/administrator|menus.add|source-derived|
|PATCH|/v1/menus/administrator/{id}|menus.edit|source-derived|
|DELETE|/v1/menus/administrator/{id}|menus.delete|source-derived|
|GET|/v1/menus/site/items|items.displayList|source-derived|
|GET|/v1/menus/site/items/{id}|items.displayItem|source-derived|
|POST|/v1/menus/site/items|items.add|source-derived|
|PATCH|/v1/menus/site/items/{id}|items.edit|source-derived|
|DELETE|/v1/menus/site/items/{id}|items.delete|source-derived|
|GET|/v1/menus/administrator/items|items.displayList|source-derived|
|GET|/v1/menus/administrator/items/{id}|items.displayItem|source-derived|
|POST|/v1/menus/administrator/items|items.add|source-derived|
|PATCH|/v1/menus/administrator/items/{id}|items.edit|source-derived|
|DELETE|/v1/menus/administrator/items/{id}|items.delete|source-derived|
|GET|/v1/menus/site/items/types|items.getTypes|source-derived|
|GET|/v1/menus/administrator/items/types|items.getTypes|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
