# com_modules REST API — Joomla 6.1.3

Пакет joomla.rest-api.modules. Версия ядра: 6.1.3.

Маршруты site/administrator задают client_id=0/1. module — машинное имя mod_*.
params выбирается по module и client_id, а не только ID экземпляра.
assignment/assigned задают назначение на меню; пустой набор нельзя автоматически
считать «везде». position — позиция установленного шаблона.
GET types возвращает типы, а не экземпляры; ответ имеет отдельную схему.
Схемы стандартных параметров включены; сторонние типы требуют своего пакета.
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
|GET|/v1/modules/types/site|modules.getTypes|source-derived|
|GET|/v1/modules/types/administrator|modules.getTypes|source-derived|
|GET|/v1/modules/site|modules.displayList|source-derived|
|GET|/v1/modules/site/{id}|modules.displayItem|source-derived|
|POST|/v1/modules/site|modules.add|source-derived|
|PATCH|/v1/modules/site/{id}|modules.edit|source-derived|
|DELETE|/v1/modules/site/{id}|modules.delete|source-derived|
|GET|/v1/modules/administrator|modules.displayList|source-derived|
|GET|/v1/modules/administrator/{id}|modules.displayItem|source-derived|
|POST|/v1/modules/administrator|modules.add|source-derived|
|PATCH|/v1/modules/administrator/{id}|modules.edit|source-derived|
|DELETE|/v1/modules/administrator/{id}|modules.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
