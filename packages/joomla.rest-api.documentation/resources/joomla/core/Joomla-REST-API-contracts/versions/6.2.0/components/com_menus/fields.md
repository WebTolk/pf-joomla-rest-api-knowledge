# com_menus: заполнение полей, Joomla 6.2.0

site/administrator разделяют клиентов. menutype — ключ меню; parent_id — родитель
пункта; type определяет форму параметров. Для component используются link/request
и параметры соответствующего view. GET items/types имеет отдельную структуру.
SEF URL зависит от дерева, языка и router, не только alias.
published/home/browserNav/access/template_style_id — самостоятельные настройки.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/menus/site

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|menutype|"string"|да|""|Unique Name: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|client_id|["integer", "string"]|нет|[0, "0"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
|preset|"string"|нет|""|Import a preset: Select a preset if you want to populate this menu with the menu items in that preset. Otherwise leave this empty.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/menus/site/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|menutype|"string"|нет|""|Unique Name: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|client_id|["integer", "string"]|нет|[0, "0"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
|preset|"string"|нет|""|Import a preset: Select a preset if you want to populate this menu with the menu items in that preset. Otherwise leave this empty.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/menus/administrator

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|menutype|"string"|да|""|Unique Name: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|client_id|["integer", "string"]|нет|[1, "1"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
|preset|"string"|нет|""|Import a preset: Select a preset if you want to populate this menu with the menu items in that preset. Otherwise leave this empty.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/menus/administrator/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|menutype|"string"|нет|""|Unique Name: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|client_id|["integer", "string"]|нет|[1, "1"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
|preset|"string"|нет|""|Import a preset: Select a preset if you want to populate this menu with the menu items in that preset. Otherwise leave this empty.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/menus/site/items

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|link|"string"|нет|""|link: Menu target URL; controller preprocesses it before form loading.||
|menutype|"string"|да|""|Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|""|Menu Item Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|home:0|
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|home:0|
|parent_id|["integer", "string"]|нет|"1"|Parent Item: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|menuordering|["integer", "string"]|нет|""|Ordering: Joomla form field menuordering; input is validated and filtered according to x-joomla-form.||
|component_id|["integer", "string"]|нет|""|component_id: Joomla form field component_id; input is validated and filtered according to x-joomla-form.||
|browserNav|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Target Window: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|template_style_id|["integer", "string"]|нет|""|Template Style: Joomla form field template_style_id; input is validated and filtered according to x-joomla-form.|type!:alias[OR]params.alias_redirect:0|
|home|["integer", "string"]|нет|[0, 1, "0", "1"]|Default Page: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|toggle_modules_assigned|["integer", "string"]|нет|[0, 1, "0", "1"]|Unassigned Modules: Joomla form field toggle_modules_assigned; input is validated and filtered according to x-joomla-form.||
|toggle_modules_published|["integer", "string"]|нет|[0, 1, "0", "1"]|Unpublished Modules: Joomla form field toggle_modules_published; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|request|"object"|нет|""|request: ||
|associations|"object"|нет|""|associations: Language tag -> menu item ID; only when associations are enabled.||
|client_id|["integer", "string"]|нет|[0, "0"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
## REST PATCH /v1/menus/site/items/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|link|"string"|нет|""|link: Menu target URL; controller preprocesses it before form loading.||
|menutype|"string"|нет|""|Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|""|Menu Item Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|home:0|
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|home:0|
|parent_id|["integer", "string"]|нет|"1"|Parent Item: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|menuordering|["integer", "string"]|нет|""|Ordering: Joomla form field menuordering; input is validated and filtered according to x-joomla-form.||
|component_id|["integer", "string"]|нет|""|component_id: Joomla form field component_id; input is validated and filtered according to x-joomla-form.||
|browserNav|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Target Window: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|template_style_id|["integer", "string"]|нет|""|Template Style: Joomla form field template_style_id; input is validated and filtered according to x-joomla-form.|type!:alias[OR]params.alias_redirect:0|
|home|["integer", "string"]|нет|[0, 1, "0", "1"]|Default Page: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|toggle_modules_assigned|["integer", "string"]|нет|[0, 1, "0", "1"]|Unassigned Modules: Joomla form field toggle_modules_assigned; input is validated and filtered according to x-joomla-form.||
|toggle_modules_published|["integer", "string"]|нет|[0, 1, "0", "1"]|Unpublished Modules: Joomla form field toggle_modules_published; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|request|"object"|нет|""|request: ||
|associations|"object"|нет|""|associations: Language tag -> menu item ID; only when associations are enabled.||
|client_id|["integer", "string"]|нет|[0, "0"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
## REST POST /v1/menus/administrator/items

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|link|"string"|нет|""|link: Menu target URL; controller preprocesses it before form loading.||
|menutype|"string"|да|""|Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|""|Menu Item Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|parent_id|["integer", "string"]|нет|"1"|Parent Item: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|menuordering|["integer", "string"]|нет|""|Ordering: Joomla form field menuordering; input is validated and filtered according to x-joomla-form.||
|component_id|["integer", "string"]|нет|""|component_id: Joomla form field component_id; input is validated and filtered according to x-joomla-form.||
|browserNav|"string"|нет|"0"|browserNav: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|home|"string"|нет|"0"|home: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|access|"string"|нет|"0"|access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|template_style_id|"string"|нет|"0"|template_style_id: Joomla form field template_style_id; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|"*"|language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|request|"object"|нет|""|request: ||
|client_id|["integer", "string"]|нет|[1, "1"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
## REST PATCH /v1/menus/administrator/items/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|link|"string"|нет|""|link: Menu target URL; controller preprocesses it before form loading.||
|menutype|"string"|нет|""|Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|""|Menu Item Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|parent_id|["integer", "string"]|нет|"1"|Parent Item: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|menuordering|["integer", "string"]|нет|""|Ordering: Joomla form field menuordering; input is validated and filtered according to x-joomla-form.||
|component_id|["integer", "string"]|нет|""|component_id: Joomla form field component_id; input is validated and filtered according to x-joomla-form.||
|browserNav|"string"|нет|"0"|browserNav: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|home|"string"|нет|"0"|home: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|access|"string"|нет|"0"|access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|template_style_id|"string"|нет|"0"|template_style_id: Joomla form field template_style_id; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|"*"|language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|request|"object"|нет|""|request: ||
|client_id|["integer", "string"]|нет|[1, "1"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||

## Инвентарь стандартных форм UI

## administrator/components/com_menus/forms/filter_items.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|client_id|["integer", "string"]|нет|[0, 1, "0", "1"]|Select Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|menutype|"string"|нет|""|Select Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Menu Items: Search in title, alias and notes. Prefix with ID: to search for a menu item ID.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|filter.parent_id|"string"|нет|""|Parent Menu Item: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|filter.componentName|"string"|нет|""|Component: Joomla form field componentName; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.lft ASC", "a.lft DESC", "a.published ASC", "a.published DESC", "a.title ASC", "a.title DESC", "menutype_title ASC", "menutype_title DESC", "a.home ASC", "a.home DESC", "a.access ASC", "a.access DESC", "association ASC", "association DESC", "language ASC", "language DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/filter_itemsadmin.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|client_id|["integer", "string"]|нет|[0, 1, "0", "1"]|Select Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|menutype|"string"|нет|""|Select Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Menu Items: Search in title, alias and notes. Prefix with ID: to search for a menu item ID.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|filter.parent_id|"string"|нет|""|Parent Menu Item: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.lft ASC", "a.lft DESC", "a.published ASC", "a.published DESC", "a.title ASC", "a.title DESC", "menutype_title ASC", "menutype_title DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/filter_menus.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|client_id|["integer", "string"]|нет|[0, 1, "0", "1"]|Select Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Menus: Search in title and menu type.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.title ASC", "a.title DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"5"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/item.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|link|"string"|нет|""|Link: Joomla form field link; input is validated and filtered according to x-joomla-form.||
|menutype|"string"|да|""|Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|""|Menu Item Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|home:0|
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|home:0|
|parent_id|["integer", "string"]|нет|"1"|Parent Item: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|menuordering|["integer", "string"]|нет|""|Ordering: Joomla form field menuordering; input is validated and filtered according to x-joomla-form.||
|component_id|["integer", "string"]|нет|""|component_id: Joomla form field component_id; input is validated and filtered according to x-joomla-form.||
|browserNav|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Target Window: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|template_style_id|["integer", "string"]|нет|""|Template Style: Joomla form field template_style_id; input is validated and filtered according to x-joomla-form.|type!:alias[OR]params.alias_redirect:0|
|home|["integer", "string"]|нет|[0, 1, "0", "1"]|Default Page: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|toggle_modules_assigned|["integer", "string"]|нет|[0, 1, "0", "1"]|Unassigned Modules: Joomla form field toggle_modules_assigned; input is validated and filtered according to x-joomla-form.||
|toggle_modules_published|["integer", "string"]|нет|[0, 1, "0", "1"]|Unpublished Modules: Joomla form field toggle_modules_published; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
## administrator/components/com_menus/forms/item_alias.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.aliasoptions|["integer", "string"]|да|""|Menu Item: Joomla form field aliasoptions; input is validated and filtered according to x-joomla-form.||
|params.alias_redirect|["integer", "string"]|нет|[0, 1, "0", "1"]|Use Redirection: Joomla form field alias_redirect; input is validated and filtered according to x-joomla-form.||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu-anchor_css|"string"|нет|""|Link Class: Joomla form field menu-anchor_css; input is validated and filtered according to x-joomla-form.||
|params.menu_icon_css|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/item_component.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu-anchor_css|"string"|нет|""|Link Class: Joomla form field menu-anchor_css; input is validated and filtered according to x-joomla-form.||
|params.menu_icon_css|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
|params.page_title|"string"|нет|""|Browser Page Title: Joomla form field page_title; input is validated and filtered according to x-joomla-form.||
|params.show_page_heading|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Show Page Heading: Joomla form field show_page_heading; input is validated and filtered according to x-joomla-form.||
|params.page_heading|"string"|нет|""|Page Heading: Joomla form field page_heading; input is validated and filtered according to x-joomla-form.||
|params.pageclass_sfx|"string"|нет|""|Page Class: Joomla form field pageclass_sfx; input is validated and filtered according to x-joomla-form.||
|params.menu-meta_description|"string"|нет|""|Meta Description: Joomla form field menu-meta_description; input is validated and filtered according to x-joomla-form.||
|params.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/item_heading.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu-anchor_css|"string"|нет|""|Link Class: Joomla form field menu-anchor_css; input is validated and filtered according to x-joomla-form.||
|params.menu_icon_css|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/item_separator.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.menu-anchor_css|"string"|нет|""|Link Class: Joomla form field menu-anchor_css; input is validated and filtered according to x-joomla-form.||
|params.menu_icon_css|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/item_url.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu-anchor_css|"string"|нет|""|Link Class: Joomla form field menu-anchor_css; input is validated and filtered according to x-joomla-form.||
|params.menu_icon_css|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu-anchor_rel|"string"|нет|["", "alternate", "author", "bookmark", "external", "help", "license", "me", "next", "nofollow", "noopener", "noreferrer", "prefetch", "prev", "search", "sponsored", "tag", "ugc"]|Link Rel Attribute: Joomla form field menu-anchor_rel; input is validated and filtered according to x-joomla-form.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/itemadmin.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|link|"string"|нет|""|Link: Joomla form field link; input is validated and filtered according to x-joomla-form.||
|menutype|"string"|да|""|Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|""|Menu Item Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|parent_id|["integer", "string"]|нет|"1"|Parent Item: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|menuordering|["integer", "string"]|нет|""|Ordering: Joomla form field menuordering; input is validated and filtered according to x-joomla-form.||
|component_id|["integer", "string"]|нет|""|component_id: Joomla form field component_id; input is validated and filtered according to x-joomla-form.||
|browserNav|["integer", "string"]|нет|[0, 1, "0", "1"]|Target Window: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|home|"string"|нет|"0"|home: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|access|"string"|нет|"0"|access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|template_style_id|"string"|нет|"0"|template_style_id: Joomla form field template_style_id; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|"*"|language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
## administrator/components/com_menus/forms/itemadmin_alias.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.aliasoptions|["integer", "string"]|да|""|Menu Item: Joomla form field aliasoptions; input is validated and filtered according to x-joomla-form.||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu_icon|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/itemadmin_component.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu_icon|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/itemadmin_container.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|link|"string"|нет|""|link: Joomla form field link; input is validated and filtered according to x-joomla-form.||
|browserNav|"string"|нет|"0"|browserNav: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu_icon|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
|params.hideitems|"array"|нет|""|Show or Hide Menu Items: Select the menu items that should or should not be shown in this container. If there are no items to show, then this container will also be hidden.<br>Please note that when you install a new component it will be displayed by default until you come back here and hide it too.||
## administrator/components/com_menus/forms/itemadmin_heading.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|link|"string"|нет|""|link: Joomla form field link; input is validated and filtered according to x-joomla-form.||
|browserNav|"string"|нет|"0"|browserNav: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu_icon|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
|params.dashboard|"string"|нет|""|Dashboard: If an identifier is provided, a dashboard is created for this menu item.||
## administrator/components/com_menus/forms/itemadmin_separator.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|link|"string"|нет|""|link: Joomla form field link; input is validated and filtered according to x-joomla-form.||
|browserNav|"string"|нет|"0"|browserNav: Joomla form field browserNav; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.text_separator|["integer", "string"]|нет|[0, 1, "0", "1"]|Display: Joomla form field text_separator; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/itemadmin_url.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.menu-anchor_title|"string"|нет|""|Link Title Attribute: Joomla form field menu-anchor_title; input is validated and filtered according to x-joomla-form.||
|params.menu-anchor_rel|"string"|нет|["", "alternate", "author", "bookmark", "external", "help", "license", "me", "next", "nofollow", "noopener", "noreferrer", "prefetch", "prev", "search", "sponsored", "tag", "ugc"]|Link Rel Attribute: Joomla form field menu-anchor_rel; input is validated and filtered according to x-joomla-form.||
|params.menu_icon|"string"|нет|""|Link Icon Class: If an icon class is entered, it takes precedence over the link image.||
|params.menu_image|"string"|нет|""|Link Image: Joomla form field menu_image; input is validated and filtered according to x-joomla-form.||
|params.menu_image_css|"string"|нет|""|Image Class: Joomla form field menu_image_css; input is validated and filtered according to x-joomla-form.||
|params.menu_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Menu Item Title: Joomla form field menu_text; input is validated and filtered according to x-joomla-form.||
|params.menu_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Display in Menu: Joomla form field menu_show; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/forms/menu.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|id: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|menutype|"string"|да|""|Unique Name: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|client_id|["integer", "string"]|нет|""|client_id: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|preset|"string"|нет|""|Import a preset: Select a preset if you want to populate this menu with the menu items in that preset. Otherwise leave this empty.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_menus/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|page_title|"string"|нет|""|Browser Page Title: Joomla form field page_title; input is validated and filtered according to x-joomla-form.||
|show_page_heading|["integer", "string"]|нет|[0, 1, "0", "1"]|Show Page Heading: Joomla form field show_page_heading; input is validated and filtered according to x-joomla-form.||
|page_heading|"string"|нет|""|Page Heading: Joomla form field page_heading; input is validated and filtered according to x-joomla-form.|show_page_heading:1|
|pageclass_sfx|"string"|нет|""|Page Class: Joomla form field pageclass_sfx; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_config/tmpl/config/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.controller|"string"|нет|""|controller: Joomla form field controller; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_config/tmpl/templates/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.controller|"string"|нет|""|controller: Joomla form field controller; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_contact/tmpl/categories/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Select the Top Level Category: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_base_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Top Level Category Description: Joomla form field show_base_description; input is validated and filtered according to x-joomla-form.||
|params.categories_description|"string"|нет|""|Alternative Description: Joomla form field categories_description; input is validated and filtered according to x-joomla-form.||
|params.maxLevelcat|["integer", "string"]|нет|["", -1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevelcat; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories_cat; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc_cat; input is validated and filtered according to x-joomla-form.||
|params.show_cat_items_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Contacts in Category: Joomla form field show_cat_items_cat; input is validated and filtered according to x-joomla-form.||
|params.show_category_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|params.show_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|params.show_description_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|params.maxLevel|["integer", "string"]|нет|["", -1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.||
|params.show_no_contacts|["integer", "string"]|нет|["", 0, 1, "0", "1"]|No Contacts Message: Joomla form field show_no_contacts; input is validated and filtered according to x-joomla-form.||
|params.show_category_heading_title_text|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Heading: Joomla form field show_category_heading_title_text; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.||
|params.show_cat_items|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Contacts in Category: Joomla form field show_cat_items; input is validated and filtered according to x-joomla-form.||
|params.filter_field|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.show_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|params.show_position_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Position: Joomla form field show_position_headings; input is validated and filtered according to x-joomla-form.||
|params.show_email_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Email: Joomla form field show_email_headings; input is validated and filtered according to x-joomla-form.||
|params.show_telephone_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Phone: Joomla form field show_telephone_headings; input is validated and filtered according to x-joomla-form.||
|params.show_mobile_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Mobile: Joomla form field show_mobile_headings; input is validated and filtered according to x-joomla-form.||
|params.show_fax_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Fax: Joomla form field show_fax_headings; input is validated and filtered according to x-joomla-form.||
|params.show_suburb_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|City or Suburb: Joomla form field show_suburb_headings; input is validated and filtered according to x-joomla-form.||
|params.show_state_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|State or County: Joomla form field show_state_headings; input is validated and filtered according to x-joomla-form.||
|params.show_country_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Country: Joomla form field show_country_headings; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.show_contact_category|"string"|нет|["", "hide", "show_no_link", "show_with_link"]|Contact Category: Joomla form field show_contact_category; input is validated and filtered according to x-joomla-form.||
|params.show_contact_list|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Select List: Joomla form field show_contact_list; input is validated and filtered according to x-joomla-form.||
|params.show_name|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Name: Joomla form field show_name; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_info|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Information: Joomla form field show_info; input is validated and filtered according to x-joomla-form.||
|params.show_position|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact's Position: Joomla form field show_position; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_email|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Email: Joomla form field show_email; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_street_address|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Street Address: Joomla form field show_street_address; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_suburb|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_TOWN-SUBURB_LABEL: Joomla form field show_suburb; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_state|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_STATE-COUNTY_LABEL: Joomla form field show_state; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_postcode|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_POST-ZIP_CODE_LABEL: Joomla form field show_postcode; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_country|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Country: Joomla form field show_country; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_telephone|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Telephone: Joomla form field show_telephone; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_mobile|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Mobile Phone: Joomla form field show_mobile; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_fax|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Fax: Joomla form field show_fax; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_webpage|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Webpage: Joomla form field show_webpage; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Image: Joomla form field show_image; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.allow_vcard|["integer", "string"]|нет|["", 0, 1, "0", "1"]|vCard: Joomla form field allow_vcard; input is validated and filtered according to x-joomla-form.||
|params.show_misc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Miscellaneous Information: Joomla form field show_misc; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.articles_display_num|"string"|нет|["", "use_contact", "5", "10", "15", "20", "25", "30", "50", "75", "100", "150", "200", "250", "300", "0"]|# Articles to List: Joomla form field articles_display_num; input is validated and filtered according to x-joomla-form.||
|params.show_links|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Links: Joomla form field show_links; input is validated and filtered according to x-joomla-form.||
|params.linka_name|"string"|нет|""|Link A Label: Joomla form field linka_name; input is validated and filtered according to x-joomla-form.||
|params.linkb_name|"string"|нет|""|Link B Label: Joomla form field linkb_name; input is validated and filtered according to x-joomla-form.||
|params.linkc_name|"string"|нет|""|Link C Label: Joomla form field linkc_name; input is validated and filtered according to x-joomla-form.||
|params.linkd_name|"string"|нет|""|Link D Label: Joomla form field linkd_name; input is validated and filtered according to x-joomla-form.||
|params.linke_name|"string"|нет|""|Link E Label: Joomla form field linke_name; input is validated and filtered according to x-joomla-form.||
|params.show_email_form|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Form: Joomla form field show_email_form; input is validated and filtered according to x-joomla-form.||
|params.show_email_copy|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Send Copy to Submitter: Joomla form field show_email_copy; input is validated and filtered according to x-joomla-form.||
|params.validate_session|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Session Check: Joomla form field validate_session; input is validated and filtered according to x-joomla-form.||
|params.custom_reply|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Custom Reply: Stops Joomla from sending the email, allowing for Plugins to handle integration with other systems.||
|params.redirect|"string"|нет|""|Contact Redirect URL: Joomla form field redirect; input is validated and filtered according to x-joomla-form.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_contact/tmpl/category/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Select a Category: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_category_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|params.show_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|params.show_description_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|params.maxLevel|["integer", "string"]|нет|["", -1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.||
|params.show_no_contacts|["integer", "string"]|нет|["", 0, 1, "0", "1"]|No Contacts Message: Joomla form field show_no_contacts; input is validated and filtered according to x-joomla-form.||
|params.show_category_heading_title_text|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Heading: Joomla form field show_category_heading_title_text; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Image: Joomla form field show_subcat_image; input is validated and filtered according to x-joomla-form.||
|params.show_cat_items|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Contacts in Category: Joomla form field show_cat_items; input is validated and filtered according to x-joomla-form.||
|params.filter_field|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.show_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|params.show_image_heading|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Image: Joomla form field show_image_heading; input is validated and filtered according to x-joomla-form.||
|params.show_position_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Position: Joomla form field show_position_headings; input is validated and filtered according to x-joomla-form.||
|params.show_email_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Email: Joomla form field show_email_headings; input is validated and filtered according to x-joomla-form.||
|params.show_telephone_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Phone: Joomla form field show_telephone_headings; input is validated and filtered according to x-joomla-form.||
|params.show_mobile_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Mobile: Joomla form field show_mobile_headings; input is validated and filtered according to x-joomla-form.||
|params.show_fax_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Fax: Joomla form field show_fax_headings; input is validated and filtered according to x-joomla-form.||
|params.show_suburb_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|City or Suburb: Joomla form field show_suburb_headings; input is validated and filtered according to x-joomla-form.||
|params.show_state_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|State or County: Joomla form field show_state_headings; input is validated and filtered according to x-joomla-form.||
|params.show_country_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Country: Joomla form field show_country_headings; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.contacts_display_num|["integer", "string"]|нет|["", 5, 10, 15, 20, 25, 30, 50, 100, 0, "5", "10", "15", "20", "25", "30", "50", "100", "0"]|# Contacts to List: Joomla form field contacts_display_num; input is validated and filtered according to x-joomla-form.||
|params.initial_sort|"string"|нет|["", "name", "sortname", "ordering", "featuredordering"]|Sort By: Joomla form field initial_sort; input is validated and filtered according to x-joomla-form.||
|params.contact_layout|"string"|нет|""|Choose a Layout: Joomla form field contact_layout; input is validated and filtered according to x-joomla-form.||
|params.show_contact_category|"string"|нет|["", "hide", "show_no_link", "show_with_link"]|Contact Category: Joomla form field show_contact_category; input is validated and filtered according to x-joomla-form.||
|params.show_contact_list|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Select List: Joomla form field show_contact_list; input is validated and filtered according to x-joomla-form.||
|params.show_name|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Name: Joomla form field show_name; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_info|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Information: Joomla form field show_info; input is validated and filtered according to x-joomla-form.||
|params.show_position|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact's Position: Joomla form field show_position; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_email|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Email: Joomla form field show_email; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_street_address|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Street Address: Joomla form field show_street_address; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_suburb|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_TOWN-SUBURB_LABEL: Joomla form field show_suburb; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_state|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_STATE-COUNTY_LABEL: Joomla form field show_state; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_postcode|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_POST-ZIP_CODE_LABEL: Joomla form field show_postcode; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_country|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Country: Joomla form field show_country; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_telephone|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Telephone: Joomla form field show_telephone; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_mobile|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Mobile Phone: Joomla form field show_mobile; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_fax|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Fax: Joomla form field show_fax; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_webpage|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Webpage: Joomla form field show_webpage; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Image: Joomla form field show_image; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.allow_vcard|["integer", "string"]|нет|["", 0, 1, "0", "1"]|vCard: Joomla form field allow_vcard; input is validated and filtered according to x-joomla-form.||
|params.show_misc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Miscellaneous Information: Joomla form field show_misc; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.articles_display_num|"string"|нет|["", "use_contact", "5", "10", "15", "20", "25", "30", "50", "75", "100", "150", "200", "250", "300", "0"]|# Articles to List: Joomla form field articles_display_num; input is validated and filtered according to x-joomla-form.||
|params.show_links|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Links: Joomla form field show_links; input is validated and filtered according to x-joomla-form.||
|params.show_user_custom_fields|"array"|нет|""|User Custom Field Groups: Joomla form field show_user_custom_fields; input is validated and filtered according to x-joomla-form.||
|params.linka_name|"string"|нет|""|Link A Label: Joomla form field linka_name; input is validated and filtered according to x-joomla-form.||
|params.linkb_name|"string"|нет|""|Link B Label: Joomla form field linkb_name; input is validated and filtered according to x-joomla-form.||
|params.linkc_name|"string"|нет|""|Link C Label: Joomla form field linkc_name; input is validated and filtered according to x-joomla-form.||
|params.linkd_name|"string"|нет|""|Link D Label: Joomla form field linkd_name; input is validated and filtered according to x-joomla-form.||
|params.linke_name|"string"|нет|""|Link E Label: Joomla form field linke_name; input is validated and filtered according to x-joomla-form.||
|params.show_email_form|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Form: Joomla form field show_email_form; input is validated and filtered according to x-joomla-form.||
|params.show_email_copy|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Send Copy to Submitter: Joomla form field show_email_copy; input is validated and filtered according to x-joomla-form.||
|params.validate_session|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Session Check: Joomla form field validate_session; input is validated and filtered according to x-joomla-form.||
|params.custom_reply|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Custom Reply: Stops Joomla from sending the email, allowing for Plugins to handle integration with other systems.||
|params.redirect|"string"|нет|""|Contact Redirect URL: Joomla form field redirect; input is validated and filtered according to x-joomla-form.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_contact/tmpl/contact/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Select Contact: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_contact_category|"string"|нет|["", "hide", "show_no_link", "show_with_link"]|Contact Category: Joomla form field show_contact_category; input is validated and filtered according to x-joomla-form.||
|params.show_contact_list|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Select List: Joomla form field show_contact_list; input is validated and filtered according to x-joomla-form.||
|params.show_name|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Name: Joomla form field show_name; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_info|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Information: Joomla form field show_info; input is validated and filtered according to x-joomla-form.||
|params.show_position|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact's Position: Joomla form field show_position; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_email|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Email: Joomla form field show_email; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.add_mailto_link|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Add Mailto: Link: Joomla form field add_mailto_link; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_street_address|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Street Address: Joomla form field show_street_address; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_suburb|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_TOWN-SUBURB_LABEL: Joomla form field show_suburb; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_state|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_STATE-COUNTY_LABEL: Joomla form field show_state; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_postcode|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_POST-ZIP_CODE_LABEL: Joomla form field show_postcode; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_country|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Country: Joomla form field show_country; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_telephone|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Telephone: Joomla form field show_telephone; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_mobile|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Mobile Phone: Joomla form field show_mobile; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_fax|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Fax: Joomla form field show_fax; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_webpage|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Webpage: Joomla form field show_webpage; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Image: Joomla form field show_image; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.allow_vcard|["integer", "string"]|нет|["", 0, 1, "0", "1"]|vCard: Joomla form field allow_vcard; input is validated and filtered according to x-joomla-form.||
|params.show_misc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Miscellaneous Information: Joomla form field show_misc; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.articles_display_num|"string"|нет|["", "use_contact", "5", "10", "15", "20", "25", "30", "50", "75", "100", "150", "200", "250", "300", "0"]|# Articles to List: Joomla form field articles_display_num; input is validated and filtered according to x-joomla-form.||
|params.show_profile|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Profile: Joomla form field show_profile; input is validated and filtered according to x-joomla-form.||
|params.show_user_custom_fields|"array"|нет|""|User Custom Field Groups: Joomla form field show_user_custom_fields; input is validated and filtered according to x-joomla-form.||
|params.show_links|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Links: Joomla form field show_links; input is validated and filtered according to x-joomla-form.||
|params.linka_name|"string"|нет|""|Link A Label: Joomla form field linka_name; input is validated and filtered according to x-joomla-form.||
|params.linkb_name|"string"|нет|""|Link B Label: Joomla form field linkb_name; input is validated and filtered according to x-joomla-form.||
|params.linkc_name|"string"|нет|""|Link C Label: Joomla form field linkc_name; input is validated and filtered according to x-joomla-form.||
|params.linkd_name|"string"|нет|""|Link D Label: Joomla form field linkd_name; input is validated and filtered according to x-joomla-form.||
|params.linke_name|"string"|нет|""|Link E Label: Joomla form field linke_name; input is validated and filtered according to x-joomla-form.||
|params.show_email_form|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Form: Joomla form field show_email_form; input is validated and filtered according to x-joomla-form.||
|params.show_email_copy|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Send Copy to Submitter: Joomla form field show_email_copy; input is validated and filtered according to x-joomla-form.||
|params.validate_session|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Session Check: Joomla form field validate_session; input is validated and filtered according to x-joomla-form.||
|params.custom_reply|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Custom Reply: Stops Joomla from sending the email, allowing for Plugins to handle integration with other systems.||
|params.redirect|"string"|нет|""|Contact Redirect URL: Joomla form field redirect; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_contact/tmpl/featured/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.filter_field|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.show_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|params.show_position_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Position: Joomla form field show_position_headings; input is validated and filtered according to x-joomla-form.||
|params.show_email_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Email: Joomla form field show_email_headings; input is validated and filtered according to x-joomla-form.||
|params.show_telephone_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Phone: Joomla form field show_telephone_headings; input is validated and filtered according to x-joomla-form.||
|params.show_mobile_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Mobile: Joomla form field show_mobile_headings; input is validated and filtered according to x-joomla-form.||
|params.show_fax_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Fax: Joomla form field show_fax_headings; input is validated and filtered according to x-joomla-form.||
|params.show_suburb_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|City or Suburb: Joomla form field show_suburb_headings; input is validated and filtered according to x-joomla-form.||
|params.show_state_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|State or County: Joomla form field show_state_headings; input is validated and filtered according to x-joomla-form.||
|params.show_country_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Country: Joomla form field show_country_headings; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_info|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Information: Joomla form field show_info; input is validated and filtered according to x-joomla-form.||
|params.show_name|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Name: Joomla form field show_name; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_position|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact's Position: Joomla form field show_position; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_email|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Email: Joomla form field show_email; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_street_address|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Street Address: Joomla form field show_street_address; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_suburb|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_TOWN-SUBURB_LABEL: Joomla form field show_suburb; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_state|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_STATE-COUNTY_LABEL: Joomla form field show_state; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_postcode|["integer", "string"]|нет|["", 0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_POST-ZIP_CODE_LABEL: Joomla form field show_postcode; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_country|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Country: Joomla form field show_country; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_telephone|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Telephone: Joomla form field show_telephone; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_mobile|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Mobile Phone: Joomla form field show_mobile; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_fax|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Fax: Joomla form field show_fax; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_webpage|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Webpage: Joomla form field show_webpage; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.show_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Image: Joomla form field show_image; input is validated and filtered according to x-joomla-form.|show_info:1|
|params.allow_vcard|["integer", "string"]|нет|["", 0, 1, "0", "1"]|vCard: Joomla form field allow_vcard; input is validated and filtered according to x-joomla-form.||
|params.show_misc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Miscellaneous Information: Joomla form field show_misc; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.articles_display_num|"string"|нет|["", "use_contact", "5", "10", "15", "20", "25", "30", "50", "75", "100", "150", "200", "250", "300", "0"]|# Articles to List: Joomla form field articles_display_num; input is validated and filtered according to x-joomla-form.||
|params.show_links|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Links: Joomla form field show_links; input is validated and filtered according to x-joomla-form.||
|params.linka_name|"string"|нет|""|Link A Label: Joomla form field linka_name; input is validated and filtered according to x-joomla-form.||
|params.linkb_name|"string"|нет|""|Link B Label: Joomla form field linkb_name; input is validated and filtered according to x-joomla-form.||
|params.linkc_name|"string"|нет|""|Link C Label: Joomla form field linkc_name; input is validated and filtered according to x-joomla-form.||
|params.linkd_name|"string"|нет|""|Link D Label: Joomla form field linkd_name; input is validated and filtered according to x-joomla-form.||
|params.linke_name|"string"|нет|""|Link E Label: Joomla form field linke_name; input is validated and filtered according to x-joomla-form.||
|params.show_email_form|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Form: Joomla form field show_email_form; input is validated and filtered according to x-joomla-form.||
|params.show_email_copy|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Send Copy to Submitter: Joomla form field show_email_copy; input is validated and filtered according to x-joomla-form.||
|params.validate_session|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Session Check: Joomla form field validate_session; input is validated and filtered according to x-joomla-form.||
|params.custom_reply|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Custom Reply: Stops Joomla from sending the email, allowing for Plugins to handle integration with other systems.||
|params.redirect|"string"|нет|""|Contact Redirect URL: Joomla form field redirect; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_contact/tmpl/form/edit.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
## Component view metadata: components/com_content/tmpl/archive/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.catid|"array"|нет|[]|Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.orderby_sec|"string"|нет|["date", "rdate", "alpha", "ralpha", "author", "rauthor", "hits", "rhits", "order", "vote", "rvote", "rank", "rrank"]|Article Order: Joomla form field orderby_sec; input is validated and filtered according to x-joomla-form.||
|params.order_date|"string"|нет|["created", "modified", "published"]|Date for Ordering: Joomla form field order_date; input is validated and filtered according to x-joomla-form.||
|params.year_sort_order|"string"|нет|["ASC", "DESC"]|Year Sort Order: The order in which years will appear in the year sort dropdown. Oldest First shows years in ascending order (2011, 2012...). Most Recent First shows years in descending order (2025, 2024...).||
|params.display_num|["integer", "string"]|нет|["", 5, 10, 15, 20, 25, 30, 50, 100, 0, "5", "10", "15", "20", "25", "30", "50", "100", "0"]|# Articles to List: Joomla form field display_num; input is validated and filtered according to x-joomla-form.||
|params.filter_field|"string"|нет|["", "hide", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.introtext_limit|["integer", "string"]|нет|"100"|Intro text Limit: Joomla form field introtext_limit; input is validated and filtered according to x-joomla-form.||
|params.show_intro|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|params.info_block_position|"string"|нет|["", "use_article", "0", "1", "2"]|Position of Article Info: Joomla form field info_block_position; input is validated and filtered according to x-joomla-form.||
|params.info_block_show_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Article Info Title: Joomla form field info_block_show_title; input is validated and filtered according to x-joomla-form.||
|params.show_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|params.link_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|params.show_parent_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|params.link_parent_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|params.link_titles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Linked Titles: If set to Yes, the article title will be a link to the article.||
|params.show_author|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|params.link_author|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|params.show_create_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|params.show_modify_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|params.show_publish_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|params.show_item_navigation|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|params.show_hits|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_content/tmpl/article/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Select Article: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_title|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|params.link_titles|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.||
|params.show_intro|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|params.info_block_position|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Position of Article Info: Joomla form field info_block_position; input is validated and filtered according to x-joomla-form.||
|params.info_block_show_title|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Article Info Title: Joomla form field info_block_show_title; input is validated and filtered according to x-joomla-form.||
|params.show_category|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|params.link_category|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|params.show_parent_category|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|params.link_parent_category|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|params.show_associations|["integer", "string"]|нет|""|Associations: Joomla form field show_associations; input is validated and filtered according to x-joomla-form.||
|params.show_author|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|params.link_author|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|params.show_create_date|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|params.show_modify_date|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|params.show_publish_date|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|params.show_item_navigation|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|params.show_vote|["integer", "string"]|нет|""|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|params.show_hits|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_noauth|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|params.urls_position|["integer", "string"]|нет|["", 0, 1, -1, "0", "1", "-1"]|Positioning of the Links: Joomla form field urls_position; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_content/tmpl/categories/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Select the Top Level Category: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_base_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Top Level Category Description: Joomla form field show_base_description; input is validated and filtered according to x-joomla-form.||
|params.categories_description|"string"|нет|""|Alternative Description: Joomla form field categories_description; input is validated and filtered according to x-joomla-form.||
|params.maxLevelcat|["integer", "string"]|нет|["", -1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevelcat; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories_cat; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc_cat; input is validated and filtered according to x-joomla-form.||
|params.show_cat_num_articles_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Articles in Category: Joomla form field show_cat_num_articles_cat; input is validated and filtered according to x-joomla-form.||
|params.show_category_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|params.show_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|params.show_description_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|params.maxLevel|["integer", "string"]|нет|["", -1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.||
|params.show_no_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|No Articles Message: Joomla form field show_no_articles; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.||
|params.show_cat_num_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Articles in Category: Joomla form field show_cat_num_articles; input is validated and filtered according to x-joomla-form.||
|params.blog_class_leading|"string"|нет|""|Leading Article Class: Joomla form field blog_class_leading; input is validated and filtered according to x-joomla-form.||
|params.blog_class|"string"|нет|""|Article Class: Joomla form field blog_class; input is validated and filtered according to x-joomla-form.||
|params.num_leading_articles|["integer", "string"]|нет|""|# Leading Articles: Joomla form field num_leading_articles; input is validated and filtered according to x-joomla-form.||
|params.num_intro_articles|["integer", "string"]|нет|""|# Intro Articles: Joomla form field num_intro_articles; input is validated and filtered according to x-joomla-form.||
|params.num_links|["integer", "string"]|нет|""|# Links: Joomla form field num_links; input is validated and filtered according to x-joomla-form.||
|params.show_subcategory_content|["integer", "string"]|нет|["", 0, -1, 1, 2, 3, 4, 5, "0", "-1", "1", "2", "3", "4", "5"]|Include Subcategories: Joomla form field show_subcategory_content; input is validated and filtered according to x-joomla-form.||
|params.orderby_pri|"string"|нет|["", "none", "alpha", "ralpha", "order"]|Category Order: Joomla form field orderby_pri; input is validated and filtered according to x-joomla-form.||
|params.orderby_sec|"string"|нет|["", "front", "rdate", "date", "alpha", "ralpha", "author", "rauthor", "hits", "rhits", "order", "rorder", "vote", "rvote", "rank", "rrank"]|Article Order: Joomla form field orderby_sec; input is validated and filtered according to x-joomla-form.||
|params.order_date|"string"|нет|["", "created", "modified", "published"]|Date for Ordering: Joomla form field order_date; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.filter_field|"string"|нет|["", "hide", "title", "author", "hits"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|params.list_show_date|"string"|нет|["", "0", "created", "modified", "published"]|Date: Joomla form field list_show_date; input is validated and filtered according to x-joomla-form.||
|params.date_format|"string"|нет|""|Date Format: Joomla form field date_format; input is validated and filtered according to x-joomla-form.||
|params.list_show_hits|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Hits: Joomla form field list_show_hits; input is validated and filtered according to x-joomla-form.||
|params.list_show_author|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Author: Joomla form field list_show_author; input is validated and filtered according to x-joomla-form.||
|params.display_num|["integer", "string"]|нет|["", 5, 10, 15, 20, 25, 30, 50, 100, 0, "5", "10", "15", "20", "25", "30", "50", "100", "0"]|# Articles to List: Joomla form field display_num; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.article_layout|"string"|нет|""|Choose a Layout: Default layout to use for items.||
|params.show_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|params.link_titles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.||
|params.show_intro|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|params.show_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|params.link_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|params.show_parent_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|params.link_parent_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|params.show_author|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|params.link_author|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|params.show_create_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|params.show_modify_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|params.show_publish_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|params.show_item_navigation|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|params.show_vote|["integer", "string"]|нет|""|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|params.show_readmore|["integer", "string"]|нет|["", 0, 1, "0", "1"]|&quot;Read More&quot; Link: If set to Show, the Read more &hellip; link will show if Main text has been provided for the Article.||
|params.show_readmore_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Read More with Title: Joomla form field show_readmore_title; input is validated and filtered according to x-joomla-form.||
|params.show_hits|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|params.show_noauth|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
|params.feed_summary|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Include in Feed: Joomla form field feed_summary; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_content/tmpl/category/blog.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Choose a Category: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|request.filter_tag|"array"|нет|""|Tags: Joomla form field filter_tag; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.layout_type|"string"|нет|"blog"|layout_type: Joomla form field layout_type; input is validated and filtered according to x-joomla-form.||
|params.show_category_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|params.show_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|params.show_description_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|params.maxLevel|["integer", "string"]|нет|["", -1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Maximum number of levels of subcategories to show.||
|params.show_empty_categories|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.||
|params.show_no_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|No Articles Message: Joomla form field show_no_articles; input is validated and filtered according to x-joomla-form.||
|params.show_category_heading_title_text|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Heading: Joomla form field show_category_heading_title_text; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Image: Joomla form field show_subcat_image; input is validated and filtered according to x-joomla-form.||
|params.show_cat_num_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Articles in Category: Joomla form field show_cat_num_articles; input is validated and filtered according to x-joomla-form.||
|params.show_cat_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_cat_tags; input is validated and filtered according to x-joomla-form.||
|params.num_leading_articles|["integer", "string"]|нет|""|# Leading Articles: Joomla form field num_leading_articles; input is validated and filtered according to x-joomla-form.||
|params.blog_class_leading|"string"|нет|""|Leading Article Class: Joomla form field blog_class_leading; input is validated and filtered according to x-joomla-form.||
|params.num_intro_articles|["integer", "string"]|нет|""|# Intro Articles: Joomla form field num_intro_articles; input is validated and filtered according to x-joomla-form.||
|params.blog_class|"string"|нет|""|Article Class: You can add any CSS class for your own styling ideas.<br>Add a border on top with class boxed.<br>For image position use for example image-left, image-right. Add image-alternate for alternate ordering of intro images.||
|params.num_columns|["integer", "string"]|нет|""|# Columns: Joomla form field num_columns; input is validated and filtered according to x-joomla-form.||
|params.multi_column_order|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Multi Column Direction: Joomla form field multi_column_order; input is validated and filtered according to x-joomla-form.||
|params.num_links|["integer", "string"]|нет|""|# Links: Joomla form field num_links; input is validated and filtered according to x-joomla-form.||
|params.show_featured|"string"|нет|["", "show", "hide", "only"]|Featured Articles: Joomla form field show_featured; input is validated and filtered according to x-joomla-form.||
|params.list_author_filtering_type|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Author Filtering Type: Joomla form field list_author_filtering_type; input is validated and filtered according to x-joomla-form.||
|params.list_author|"array"|нет|""|Authors: Joomla form field list_author; input is validated and filtered according to x-joomla-form.|list_author_filtering_type!:2|
|params.link_intro_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Linked Intro Image: Joomla form field link_intro_image; input is validated and filtered according to x-joomla-form.||
|params.show_subcategory_content|["integer", "string"]|нет|["", 0, -1, 1, 2, 3, 4, 5, "0", "-1", "1", "2", "3", "4", "5"]|Include Subcategories: Joomla form field show_subcategory_content; input is validated and filtered according to x-joomla-form.||
|params.orderby_pri|"string"|нет|["", "none", "alpha", "ralpha", "order"]|Category Order: Joomla form field orderby_pri; input is validated and filtered according to x-joomla-form.||
|params.orderby_sec|"string"|нет|["", "front", "rdate", "date", "alpha", "ralpha", "author", "rauthor", "hits", "rhits", "random", "order", "rorder", "vote", "rvote", "rank", "rrank"]|Article Order: Joomla form field orderby_sec; input is validated and filtered according to x-joomla-form.||
|params.order_date|"string"|нет|["", "created", "modified", "published", "unpublished"]|Date for Ordering: Joomla form field order_date; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.article_layout|"string"|нет|""|Choose a Layout: Default layout to use for items.||
|params.show_title|"string"|нет|["", "use_article", "0", "1"]|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|params.link_titles|"string"|нет|["", "use_article", "0", "1"]|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.||
|params.show_intro|"string"|нет|["", "use_article", "0", "1"]|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|params.info_block_position|"string"|нет|["", "use_article", "0", "1", "2"]|Position of Article Info: Joomla form field info_block_position; input is validated and filtered according to x-joomla-form.||
|params.info_block_show_title|"string"|нет|["", "use_article", "0", "1"]|Article Info Title: Joomla form field info_block_show_title; input is validated and filtered according to x-joomla-form.||
|params.show_category|"string"|нет|["", "use_article", "0", "1"]|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|params.link_category|"string"|нет|["", "use_article", "0", "1"]|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|params.show_parent_category|"string"|нет|["", "use_article", "0", "1"]|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|params.link_parent_category|"string"|нет|["", "use_article", "0", "1"]|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|params.show_associations|"string"|нет|""|Associations: Joomla form field show_associations; input is validated and filtered according to x-joomla-form.||
|params.show_author|"string"|нет|["", "use_article", "0", "1"]|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|params.link_author|"string"|нет|["", "use_article", "0", "1"]|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|params.show_create_date|"string"|нет|["", "use_article", "0", "1"]|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|params.show_modify_date|"string"|нет|["", "use_article", "0", "1"]|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|params.show_publish_date|"string"|нет|["", "use_article", "0", "1"]|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|params.show_item_navigation|"string"|нет|["", "use_article", "0", "1"]|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|params.show_vote|"string"|нет|""|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|params.show_readmore|["integer", "string"]|нет|["", 0, 1, "0", "1"]|&quot;Read More&quot; Link: If set to Show, the Read more &hellip; link will show if Main text has been provided for the Article.||
|params.show_readmore_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Read More with Title: Joomla form field show_readmore_title; input is validated and filtered according to x-joomla-form.||
|params.show_hits|"string"|нет|["", "use_article", "0", "1"]|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|params.show_tags|"string"|нет|["", "use_article", "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_noauth|"string"|нет|["", "use_article", "0", "1"]|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
|params.feed_summary|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Include in Feed: Joomla form field feed_summary; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_content/tmpl/category/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Choose a Category: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|request.filter_tag|"array"|нет|""|Tags: Joomla form field filter_tag; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_category_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|params.show_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|params.show_description_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|params.maxLevel|["integer", "string"]|нет|["", -1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.||
|params.show_no_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|No Articles Message: Joomla form field show_no_articles; input is validated and filtered according to x-joomla-form.||
|params.show_category_heading_title_text|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Heading: Joomla form field show_category_heading_title_text; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Image: Joomla form field show_subcat_image; input is validated and filtered according to x-joomla-form.||
|params.show_cat_num_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Articles in Category: Joomla form field show_cat_num_articles; input is validated and filtered according to x-joomla-form.||
|params.show_cat_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_cat_tags; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.filter_field|"string"|нет|["", "hide", "title", "author", "hits", "tag", "month"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.list_author_filtering_type|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Author Filtering Type: Joomla form field list_author_filtering_type; input is validated and filtered according to x-joomla-form.||
|params.list_author|"array"|нет|""|Authors: Joomla form field list_author; input is validated and filtered according to x-joomla-form.|list_author_filtering_type!:2|
|params.show_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|params.list_show_date|"string"|нет|["", "0", "created", "modified", "published"]|Date: Joomla form field list_show_date; input is validated and filtered according to x-joomla-form.||
|params.date_format|"string"|нет|""|Date Format: Optional format string for showing the date. For example, D M Y for day month year or you can use d-m-y for a short version eg. 28-12-16. See https://php.net/date. If left blank, it uses DATE_FORMAT_LC1 from your language file.||
|params.list_show_hits|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Hits: Joomla form field list_show_hits; input is validated and filtered according to x-joomla-form.||
|params.list_show_author|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Author: Joomla form field list_show_author; input is validated and filtered according to x-joomla-form.||
|params.list_show_votes|["integer", "string"]|нет|""|Show Votes in List: Joomla form field list_show_votes; input is validated and filtered according to x-joomla-form.||
|params.list_show_ratings|["integer", "string"]|нет|""|Show Ratings in List: Joomla form field list_show_ratings; input is validated and filtered according to x-joomla-form.||
|params.orderby_pri|"string"|нет|["", "none", "alpha", "ralpha", "order"]|Category Order: Joomla form field orderby_pri; input is validated and filtered according to x-joomla-form.||
|params.orderby_sec|"string"|нет|["", "front", "rdate", "date", "alpha", "ralpha", "author", "rauthor", "hits", "rhits", "random", "order", "rorder", "vote", "rvote", "rank", "rrank"]|Article Order: Joomla form field orderby_sec; input is validated and filtered according to x-joomla-form.||
|params.order_date|"string"|нет|["", "created", "modified", "published"]|Date for Ordering: Joomla form field order_date; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.display_num|["integer", "string"]|нет|["", 5, 10, 15, 20, 25, 30, 50, 100, 0, "5", "10", "15", "20", "25", "30", "50", "100", "0"]|# Articles to List: Joomla form field display_num; input is validated and filtered according to x-joomla-form.||
|params.show_featured|"string"|нет|["", "show", "hide", "only"]|Featured Articles: Joomla form field show_featured; input is validated and filtered according to x-joomla-form.||
|params.article_layout|"string"|нет|""|Choose a Layout: Default layout to use for items.||
|params.show_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|params.link_titles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.||
|params.show_intro|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|params.show_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|params.link_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|params.show_parent_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|params.link_parent_category|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|params.show_associations|["integer", "string"]|нет|""|Associations: Joomla form field show_associations; input is validated and filtered according to x-joomla-form.||
|params.show_author|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|params.link_author|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|params.show_create_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|params.show_modify_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|params.show_publish_date|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|params.show_item_navigation|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|params.show_vote|["integer", "string"]|нет|""|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|params.show_readmore|["integer", "string"]|нет|["", 0, 1, "0", "1"]|&quot;Read More&quot; Link: If set to Show, the Read more &hellip; link will show if Main text has been provided for the Article.||
|params.show_readmore_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Read More with Title: Joomla form field show_readmore_title; input is validated and filtered according to x-joomla-form.||
|params.show_hits|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|params.show_noauth|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
|params.feed_summary|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Include in Feed: Joomla form field feed_summary; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_content/tmpl/featured/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.featured_categories|"array"|нет|[]|Select Categories: Joomla form field featured_categories; input is validated and filtered according to x-joomla-form.||
|params.layout_type|"string"|нет|"blog"|layout_type: Joomla form field layout_type; input is validated and filtered according to x-joomla-form.||
|params.num_leading_articles|["integer", "string"]|нет|""|# Leading Articles: Joomla form field num_leading_articles; input is validated and filtered according to x-joomla-form.||
|params.blog_class_leading|"string"|нет|""|Leading Article Class: Joomla form field blog_class_leading; input is validated and filtered according to x-joomla-form.||
|params.num_intro_articles|["integer", "string"]|нет|""|# Intro Articles: Joomla form field num_intro_articles; input is validated and filtered according to x-joomla-form.||
|params.blog_class|"string"|нет|""|Article Class: You can add any CSS class for your own styling ideas.<br>Add a border on top with class boxed.<br>For image position use for example image-left, image-right. Add image-alternate for alternate ordering of intro images.||
|params.num_columns|["integer", "string"]|нет|""|# Columns: Joomla form field num_columns; input is validated and filtered according to x-joomla-form.||
|params.multi_column_order|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Multi Column Direction: Joomla form field multi_column_order; input is validated and filtered according to x-joomla-form.||
|params.num_links|["integer", "string"]|нет|""|# Links: Joomla form field num_links; input is validated and filtered according to x-joomla-form.||
|params.link_intro_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Linked Intro Image: Joomla form field link_intro_image; input is validated and filtered according to x-joomla-form.||
|params.orderby_pri|"string"|нет|["", "none", "alpha", "ralpha", "order"]|Category Order: Joomla form field orderby_pri; input is validated and filtered according to x-joomla-form.||
|params.orderby_sec|"string"|нет|["", "front", "rdate", "date", "alpha", "ralpha", "author", "rauthor", "hits", "rhits", "random", "order", "rorder", "vote", "rvote", "rank", "rrank"]|Article Order: Joomla form field orderby_sec; input is validated and filtered according to x-joomla-form.||
|params.order_date|"string"|нет|["", "created", "modified", "published", "unpublished"]|Date for Ordering: Joomla form field order_date; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.show_title|"string"|нет|["", "use_article", "0", "1"]|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|params.link_titles|"string"|нет|["", "use_article", "0", "1"]|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.||
|params.show_intro|"string"|нет|["", "use_article", "0", "1"]|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|params.info_block_position|"string"|нет|["", "use_article", "0", "1", "2"]|Position of Article Info: Joomla form field info_block_position; input is validated and filtered according to x-joomla-form.||
|params.info_block_show_title|"string"|нет|["", "use_article", "0", "1"]|Article Info Title: Joomla form field info_block_show_title; input is validated and filtered according to x-joomla-form.||
|params.show_category|"string"|нет|["", "use_article", "0", "1"]|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|params.link_category|"string"|нет|["", "use_article", "0", "1"]|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|params.show_parent_category|"string"|нет|["", "use_article", "0", "1"]|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|params.link_parent_category|"string"|нет|["", "use_article", "0", "1"]|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|params.show_associations|["integer", "string"]|нет|""|Associations: Joomla form field show_associations; input is validated and filtered according to x-joomla-form.||
|params.show_author|"string"|нет|["", "use_article", "0", "1"]|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|params.link_author|"string"|нет|["", "use_article", "0", "1"]|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|params.show_create_date|"string"|нет|["", "use_article", "0", "1"]|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|params.show_modify_date|"string"|нет|["", "use_article", "0", "1"]|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|params.show_publish_date|"string"|нет|["", "use_article", "0", "1"]|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|params.show_item_navigation|"string"|нет|["", "use_article", "0", "1"]|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|params.show_vote|"string"|нет|""|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|params.show_readmore|["integer", "string"]|нет|["", 0, 1, "0", "1"]|&quot;Read More&quot; Link: If set to Show, the Read more &hellip; link will show if Main text has been provided for the Article.||
|params.show_readmore_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Read More with Title: Joomla form field show_readmore_title; input is validated and filtered according to x-joomla-form.||
|params.show_hits|"string"|нет|["", "use_article", "0", "1"]|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_noauth|"string"|нет|["", "use_article", "0", "1"]|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
|params.feed_summary|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Include in Feed: Joomla form field feed_summary; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_content/tmpl/form/edit.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.enable_category|["integer", "string"]|нет|[0, 1, "0", "1"]|Specific Category: Joomla form field enable_category; input is validated and filtered according to x-joomla-form.||
|params.catid|["integer", "string"]|нет|""|Choose a Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.|enable_category:1|
|params.redirect_menuitem|["integer", "string"]|нет|""|Submission/Cancel Redirect: Select the page the user will be redirected to after a successful article submission and after cancel (if not set differently below). The default is to redirect to the home page.||
|params.custom_cancel_redirect|["integer", "string"]|нет|[0, 1, "0", "1"]|Custom Redirect on Cancel: If set to 'Yes', you can set a redirection page, distinct from above 'Submission/Cancel Redirect', to redirect to when user Cancels article submission.<br>If set to 'No', when user Cancels article submission, the user is redirected to the above 'Submission/Cancel Redirect' page.||
|params.cancel_redirect_menuitem|["integer", "string"]|нет|""|Cancel Redirect: Select the page the user will be redirected to after Canceling article submission. The default is to redirect to the same article submission page (cleaning form).|custom_cancel_redirect:1|
## Component view metadata: components/com_finder/tmpl/search/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.q|"string"|нет|""|Prefilled Search Term: Joomla form field q; input is validated and filtered according to x-joomla-form.||
|request.f|"string"|нет|""|Filter: Joomla form field f; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_date_filters|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Date Filters: Joomla form field show_date_filters; input is validated and filtered according to x-joomla-form.||
|params.show_advanced|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Advanced Search: Joomla form field show_advanced; input is validated and filtered according to x-joomla-form.||
|params.expand_advanced|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Expand Advanced Search: Joomla form field expand_advanced; input is validated and filtered according to x-joomla-form.||
|params.show_taxonomy|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Result Taxonomy: Joomla form field show_taxonomy; input is validated and filtered according to x-joomla-form.||
|params.show_description|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Result Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|params.description_length|["integer", "string"]|нет|""|Description Length: Joomla form field description_length; input is validated and filtered according to x-joomla-form.||
|params.show_image|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Result Image: Joomla form field show_image; input is validated and filtered according to x-joomla-form.||
|params.image_class|"string"|нет|""|Image Class: Joomla form field image_class; input is validated and filtered according to x-joomla-form.|show_image!:0|
|params.link_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Linked Image: Joomla form field link_image; input is validated and filtered according to x-joomla-form.|show_image!:0|
|params.show_date|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Result Date: Joomla form field show_date; input is validated and filtered according to x-joomla-form.||
|params.show_url|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Result URL: Joomla form field show_url; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.list_limit|["integer", "string"]|нет|[5, 10, 15, 20, 25, 30, 50, 100, 0, "5", "10", "15", "20", "25", "30", "50", "100", "0"]|Select number of items per page.: Joomla form field list_limit; input is validated and filtered according to x-joomla-form.||
|params.allow_empty_query|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Allow Empty Search: Only if a filter is selected, allow an empty search string to initiate a search within the filter constraints.||
|params.show_suggested_query|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Did You Mean: Joomla form field show_suggested_query; input is validated and filtered according to x-joomla-form.||
|params.show_explained_query|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Query Explanation: Joomla form field show_explained_query; input is validated and filtered according to x-joomla-form.||
|params.sort_order|"string"|нет|["", "relevance", "title", "date", "price", "sale_price"]|Sort Field: Joomla form field sort_order; input is validated and filtered according to x-joomla-form.||
|params.show_sort_order|["integer", "string"]|нет|[0, 1, "0", "1"]|Show Sort Fields: Joomla form field show_sort_order; input is validated and filtered according to x-joomla-form.||
|params.shown_sort_order|"array"|нет|""|Additional Sort Fields: Joomla form field shown_sort_order; input is validated and filtered according to x-joomla-form.|show_sort_order:1|
|params.sort_direction|"string"|нет|["", "desc", "asc"]|Sort Direction: Joomla form field sort_direction; input is validated and filtered according to x-joomla-form.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_newsfeeds/tmpl/categories/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Select the Top Level Category: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_base_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Top Level Category Description: Joomla form field show_base_description; input is validated and filtered according to x-joomla-form.||
|params.categories_description|"string"|нет|""|Alternative Description: Joomla form field categories_description; input is validated and filtered according to x-joomla-form.||
|params.maxLevelcat|["integer", "string"]|нет|["", -1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevelcat; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories_cat; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc_cat; input is validated and filtered according to x-joomla-form.||
|params.show_cat_items_cat|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Feeds in Category: Joomla form field show_cat_items_cat; input is validated and filtered according to x-joomla-form.||
|params.show_category_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|params.show_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|params.show_description_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|params.maxLevel|["integer", "string"]|нет|["", -1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.||
|params.show_cat_items|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Feeds in Category: Joomla form field show_cat_items; input is validated and filtered according to x-joomla-form.||
|params.filter_field|"string"|нет|["", "hide", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.show_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.show_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Links: Joomla form field show_link; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.show_feed_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Image: Joomla form field show_feed_image; input is validated and filtered according to x-joomla-form.||
|params.show_feed_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Description: Joomla form field show_feed_description; input is validated and filtered according to x-joomla-form.||
|params.show_item_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Content: Joomla form field show_item_description; input is validated and filtered according to x-joomla-form.||
|params.feed_character_count|["integer", "string"]|нет|""|Characters Count: 0 will show all the text.||
## Component view metadata: components/com_newsfeeds/tmpl/category/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Category: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_category_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|params.show_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|params.show_description_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|params.maxLevel|["integer", "string"]|нет|["", -1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|params.show_empty_categories|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_desc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.||
|params.show_subcat_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Subcategories Image: Joomla form field show_subcat_image; input is validated and filtered according to x-joomla-form.||
|params.show_cat_items|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Feeds in Category: Joomla form field show_cat_items; input is validated and filtered according to x-joomla-form.||
|params.filter_field|"string"|нет|["", "hide", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|# Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.show_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Links: Joomla form field show_link; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.show_feed_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Image: Joomla form field show_feed_image; input is validated and filtered according to x-joomla-form.||
|params.show_feed_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Description: Joomla form field show_feed_description; input is validated and filtered according to x-joomla-form.||
|params.show_item_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Content: Joomla form field show_item_description; input is validated and filtered according to x-joomla-form.||
|params.feed_character_count|["integer", "string"]|нет|""|Characters Count: 0 will show all the text.||
|params.feed_display_order|"string"|нет|["", "des", "asc"]|Feed Display Order: Joomla form field feed_display_order; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_newsfeeds/tmpl/newsfeed/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|["integer", "string"]|да|""|Feed: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_feed_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Image: Joomla form field show_feed_image; input is validated and filtered according to x-joomla-form.||
|params.show_feed_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Description: Joomla form field show_feed_description; input is validated and filtered according to x-joomla-form.||
|params.show_item_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Content: Joomla form field show_item_description; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.feed_character_count|["integer", "string"]|нет|""|Characters Count: 0 will show all the text.||
|params.feed_display_order|"string"|нет|["", "des", "asc"]|Feed Display Order: Joomla form field feed_display_order; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_privacy/tmpl/confirm/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## Component view metadata: components/com_privacy/tmpl/remind/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## Component view metadata: components/com_privacy/tmpl/request/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## Component view metadata: components/com_tags/tmpl/tag/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|"array"|да|""|Tag: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|request.types|"array"|нет|""|Select Content Type: Joomla form field types; input is validated and filtered according to x-joomla-form.||
|request.tag_list_language_filter|"string"|нет|""|Language Filter: Joomla form field tag_list_language_filter; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_tag_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tag Name: Joomla form field show_tag_title; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_tag_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tag Image: Joomla form field tag_list_show_tag_image; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_tag_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tag Description: Joomla form field tag_list_show_tag_description; input is validated and filtered according to x-joomla-form.||
|params.tag_list_image|"string"|нет|""|Image: Joomla form field tag_list_image; input is validated and filtered according to x-joomla-form.||
|params.tag_list_image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field tag_list_image_alt; input is validated and filtered according to x-joomla-form.||
|params.tag_list_image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|params.tag_list_description|"string"|нет|""|Description: Optional description to show at the top of the list. For example, this can be used when you have a layout that includes more than one tag.||
|params.tag_list_orderby|"string"|нет|["", "c.core_title", "match_count", "c.core_created_time", "c.core_modified_time", "c.core_publish_up"]|Order: Joomla form field tag_list_orderby; input is validated and filtered according to x-joomla-form.||
|params.tag_list_orderby_direction|"string"|нет|["", "ASC", "DESC"]|Direction: Joomla form field tag_list_orderby_direction; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_item_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Item Image: Joomla form field tag_list_show_item_image; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_item_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Item Description: Joomla form field tag_list_show_item_description; input is validated and filtered according to x-joomla-form.||
|params.tag_list_item_maximum_characters|["integer", "string"]|нет|""|Maximum Characters: Joomla form field tag_list_item_maximum_characters; input is validated and filtered according to x-joomla-form.||
|params.filter_field|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.return_any_or_all|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Match Type: Joomla form field return_any_or_all; input is validated and filtered according to x-joomla-form.||
|params.include_children|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Child Tags: Joomla form field include_children; input is validated and filtered according to x-joomla-form.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_tags/tmpl/tag/list.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.id|"array"|да|""|Tag: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|request.types|"array"|нет|""|Select Content Type: Joomla form field types; input is validated and filtered according to x-joomla-form.||
|request.tag_list_language_filter|"string"|нет|""|Language Filter: Joomla form field tag_list_language_filter; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_tag_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tag Name: Joomla form field show_tag_title; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_tag_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tag Image: Joomla form field tag_list_show_tag_image; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_tag_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tag Description: Joomla form field tag_list_show_tag_description; input is validated and filtered according to x-joomla-form.||
|params.tag_list_image|"string"|нет|""|Image: Joomla form field tag_list_image; input is validated and filtered according to x-joomla-form.||
|params.tag_list_image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field tag_list_image_alt; input is validated and filtered according to x-joomla-form.||
|params.tag_list_image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|params.tag_list_description|"string"|нет|""|Description: Optional description to show at the top of the list. For example, this can be used when you have a layout that includes more than one tag.||
|params.tag_list_orderby|"string"|нет|["", "c.core_title", "match_count", "c.core_created_time", "c.core_modified_time", "c.core_publish_up"]|Order: Joomla form field tag_list_orderby; input is validated and filtered according to x-joomla-form.||
|params.tag_list_orderby_direction|"string"|нет|["", "ASC", "DESC"]|Direction: Joomla form field tag_list_orderby_direction; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_item_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Item Image: Joomla form field tag_list_show_item_image; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_item_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Item Description: Joomla form field tag_list_show_item_description; input is validated and filtered according to x-joomla-form.||
|params.tag_list_item_maximum_characters|["integer", "string"]|нет|""|Maximum Characters: Joomla form field tag_list_item_maximum_characters; input is validated and filtered according to x-joomla-form.||
|params.filter_field|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_headings|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.display_num|["integer", "string"]|нет|["", 5, 10, 15, 20, 25, 30, 50, 100, 0, "5", "10", "15", "20", "25", "30", "50", "100", "0"]|# Items to List: Joomla form field display_num; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.tag_list_show_date|"string"|нет|["", "0", "created", "modified", "published"]|Date: Joomla form field tag_list_show_date; input is validated and filtered according to x-joomla-form.||
|params.date_format|"string"|нет|""|Date Format: Optional format string for showing the date. For example, D M Y for day month year or you can use d-m-y for a short version eg. 28-12-16. See https://php.net/date. If left blank, it uses DATE_FORMAT_LC1 from your language file.||
|params.return_any_or_all|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Match Type: Joomla form field return_any_or_all; input is validated and filtered according to x-joomla-form.||
|params.include_children|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Child Tags: Joomla form field include_children; input is validated and filtered according to x-joomla-form.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_tags/tmpl/tags/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.parent_id|["integer", "string"]|нет|""|Parent Tag: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|request.tag_list_language_filter|"string"|нет|""|Language Filter: Joomla form field tag_list_language_filter; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.tag_columns|["integer", "string"]|нет|"4"|Number of Columns: Joomla form field tag_columns; input is validated and filtered according to x-joomla-form.||
|params.all_tags_description|"string"|нет|""|Heading Description: Joomla form field all_tags_description; input is validated and filtered according to x-joomla-form.||
|params.all_tags_show_description_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Show Heading Image: Joomla form field all_tags_show_description_image; input is validated and filtered according to x-joomla-form.||
|params.all_tags_description_image|"string"|нет|""|Heading Image File: Joomla form field all_tags_description_image; input is validated and filtered according to x-joomla-form.||
|params.all_tags_description_image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field all_tags_description_image_alt; input is validated and filtered according to x-joomla-form.||
|params.all_tags_description_image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|params.all_tags_orderby|"string"|нет|["", "title", "hits", "created_time", "modified_time", "publish_up"]|Order: Joomla form field all_tags_orderby; input is validated and filtered according to x-joomla-form.||
|params.all_tags_orderby_direction|"string"|нет|["", "ASC", "DESC"]|Direction: Joomla form field all_tags_orderby_direction; input is validated and filtered according to x-joomla-form.||
|params.all_tags_show_tag_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Item Images: Joomla form field all_tags_show_tag_image; input is validated and filtered according to x-joomla-form.||
|params.all_tags_show_tag_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tag Descriptions: Joomla form field all_tags_show_tag_description; input is validated and filtered according to x-joomla-form.||
|params.all_tags_tag_maximum_characters|["integer", "string"]|нет|""|Maximum Characters: Joomla form field all_tags_tag_maximum_characters; input is validated and filtered according to x-joomla-form.||
|params.all_tags_show_tag_hits|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Hits: Joomla form field all_tags_show_tag_hits; input is validated and filtered according to x-joomla-form.||
|params.maximum|["integer", "string"]|нет|"200"|Maximum Items: Joomla form field maximum; input is validated and filtered according to x-joomla-form.||
|params.filter_field|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_limit|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|params.show_pagination|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|params.show_pagination_results|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.||
|params.show_feed_link|["integer", "string"]|нет|["", 0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
## Component view metadata: components/com_users/tmpl/login/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.loginredirectchoice|["integer", "string"]|нет|[0, 1, "0", "1"]|Choose Login Redirect Type: Joomla form field loginredirectchoice; input is validated and filtered according to x-joomla-form.||
|params.login_redirect_url|"string"|нет|""|Login Redirect: If a URL is entered here, users will be redirected to it after login.<br>The URL must be internal (eg: index.php?Itemid=999).|loginredirectchoice:0|
|params.login_redirect_menuitem|["integer", "string"]|нет|""|Menu Item Login Redirect: If no menu item is selected, users will be redirected to the their profile after login.|loginredirectchoice:1|
|params.logindescription_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Login Description: Joomla form field logindescription_show; input is validated and filtered according to x-joomla-form.||
|params.login_description|"string"|нет|""|Login Description Text: Joomla form field login_description; input is validated and filtered according to x-joomla-form.|logindescription_show:1|
|params.login_image|"string"|нет|""|Login Image: Joomla form field login_image; input is validated and filtered according to x-joomla-form.||
|params.login_image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field login_image_alt; input is validated and filtered according to x-joomla-form.||
|params.login_image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|params.logoutredirectchoice|["integer", "string"]|нет|[0, 1, "0", "1"]|Choose Logout Redirect Type: Joomla form field logoutredirectchoice; input is validated and filtered according to x-joomla-form.||
|params.logout_redirect_url|"string"|нет|""|Logout Redirect: Joomla form field logout_redirect_url; input is validated and filtered according to x-joomla-form.|logoutredirectchoice:0|
|params.logout_redirect_menuitem|["integer", "string"]|нет|""|Menu Item Logout Redirect: If no menu item is selected, users will be redirected to the homepage after logout.|logoutredirectchoice:1|
|params.logoutdescription_show|["integer", "string"]|нет|[0, 1, "0", "1"]|Logout Description: Joomla form field logoutdescription_show; input is validated and filtered according to x-joomla-form.||
|params.logout_description|"string"|нет|""|Logout Description Text: Joomla form field logout_description; input is validated and filtered according to x-joomla-form.|logoutdescription_show:1|
|params.logout_image|"string"|нет|""|Logout Image: Joomla form field logout_image; input is validated and filtered according to x-joomla-form.||
|params.logout_image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field logout_image_alt; input is validated and filtered according to x-joomla-form.||
|params.logout_image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|params.customRegLinkMenu|["integer", "string"]|нет|""|Registration Page: Set a Menu Item to utilize a custom registration page.||
## Component view metadata: components/com_users/tmpl/login/logout.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|request|"object"|нет|""|request: ||
|request.task|"string"|нет|"user.menulogout"|task: Joomla form field task; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.logout|["integer", "string"]|нет|""|Logout Redirection Page: Select or create the page the user will be redirected to after ending their current session by logging out. The default is to stay on the same page.||
## Component view metadata: components/com_users/tmpl/profile/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## Component view metadata: components/com_users/tmpl/profile/edit.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## Component view metadata: components/com_users/tmpl/registration/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## Component view metadata: components/com_users/tmpl/remind/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## Component view metadata: components/com_users/tmpl/reset/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## Component view metadata: components/com_wrapper/tmpl/wrapper/default.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.url|"string"|да|""|URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.width|"string"|нет|"100%"|Width: Joomla form field width; input is validated and filtered according to x-joomla-form.||
|params.height|["integer", "string"]|нет|"500"|Height: Joomla form field height; input is validated and filtered according to x-joomla-form.||
|params.height_auto|["integer", "string"]|нет|[0, 1, "0", "1"]|Auto Height: Joomla form field height_auto; input is validated and filtered according to x-joomla-form.||
|params.add_scheme|["integer", "string"]|нет|[0, 1, "0", "1"]|Auto Add: By default, http:// will be added unless it detects http:// or https:// in the URL you provide. This allows you to switch off this functionality.||
|params.lazyloading|"string"|нет|["eager", "lazy"]|Lazy Loading: Joomla form field lazyloading; input is validated and filtered according to x-joomla-form.||
