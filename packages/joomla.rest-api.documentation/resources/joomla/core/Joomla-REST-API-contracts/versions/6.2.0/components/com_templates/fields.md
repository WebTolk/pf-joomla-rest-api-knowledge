# com_templates: заполнение полей, Joomla 6.2.0

См. форму и схему ответа endpoint.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/templates/styles/site

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Style Name: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|assigned|"string"|нет|""|assigned: Joomla form field assigned; input is validated and filtered according to x-joomla-form.||
|home|["integer", "string"]|нет|"0"|Default: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|client_id|["integer", "string"]|нет|[0, "0"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
|template|"string"|да|""|template: Installed template element. Required on create; controller preserves the stored template on PATCH.||
## REST PATCH /v1/templates/styles/site/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Style Name: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|assigned|"string"|нет|""|assigned: Joomla form field assigned; input is validated and filtered according to x-joomla-form.||
|home|["integer", "string"]|нет|"0"|Default: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|client_id|["integer", "string"]|нет|[0, "0"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
|template|"string"|нет|""|template: Installed template element. Required on create; controller preserves the stored template on PATCH.||
## REST POST /v1/templates/styles/administrator

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Style Name: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|assigned|"string"|нет|""|assigned: Joomla form field assigned; input is validated and filtered according to x-joomla-form.||
|home|["integer", "string"]|нет|[0, 1, "0", "1"]|Default: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|client_id|["integer", "string"]|нет|[1, "1"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
|template|"string"|да|""|template: Installed template element. Required on create; controller preserves the stored template on PATCH.||
## REST PATCH /v1/templates/styles/administrator/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Style Name: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|assigned|"string"|нет|""|assigned: Joomla form field assigned; input is validated and filtered according to x-joomla-form.||
|home|["integer", "string"]|нет|[0, 1, "0", "1"]|Default: Joomla form field home; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|client_id|["integer", "string"]|нет|[1, "1"]|client_id: Fixed by the site/administrator route; cannot switch clients with the body.||
|template|"string"|нет|""|template: Installed template element. Required on create; controller preserves the stored template on PATCH.||

## Инвентарь стандартных форм UI

## administrator/components/com_templates/forms/filter_styles.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|client_id|["integer", "string"]|нет|[0, 1, "0", "1"]|Select Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search: Search in style description.||
|filter.menuitem|["integer", "string"]|нет|""|- Select Menu Item -: Joomla form field menuitem; input is validated and filtered according to x-joomla-form.|client_id:0|
|filter.template|"string"|нет|""|- Select Template -: Joomla form field template; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.title ASC", "a.title DESC", "a.home ASC", "a.home DESC", "a.template ASC", "a.template DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_templates/forms/filter_templates.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|client_id|["integer", "string"]|нет|[0, 1, "0", "1"]|Select Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search: Search in template name or folder name.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.element ASC", "a.element DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_templates/forms/source.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|extension_id|"string"|нет|""|extension_id: Joomla form field extension_id; input is validated and filtered according to x-joomla-form.||
|filename|"string"|нет|""|filename: Joomla form field filename; input is validated and filtered according to x-joomla-form.||
|source|"string"|нет|""|Source Code: Joomla form field source; input is validated and filtered according to x-joomla-form.||
|core|"string"|нет|""|Source Code: Joomla form field core; input is validated and filtered according to x-joomla-form.||
|show_core|["integer", "string"]|нет|[0, 1, "0", "1"]|Show Original File: Joomla form field show_core; input is validated and filtered according to x-joomla-form.||
|show_diff|["integer", "string"]|нет|[0, 1, "0", "1"]|Show Differences: Joomla form field show_diff; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_templates/forms/style.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|template|"string"|нет|""|Template: Joomla form field template; input is validated and filtered according to x-joomla-form.||
|client_id|["integer", "string"]|нет|"0"|Location: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Style Name: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|assigned|"string"|нет|""|assigned: Joomla form field assigned; input is validated and filtered according to x-joomla-form.||
|inheritable|["integer", "string"]|нет|""|inheritable: Joomla form field inheritable; input is validated and filtered according to x-joomla-form.||
|parent|"string"|нет|""|parent: Joomla form field parent; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_templates/forms/style_administrator.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|home|["integer", "string"]|нет|[0, 1, "0", "1"]|Default: Joomla form field home; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_templates/forms/style_site.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|home|["integer", "string"]|нет|"0"|Default: Joomla form field home; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_templates/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|template_positions_display|["integer", "string"]|нет|[0, 1, "0", "1"]|Preview Module Positions: Joomla form field template_positions_display; input is validated and filtered according to x-joomla-form.||
|upload_limit|["integer", "string"]|нет|"10"|Max. Upload Size (MB): Joomla form field upload_limit; input is validated and filtered according to x-joomla-form.||
|image_formats|"string"|нет|"gif,bmp,jpg,jpeg,png,webp"|Valid Image Formats: Joomla form field image_formats; input is validated and filtered according to x-joomla-form.||
|source_formats|"string"|нет|"txt,less,ini,xml,js,php,css,sass,scss,json"|Valid Source Formats: Joomla form field source_formats; input is validated and filtered according to x-joomla-form.||
|font_formats|"string"|нет|"woff,woff2,ttf,otf"|Valid Font Formats: Joomla form field font_formats; input is validated and filtered according to x-joomla-form.||
|compressed_formats|"string"|нет|"zip"|compressed_formats: Joomla form field compressed_formats; input is validated and filtered according to x-joomla-form.||
|difference|"string"|нет|["Inline", "SideBySide"]|File Diff Display: Joomla form field difference; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
