# com_installer: заполнение полей, Joomla 6.1.3

GET extensions перечисляет расширения; GET languages — доступные языковые пакеты.
POST languages -> languages.install зарегистрирован, но метод install отсутствует
в API LanguagesController и ApiController этих снимков. Он отмечен как
registered-unimplemented: успешный ответ не выдумывается. Установка через UI
требует соответствующей области задания.
Для снимка 6.1.3 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.


## Инвентарь стандартных форм UI

## administrator/components/com_installer/forms/filter_database.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Extensions: Search in extension name. Prefix with ID: to search for an extension ID.||
|filter.client_id|"string"|нет|""|Location: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter.type|"string"|нет|""|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|filter.folder|"string"|нет|""|Folder: Joomla form field folder; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "name ASC", "name DESC", "client_translated ASC", "client_translated DESC", "type_translated ASC", "type_translated DESC", "folder_translated ASC", "folder_translated DESC", "extension_id ASC", "extension_id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"2"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_installer/forms/filter_discover.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Discovered Extensions: Search in discovered extension name. Prefix with ID: to search for an extension ID.||
|filter.client_id|"string"|нет|""|Location: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter.type|"string"|нет|""|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|filter.folder|"string"|нет|""|Folder: Joomla form field folder; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "name ASC", "name DESC", "client_translated ASC", "client_translated DESC", "type_translated ASC", "type_translated DESC", "folder_translated ASC", "folder_translated DESC", "extension_id ASC", "extension_id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_installer/forms/filter_languages.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Languages: Search in language name and language tag.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "name ASC", "name DESC", "element ASC", "element DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_installer/forms/filter_manage.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Extensions: Search in extension name. Prefix with ID: to search for an extension ID.||
|filter.status|"string"|нет|""|Status: Joomla form field status; input is validated and filtered according to x-joomla-form.||
|filter.client_id|"string"|нет|""|Location: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter.type|"string"|нет|""|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|filter.folder|"string"|нет|""|Folder: Joomla form field folder; input is validated and filtered according to x-joomla-form.||
|filter.package_id|"string"|нет|""|Package: Search for a package extension and extensions included with that package extension.||
|filter.core|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Type: Joomla form field core; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "status ASC", "status DESC", "name ASC", "name DESC", "client_translated ASC", "client_translated DESC", "type_translated ASC", "type_translated DESC", "creationDate ASC", "creationDate DESC", "folder_translated ASC", "folder_translated DESC", "package_id ASC", "package_id DESC", "extension_id ASC", "extension_id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_installer/forms/filter_update.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Extensions with Updates: Search in extension name. Prefix with ID:, UID: or EID: to search for an update ID, update site ID or extension ID.||
|filter.client_id|"string"|нет|""|Location: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter.type|"string"|нет|""|Location: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|filter.folder|"string"|нет|""|Folder: Joomla form field folder; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "u.name ASC", "u.name DESC", "client_translated ASC", "client_translated DESC", "type_translated ASC", "type_translated DESC", "folder_translated ASC", "folder_translated DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_installer/forms/filter_updatesites.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Update Sites: Search in extension name. Prefix with ID: to search for an update site ID.||
|filter.enabled|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Status: Joomla form field enabled; input is validated and filtered according to x-joomla-form.||
|filter.client_id|"string"|нет|""|Location: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter.type|"string"|нет|""|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|filter.folder|"string"|нет|""|Folder: Joomla form field folder; input is validated and filtered according to x-joomla-form.||
|filter.supported|["integer", "string"]|нет|["", 1, -1, 2, "1", "-1", "2"]|Download Key: Joomla form field supported; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "enabled ASC", "enabled DESC", "update_site_name ASC", "update_site_name DESC", "name ASC", "name DESC", "client_translated ASC", "client_translated DESC", "type_translated ASC", "type_translated DESC", "folder_translated ASC", "folder_translated DESC", "update_site_id ASC", "update_site_id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_installer/forms/updatesite.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|update_site_id|"string"|нет|""|update_site_id: Joomla form field update_site_id; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|""|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|location|"string"|нет|""|Location: Joomla form field location; input is validated and filtered according to x-joomla-form.||
|extra_query|"string"|нет|""|Download Key: This extension restricts updates. Typically this means it is an extension with paid downloads. You need to obtain a Download Key from its developer and enter it here to unlock updates for it. You may need to make a payment to the developer to obtain or activate the download key.||
|downloadIdPrefix|"string"|нет|""|downloadIdPrefix: Joomla form field downloadIdPrefix; input is validated and filtered according to x-joomla-form.||
|downloadIdSuffix|"string"|нет|""|downloadIdSuffix: Joomla form field downloadIdSuffix; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_installer/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|cachetimeout|["integer", "string"]|нет|"6"|Updates Caching (in hours): Joomla form field cachetimeout; input is validated and filtered according to x-joomla-form.||
|minimum_stability|["integer", "string"]|нет|[0, 1, 2, 3, 4, "0", "1", "2", "3", "4"]|Minimum Extension Stability: The minimum stability of the extension updates you would like to see. Development is the least stable, Stable is production quality. If an extension doesn't specify a level it is assumed to be Stable.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
