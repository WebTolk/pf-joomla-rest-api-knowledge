# com_redirect: заполнение полей, Joomla 5.4.8

См. форму и схему ответа endpoint.
Для снимка 5.4.8 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/redirects

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|old_url|"string"|да|""|Expired URL: Enter the URL that has to be redirected.||
|new_url|"string"|да|""|New URL: Enter the URL to be redirected to.||
|comment|"string"|нет|""|Comment: Joomla form field comment; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|header|["integer", "string"]|нет|"301"|Redirect Status Code: Choose the HTTP 1.1 status code to associate with the redirect. Only status codes from 300-399 correspond to a redirect.||
## REST PATCH /v1/redirects/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|old_url|"string"|нет|""|Expired URL: Enter the URL that has to be redirected.||
|new_url|"string"|нет|""|New URL: Enter the URL to be redirected to.||
|comment|"string"|нет|""|Comment: Joomla form field comment; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|header|["integer", "string"]|нет|"301"|Redirect Status Code: Choose the HTTP 1.1 status code to associate with the redirect. Only status codes from 300-399 correspond to a redirect.||

## Инвентарь стандартных форм UI

## administrator/components/com_redirect/forms/filter_links.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Links: Search in expired URL, new URL, referring page and comment. Prefix with ID: to search for a link ID.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.http_status|"string"|нет|""|Status Code: Joomla form field http_status; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.published ASC", "a.published DESC", "a.old_url ASC", "a.old_url DESC", "a.new_url ASC", "a.new_url DESC", "a.referer ASC", "a.referer DESC", "a.created_date ASC", "a.created_date DESC", "a.hits ASC", "a.hits DESC", "a.header ASC", "a.header DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"5"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_redirect/forms/link.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|old_url|"string"|да|""|Expired URL: Enter the URL that has to be redirected.||
|new_url|"string"|да|""|New URL: Enter the URL to be redirected to.||
|comment|"string"|нет|""|Comment: Joomla form field comment; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|referer|"string"|нет|""|Link Referrer: Joomla form field referer; input is validated and filtered according to x-joomla-form.||
|created_date|"string"|нет|""|Created Date: Joomla form field created_date; input is validated and filtered according to x-joomla-form.||
|modified_date|"string"|нет|""|Last Updated Date: Joomla form field modified_date; input is validated and filtered according to x-joomla-form.||
|header|["integer", "string"]|нет|"301"|Redirect Status Code: Choose the HTTP 1.1 status code to associate with the redirect. Only status codes from 300-399 correspond to a redirect.||
## administrator/components/com_redirect/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|mode|["integer", "string"]|нет|[0, 1, "0", "1"]|Activate Advanced Mode: The Advanced Mode allows the use of HTTP 1.1 status codes other than the default '301 Permanently Moved'.||
|separator|"string"|нет|"&#124;"|Bulk Import Separator: The separator used for bulk import, by default it is '&#124;' but it can be ',' for a copy / paste from a CSV file for instance.||
|defaultImportState|["integer", "string"]|нет|[0, 1, "0", "1"]|Import State: When batch importing redirects, enable or disable by default.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
