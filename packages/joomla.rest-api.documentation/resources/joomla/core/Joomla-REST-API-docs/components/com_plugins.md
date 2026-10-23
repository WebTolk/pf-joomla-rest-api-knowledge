# com_plugins REST API — Joomla 6.2.0

Пакет joomla.rest-api.plugins. Версия ядра: 6.2.0.

Штатные операции: GET список, GET запись, PATCH запись. POST/DELETE для установки
и удаления плагинов отсутствуют. id — extension_id; folder+element определяют тип.
PATCH принимает ТОЛЬКО enabled, access, ordering. PluginsController проверяет
сырой плоский JSON; params, folder, element, name и любой другой ключ вызывают
InvalidParameterException, HTTP 400. Обёртка data здесь также не принимается.
Схемы параметров из XML включены для заполнения UI и повторного использования
знаний, но не разрешают запись params через этот REST endpoint.
В JsonapiView params не входит в fieldsToRenderItem: GET не даёт полного снимка
параметров. Их чтение и изменение выполняются в штатной форме UI.
enabled, ordering и access имеют различную семантику.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_plugins/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_plugins/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_plugins/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_plugins/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_plugins/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_plugins/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|GET|/v1/plugins|plugins.displayList|source-derived|
|GET|/v1/plugins/{id}|plugins.displayItem|source-derived|
|PATCH|/v1/plugins/{id}|plugins.edit|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
