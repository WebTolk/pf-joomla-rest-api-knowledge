# com_modules: заполнение полей, Joomla 5.4.8

Маршруты site/administrator задают client_id=0/1. module — машинное имя mod_*.
params выбирается по module и client_id, а не только ID экземпляра.
assignment/assigned задают назначение на меню; пустой набор нельзя автоматически
считать «везде». position — позиция установленного шаблона.
GET types возвращает типы, а не экземпляры; ответ имеет отдельную схему.
Схемы стандартных параметров включены; сторонние типы требуют своего пакета.
Для снимка 5.4.8 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/modules/site

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|module|"string"|да|""|Module Type: Joomla form field module; input is validated and filtered according to x-joomla-form.||
|showtitle|["integer", "string"]|нет|[0, 1, "0", "1"]|Title: Joomla form field showtitle; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|position|"string"|нет|""|Position: Joomla form field position; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|content|"string"|нет|""|Text: Joomla form field content; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|assignment|["integer", "string"]|нет|[0, 1, -1, "0", "1", "-1", "-"]|assignment: 0 all pages, 1 included IDs, -1 excluded IDs, '-' none.||
|assigned|"array"|нет|""|assigned: Menu item IDs consumed by ModuleModel. Hidden XML widget does not imply a scalar string.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|client_id|["integer", "string"]|нет|[0, "0"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
## REST PATCH /v1/modules/site/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|module|"string"|нет|""|Module Type: Joomla form field module; input is validated and filtered according to x-joomla-form.||
|showtitle|["integer", "string"]|нет|[0, 1, "0", "1"]|Title: Joomla form field showtitle; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|position|"string"|нет|""|Position: Joomla form field position; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|content|"string"|нет|""|Text: Joomla form field content; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|assignment|["integer", "string"]|нет|[0, 1, -1, "0", "1", "-1", "-"]|assignment: 0 all pages, 1 included IDs, -1 excluded IDs, '-' none.||
|assigned|"array"|нет|""|assigned: Menu item IDs consumed by ModuleModel. Hidden XML widget does not imply a scalar string.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|client_id|["integer", "string"]|нет|[0, "0"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
## REST POST /v1/modules/administrator

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|module|"string"|да|""|Module Type: Joomla form field module; input is validated and filtered according to x-joomla-form.||
|showtitle|["integer", "string"]|нет|[0, 1, "0", "1"]|Title: Joomla form field showtitle; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|position|"string"|нет|""|Position: Joomla form field position; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|"*"|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|content|"string"|нет|""|Text: Joomla form field content; input is validated and filtered according to x-joomla-form.||
|assignment|"string"|нет|""|assignment: Joomla form field assignment; input is validated and filtered according to x-joomla-form.||
|assigned|"string"|нет|""|assigned: Joomla form field assigned; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|client_id|["integer", "string"]|нет|[1, "1"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
## REST PATCH /v1/modules/administrator/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|module|"string"|нет|""|Module Type: Joomla form field module; input is validated and filtered according to x-joomla-form.||
|showtitle|["integer", "string"]|нет|[0, 1, "0", "1"]|Title: Joomla form field showtitle; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|position|"string"|нет|""|Position: Joomla form field position; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|"*"|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|content|"string"|нет|""|Text: Joomla form field content; input is validated and filtered according to x-joomla-form.||
|assignment|"string"|нет|""|assignment: Joomla form field assignment; input is validated and filtered according to x-joomla-form.||
|assigned|"string"|нет|""|assigned: Joomla form field assigned; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|client_id|["integer", "string"]|нет|[1, "1"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||

## Инвентарь стандартных форм UI

## administrator/components/com_modules/forms/advanced.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.module_tag|"string"|нет|"div"|Module Tag: Joomla form field module_tag; input is validated and filtered according to x-joomla-form.||
|params.bootstrap_size|["integer", "string"]|нет|""|Bootstrap Size: Joomla form field bootstrap_size; input is validated and filtered according to x-joomla-form.||
|params.header_tag|"string"|нет|"h3"|Header Tag: Joomla form field header_tag; input is validated and filtered according to x-joomla-form.||
|params.header_class|"string"|нет|""|Header Class: Joomla form field header_class; input is validated and filtered according to x-joomla-form.||
|params.style|"string"|нет|""|Module Style: Joomla form field style; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_modules/forms/filter_modules.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|client_id|["integer", "string"]|нет|[0, 1, "0", "1"]|Select Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Modules: Search in module title and note. Prefix with ID: to search for a module ID.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.position|"string"|нет|""|Position: Joomla form field position; input is validated and filtered according to x-joomla-form.||
|filter.module|"string"|нет|""|Type: Joomla form field module; input is validated and filtered according to x-joomla-form.||
|filter.menuitem|["integer", "string"]|нет|""|Menu Selection: Joomla form field menuitem; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.published ASC", "a.published DESC", "a.title ASC", "a.title DESC", "a.position ASC", "a.position DESC", "name ASC", "name DESC", "pages ASC", "pages DESC", "ag.title ASC", "ag.title DESC", "l.title ASC", "l.title DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_modules/forms/filter_modulesadmin.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|client_id|["integer", "string"]|нет|[0, 1, "0", "1"]|Select Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Modules: Search in module title and note. Prefix with ID: to search for a module ID.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.position|"string"|нет|""|Position: Joomla form field position; input is validated and filtered according to x-joomla-form.||
|filter.module|"string"|нет|""|Type: Joomla form field module; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.published ASC", "a.published DESC", "a.title ASC", "a.title DESC", "a.position ASC", "a.position DESC", "name ASC", "name DESC", "ag.title ASC", "ag.title DESC", "a.language ASC", "a.language DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_modules/forms/module.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|module|"string"|нет|""|Module Type: Joomla form field module; input is validated and filtered according to x-joomla-form.||
|showtitle|["integer", "string"]|нет|[0, 1, "0", "1"]|Title: Joomla form field showtitle; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|client_id|["integer", "string"]|нет|""|Module Location: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|position|"string"|нет|""|Position: Joomla form field position; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|content|"string"|нет|""|Text: Joomla form field content; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|assignment|["integer", "string"]|нет|[0, 1, -1, "0", "1", "-1", "-"]|assignment: 0 all pages, 1 included IDs, -1 excluded IDs, '-' none.||
|assigned|"array"|нет|""|assigned: Menu item IDs consumed by ModuleModel. Hidden XML widget does not imply a scalar string.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_modules/forms/moduleadmin.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|module|"string"|нет|""|Module Type: Joomla form field module; input is validated and filtered according to x-joomla-form.||
|showtitle|["integer", "string"]|нет|[0, 1, "0", "1"]|Title: Joomla form field showtitle; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|client_id|"string"|нет|""|Module Location: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|position|"string"|нет|""|Position: Joomla form field position; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|"*"|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|content|"string"|нет|""|Text: Joomla form field content; input is validated and filtered according to x-joomla-form.||
|assignment|"string"|нет|""|assignment: Joomla form field assignment; input is validated and filtered according to x-joomla-form.||
|assigned|"string"|нет|""|assigned: Joomla form field assigned; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_modules/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|redirect_edit|"string"|нет|["admin", "site"]|Edit Module: Select if module editing should be opened in the site or administration interface.||
|adminlangfilter|["integer", "string"]|нет|[0, 1, "0", "1"]|Language Filtering: Allows filtering administrator modules per administrator language.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
