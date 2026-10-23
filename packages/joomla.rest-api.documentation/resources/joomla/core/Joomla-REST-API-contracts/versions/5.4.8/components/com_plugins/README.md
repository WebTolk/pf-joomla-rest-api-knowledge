# com_plugins REST API — Joomla 5.4.8

Пакет joomla.rest-api.plugins. Версия ядра: 5.4.8.

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
Для снимка 5.4.8 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

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
|GET|/v1/plugins|plugins.displayList|source-derived|
|GET|/v1/plugins/{id}|plugins.displayItem|source-derived|
|PATCH|/v1/plugins/{id}|plugins.edit|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
