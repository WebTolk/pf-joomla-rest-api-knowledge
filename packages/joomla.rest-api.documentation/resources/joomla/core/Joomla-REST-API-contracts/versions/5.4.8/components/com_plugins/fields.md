# com_plugins: заполнение полей, Joomla 5.4.8

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

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST PATCH /v1/plugins/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|enabled|["integer", "string"]|нет|[1, 0, "1", "0"]|Status: Joomla form field enabled; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||

## Инвентарь стандартных форм UI

## administrator/components/com_plugins/forms/filter_plugins.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Plugins: Search in plugin name. Prefix with ID: to search for a plugin ID.||
|filter.enabled|"string"|нет|""|Status: Joomla form field enabled; input is validated and filtered according to x-joomla-form.||
|filter.folder|"string"|нет|""|Type: Joomla form field folder; input is validated and filtered according to x-joomla-form.||
|filter.element|"string"|нет|""|Element: Joomla form field element; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "ordering ASC", "ordering DESC", "enabled ASC", "enabled DESC", "name ASC", "name DESC", "folder ASC", "folder DESC", "element ASC", "element DESC", "access ASC", "access DESC", "extension_id ASC", "extension_id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_plugins/forms/plugin.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|extension_id|["integer", "string"]|нет|"0"|ID: Joomla form field extension_id; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Plugin Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|enabled|["integer", "string"]|нет|[1, 0, "1", "0"]|Status: Joomla form field enabled; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|folder|"string"|нет|""|Plugin Type: Joomla form field folder; input is validated and filtered according to x-joomla-form.||
|element|"string"|нет|""|Plugin File: Joomla form field element; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_plugins/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
