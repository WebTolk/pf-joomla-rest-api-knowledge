# com_users: заполнение полей, Joomla 6.2.0

Пароли не возвращаются GET. POST при наличии password копирует его в password2.
PATCH с пропущенным password сохраняет пароль. Пропущенные groups восстанавливает
специальный обработчик. groups — ID групп; viewlevels.rules — группы доступа,
что отличается от вложенных правил ACL.
Фильтры registrationDateStart/End и lastVisitDateStart/End требуют RFC3339.
Для viewlevels POST rules — массив ID групп, PATCH rules — JSON-строка массива
(например "[2,3]"): API-контроллер вызывает json_decode до фильтра формы.
Массив в PATCH вызывает TypeError; пропуск rules использует сохранённую строку.
Профиль и custom fields могут расширяться user-плагинами.
В 6.2.0 создание, изменение и удаление viewlevels требует core.admin на com_users. Права групп также проверяются через core.admin.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/users

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|да|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|username|"string"|да|""|Login Name (Username): Joomla form field username; input is validated and filtered according to x-joomla-form.||
|password|"string"|нет|""|Password: Joomla form field password; input is validated and filtered according to x-joomla-form.||
|email|"string"|да|""|Email: Joomla form field email; input is validated and filtered according to x-joomla-form.||
|sendEmail|["integer", "string"]|нет|[0, 1, "0", "1"]|Receive System Emails: Joomla form field sendEmail; input is validated and filtered according to x-joomla-form.||
|block|["integer", "string"]|нет|[1, 0, "1", "0"]|User Status: Joomla form field block; input is validated and filtered according to x-joomla-form.||
|requireReset|["integer", "string"]|нет|[0, 1, "0", "1"]|Require Password Reset: Joomla form field requireReset; input is validated and filtered according to x-joomla-form.||
|groups|"array"|нет|""|groups: User group IDs. UserModel consumes an array although the XML widget is hidden.||
|params|"object"|нет|""|params: ||
|params.admin_style|["integer", "string"]|нет|""|Backend Template Style: Joomla form field admin_style; input is validated and filtered according to x-joomla-form.||
|params.colorScheme|"string"|нет|["", "os", "light", "dark"]|Dark Mode: Joomla form field colorScheme; input is validated and filtered according to x-joomla-form.||
|params.allowTourAutoStart|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Allow Auto Starting Tours: Joomla form field allowTourAutoStart; input is validated and filtered according to x-joomla-form.||
|params.admin_language|"string"|нет|""|Backend Language: Joomla form field admin_language; input is validated and filtered according to x-joomla-form.||
|params.language|"string"|нет|""|Frontend Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|params.editor|"string"|нет|""|Editor: Joomla form field editor; input is validated and filtered according to x-joomla-form.||
|params.timezone|"string"|нет|""|Time Zone: Joomla form field timezone; input is validated and filtered according to x-joomla-form.||
|params.a11y_mono|"string"|нет|["0", "monochrome"]|Monochrome: Joomla form field a11y_mono; input is validated and filtered according to x-joomla-form.||
|params.a11y_contrast|"string"|нет|["0", "high_contrast"]|High Contrast: Joomla form field a11y_contrast; input is validated and filtered according to x-joomla-form.||
|params.a11y_highlight|"string"|нет|["0", "highlight"]|Highlight Links: Joomla form field a11y_highlight; input is validated and filtered according to x-joomla-form.||
|params.a11y_font|"string"|нет|["0", "fontsize"]|Increase Font Size: Joomla form field a11y_font; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
## REST PATCH /v1/users/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|username|"string"|нет|""|Login Name (Username): Joomla form field username; input is validated and filtered according to x-joomla-form.||
|password|"string"|нет|""|Password: Joomla form field password; input is validated and filtered according to x-joomla-form.||
|email|"string"|нет|""|Email: Joomla form field email; input is validated and filtered according to x-joomla-form.||
|sendEmail|["integer", "string"]|нет|[0, 1, "0", "1"]|Receive System Emails: Joomla form field sendEmail; input is validated and filtered according to x-joomla-form.||
|block|["integer", "string"]|нет|[1, 0, "1", "0"]|User Status: Joomla form field block; input is validated and filtered according to x-joomla-form.||
|requireReset|["integer", "string"]|нет|[0, 1, "0", "1"]|Require Password Reset: Joomla form field requireReset; input is validated and filtered according to x-joomla-form.||
|groups|"array"|нет|""|groups: User group IDs. UserModel consumes an array although the XML widget is hidden.||
|params|"object"|нет|""|params: ||
|params.admin_style|["integer", "string"]|нет|""|Backend Template Style: Joomla form field admin_style; input is validated and filtered according to x-joomla-form.||
|params.colorScheme|"string"|нет|["", "os", "light", "dark"]|Dark Mode: Joomla form field colorScheme; input is validated and filtered according to x-joomla-form.||
|params.allowTourAutoStart|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Allow Auto Starting Tours: Joomla form field allowTourAutoStart; input is validated and filtered according to x-joomla-form.||
|params.admin_language|"string"|нет|""|Backend Language: Joomla form field admin_language; input is validated and filtered according to x-joomla-form.||
|params.language|"string"|нет|""|Frontend Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|params.editor|"string"|нет|""|Editor: Joomla form field editor; input is validated and filtered according to x-joomla-form.||
|params.timezone|"string"|нет|""|Time Zone: Joomla form field timezone; input is validated and filtered according to x-joomla-form.||
|params.a11y_mono|"string"|нет|["0", "monochrome"]|Monochrome: Joomla form field a11y_mono; input is validated and filtered according to x-joomla-form.||
|params.a11y_contrast|"string"|нет|["0", "high_contrast"]|High Contrast: Joomla form field a11y_contrast; input is validated and filtered according to x-joomla-form.||
|params.a11y_highlight|"string"|нет|["0", "highlight"]|Highlight Links: Joomla form field a11y_highlight; input is validated and filtered according to x-joomla-form.||
|params.a11y_font|"string"|нет|["0", "fontsize"]|Increase Font Size: Joomla form field a11y_font; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
## REST POST /v1/users/groups

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Group Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|parent_id|["integer", "string"]|нет|""|Group Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|actions|"array"|нет|""|actions: Joomla form field actions; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
## REST PATCH /v1/users/groups/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Group Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|parent_id|["integer", "string"]|нет|""|Group Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|actions|"array"|нет|""|actions: Joomla form field actions; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
## REST POST /v1/users/levels

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Level Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|"0"|Ordering: Select the ordering.||
|rules|"array"|нет|""|rules: ||
|com_fields|"object"|нет|""|com_fields: ||
## REST PATCH /v1/users/levels/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Level Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|"0"|Ordering: Select the ordering.||
|rules|"string"|нет|""|rules: PATCH preprocessSaveData calls json_decode on rules. Send a JSON-encoded ID array string, e.g. "[2,3]". Omission restores the stored JSON string. A JSON array here triggers a PHP TypeError, not the create contract.||
|com_fields|"object"|нет|""|com_fields: ||

## Инвентарь стандартных форм UI

## administrator/components/com_users/forms/category.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## administrator/components/com_users/forms/config_domain.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|да|""|Domain Name: Enter a domain name. Wildcards (*) are supported. For example:<br><strong>*</strong> allows or disallows all domains;<br><strong>*.com</strong> allows or disallows all .com domains;<br><strong>*.joomla.org</strong> allows or disallows all joomla.org subdomains.||
|rule|["integer", "string"]|да|[0, 1, "0", "1"]|Rule: Select whether to allow or disallow the domain.||
## administrator/components/com_users/forms/filter_debuggroup.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Assets: Search in asset name or title.||
|filter.component|"string"|нет|""|Component: Joomla form field component; input is validated and filtered according to x-joomla-form.||
|filter.level_start|"string"|нет|""|Start Level: Joomla form field level_start; input is validated and filtered according to x-joomla-form.||
|filter.level_end|"string"|нет|""|-End Level: Joomla form field level_end; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.title ASC", "a.title DESC", "a.name ASC", "a.name DESC", "a.lft ASC", "a.lft DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/filter_debuguser.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Assets: Search in asset name or title.||
|filter.component|"string"|нет|""|Component: Joomla form field component; input is validated and filtered according to x-joomla-form.||
|filter.level_start|"string"|нет|""|Start Level: Joomla form field level_start; input is validated and filtered according to x-joomla-form.||
|filter.level_end|"string"|нет|""|-End Level: Joomla form field level_end; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.title ASC", "a.title DESC", "a.name ASC", "a.name DESC", "a.lft ASC", "a.lft DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/filter_groups.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search User Groups: Search in group title. Prefix with ID: to search for a group ID.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.lft ASC", "a.lft DESC", "a.title ASC", "a.title DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/filter_levels.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Viewing Access Levels: Search in level name. Prefix with ID: to search for an access level ID.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.title ASC", "a.title DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/filter_notes.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search User Notes: Search in subject, name or username. Prefix with ID: or UID: to search for a note ID or user ID.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.category_id|["integer", "string"]|нет|""|Category: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.state ASC", "a.state DESC", "a.subject ASC", "a.subject DESC", "c.title ASC", "c.title DESC", "u.name ASC", "u.name DESC", "a.review_time ASC", "a.review_time DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/filter_users.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Users: Search in name, username or email. Prefix with ID: to search for a user ID.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.mfa|["integer", "string"]|нет|["", 1, 0, "1", "0"]|MFA: Joomla form field mfa; input is validated and filtered according to x-joomla-form.||
|filter.active|"string"|нет|""|Activated: Joomla form field active; input is validated and filtered according to x-joomla-form.||
|filter.group_id|["integer", "string"]|нет|""|User Groups: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|filter.lastvisitrange|"string"|нет|""|Last Visit: Joomla form field lastvisitrange; input is validated and filtered according to x-joomla-form.||
|filter.range|"string"|нет|""|Registered: Joomla form field range; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.name ASC", "a.name DESC", "a.username ASC", "a.username DESC", "a.block ASC", "a.block DESC", "a.activation ASC", "a.activation DESC", "a.email ASC", "a.email DESC", "a.lastvisitDate ASC", "a.lastvisitDate DESC", "a.registerDate ASC", "a.registerDate DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/group.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|id: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Group Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|parent_id|["integer", "string"]|нет|""|Group Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|actions|"array"|нет|""|actions: Joomla form field actions; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/level.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|id: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Level Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|"0"|Ordering: Select the ordering.||
|rules|"string"|нет|""|rules: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/mail.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|recurse|"string"|нет|""|Mail to Child User Groups: Joomla form field recurse; input is validated and filtered according to x-joomla-form.||
|mode|"string"|нет|""|Send in HTML Mode: Joomla form field mode; input is validated and filtered according to x-joomla-form.||
|disabled|"string"|нет|""|Send to Blocked Users: Joomla form field disabled; input is validated and filtered according to x-joomla-form.||
|group|["integer", "string"]|нет|"0"|Group: Joomla form field group; input is validated and filtered according to x-joomla-form.||
|bcc|"string"|нет|"1"|Recipients as BCC: Joomla form field bcc; input is validated and filtered according to x-joomla-form.||
|subject|"string"|да|""|Subject: Joomla form field subject; input is validated and filtered according to x-joomla-form.||
|message|"string"|да|""|Message: Joomla form field message; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/note.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|"string"|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|user_id|["integer", "string"]|да|""|User: Joomla form field user_id; input is validated and filtered according to x-joomla-form.||
|catid|["integer", "string"]|да|""|Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.||
|subject|"string"|нет|""|Subject: Joomla form field subject; input is validated and filtered according to x-joomla-form.||
|body|"string"|нет|""|Note: Joomla form field body; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|review_time|"string"|нет|"NOW"|Review Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/forms/user.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|да|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|username|"string"|да|""|Login Name (Username): Joomla form field username; input is validated and filtered according to x-joomla-form.||
|password|"string"|нет|""|Password: Joomla form field password; input is validated and filtered according to x-joomla-form.||
|password2|"string"|нет|""|Confirm Password: Joomla form field password2; input is validated and filtered according to x-joomla-form.||
|email|"string"|да|""|Email: Joomla form field email; input is validated and filtered according to x-joomla-form.||
|registerDate|"string"|нет|""|Registration Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|lastvisitDate|"string"|нет|""|Last Visit Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|lastResetTime|"string"|нет|""|Last Reset Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|resetCount|["integer", "string"]|нет|"0"|Password Reset Count: Joomla form field resetCount; input is validated and filtered according to x-joomla-form.||
|sendEmail|["integer", "string"]|нет|[0, 1, "0", "1"]|Receive System Emails: Joomla form field sendEmail; input is validated and filtered according to x-joomla-form.||
|block|["integer", "string"]|нет|[1, 0, "1", "0"]|User Status: Joomla form field block; input is validated and filtered according to x-joomla-form.||
|requireReset|["integer", "string"]|нет|[0, 1, "0", "1"]|Require Password Reset: Joomla form field requireReset; input is validated and filtered according to x-joomla-form.||
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|groups|"array"|нет|""|groups: User group IDs. UserModel consumes an array although the XML widget is hidden.||
|params|"object"|нет|""|params: ||
|params.admin_style|["integer", "string"]|нет|""|Backend Template Style: Joomla form field admin_style; input is validated and filtered according to x-joomla-form.||
|params.colorScheme|"string"|нет|["", "os", "light", "dark"]|Dark Mode: Joomla form field colorScheme; input is validated and filtered according to x-joomla-form.||
|params.allowTourAutoStart|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Allow Auto Starting Tours: Joomla form field allowTourAutoStart; input is validated and filtered according to x-joomla-form.||
|params.admin_language|"string"|нет|""|Backend Language: Joomla form field admin_language; input is validated and filtered according to x-joomla-form.||
|params.language|"string"|нет|""|Frontend Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|params.editor|"string"|нет|""|Editor: Joomla form field editor; input is validated and filtered according to x-joomla-form.||
|params.timezone|"string"|нет|""|Time Zone: Joomla form field timezone; input is validated and filtered according to x-joomla-form.||
|params.a11y_mono|"string"|нет|["0", "monochrome"]|Monochrome: Joomla form field a11y_mono; input is validated and filtered according to x-joomla-form.||
|params.a11y_contrast|"string"|нет|["0", "high_contrast"]|High Contrast: Joomla form field a11y_contrast; input is validated and filtered according to x-joomla-form.||
|params.a11y_highlight|"string"|нет|["0", "highlight"]|Highlight Links: Joomla form field a11y_highlight; input is validated and filtered according to x-joomla-form.||
|params.a11y_font|"string"|нет|["0", "fontsize"]|Increase Font Size: Joomla form field a11y_font; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_users/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|allowUserRegistration|["integer", "string"]|нет|[0, 1, "0", "1"]|Allow User Registration: Joomla form field allowUserRegistration; input is validated and filtered according to x-joomla-form.||
|new_usertype|["integer", "string"]|нет|"2"|New User Registration Group: Joomla form field new_usertype; input is validated and filtered according to x-joomla-form.||
|guest_usergroup|["integer", "string"]|нет|"1"|Guest User Group: Joomla form field guest_usergroup; input is validated and filtered according to x-joomla-form.||
|sendpassword|["integer", "string"]|нет|[0, 1, "0", "1"]|Send Password: Joomla form field sendpassword; input is validated and filtered according to x-joomla-form.||
|useractivation|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|New User Account Activation: Joomla form field useractivation; input is validated and filtered according to x-joomla-form.||
|mail_to_admin|["integer", "string"]|нет|[0, 1, "0", "1"]|Send Mail to Administrators: Joomla form field mail_to_admin; input is validated and filtered according to x-joomla-form.||
|captcha|["integer", "string"]|нет|""|Captcha: Joomla form field captcha; input is validated and filtered according to x-joomla-form.||
|frontend_userparams|["integer", "string"]|нет|[0, 1, "0", "1"]|Frontend User Parameters: Joomla form field frontend_userparams; input is validated and filtered according to x-joomla-form.||
|site_language|["integer", "string"]|нет|[0, 1, "0", "1"]|Frontend Language: Joomla form field site_language; input is validated and filtered according to x-joomla-form.|frontend_userparams:1|
|change_login_name|["integer", "string"]|нет|[0, 1, "0", "1"]|Change Username: Joomla form field change_login_name; input is validated and filtered according to x-joomla-form.||
|domains|"anyOf"|нет|""|Email Domains: Joomla form field domains; input is validated and filtered according to x-joomla-form.||
|reset_count|["integer", "string"]|нет|"10"|Maximum Reset Count: Joomla form field reset_count; input is validated and filtered according to x-joomla-form.||
|reset_time|["integer", "string"]|нет|"1"|Reset Time (hours): Joomla form field reset_time; input is validated and filtered according to x-joomla-form.||
|minimum_length|["integer", "string"]|нет|"12"|Minimum Password Length: Joomla form field minimum_length; input is validated and filtered according to x-joomla-form.||
|minimum_integers|["integer", "string"]|нет|"0"|Minimum Numbers: Joomla form field minimum_integers; input is validated and filtered according to x-joomla-form.||
|minimum_symbols|["integer", "string"]|нет|"0"|Minimum Symbols: Joomla form field minimum_symbols; input is validated and filtered according to x-joomla-form.||
|minimum_uppercase|["integer", "string"]|нет|"0"|Minimum Upper Case: Joomla form field minimum_uppercase; input is validated and filtered according to x-joomla-form.||
|minimum_lowercase|["integer", "string"]|нет|"0"|Minimum Lower Case: Joomla form field minimum_lowercase; input is validated and filtered according to x-joomla-form.||
|allowed_positions_frontend|"string"|нет|""|Allowed frontend module positions: When displaying the frontend Multi-factor Authentication page all modules will be hidden except those in the positions selected here.||
|frontend_show_title|["integer", "string"]|нет|[0, 1, "0", "1"]|Show title in frontend: Should I display a title in the frontend Multi-factor Authentication verification page? Please note that the title is always displayed in the backend. If you need to change the title please override the language key <code>COM_USERS_USER_MULTIFACTOR_AUTH</code> using the System, Manage, Language Overrides page of the site's backend.||
|allowed_positions_backend|"string"|нет|""|Allowed backend module positions: When displaying the backend Multi-factor Authentication page all modules will be hidden except those in the positions selected here. Please note that modules in the <code>title</code> position are always shown: this is required to show the backend page icon and title.||
|neverMFAUserGroups|["integer", "string"]|нет|""|Disable Multi-factor Authentication: Any user who belongs in <em>any</em> of the selected user groups will be exempt from Multi-factor Authentication. Even if they have set up Multi-factor Authentication methods they will not be asked to use them when they are logging in, nor will they be able to view them, remove them, or change their configuration.||
|forceMFAUserGroups|["integer", "string"]|нет|""|Enforce Multi-factor Authentication: Any user who belongs in <em>any</em> of the selected user groups will be required to enable Multi-factor Authentication before being able to use the site.||
|captive_template|["integer", "string"]|нет|""|Frontend template style: Choose the frontend template style to use in the Multi-factor Authentication page. Select "- Use Default -" to use the default site template style.||
|mfaonsilent|["integer", "string"]|нет|[0, 1, "0", "1"]|Multi-factor Authentication after silent login: Should the user have to go through Multi-factor Authentication after a silent user login? Silent logins are those which do not require a username and password e.g. the Remember Me feature, passkeys etc.||
|silentresponses|"string"|нет|"cookie, passwordless"|Silent login authentication response types (for experts): For experts. A comma–separated list of Joomla authentication response types which are considered silent logins. The default is <code>cookie</code> (the Remember Me feature) and <code>passwordless</code> (passkeys).|mfaonsilent:0|
|mfaredirectonlogin|["integer", "string"]|нет|[0, 1, "0", "1"]|Onboard new users: If the user has not yet set up Multi-factor Authentication and this option is enabled they will be redirected to the Multi-factor Authentication setup page or the custom URL you set up below. This is meant to be a simple way to let your users know that Multi-factor Authentication is an option on your site.||
|mfaredirecturl|"string"|нет|""|Custom redirection URL: If it's not empty redirects to this URL instead of the Multi-factor Authentication setup page when the option above is enabled. WARNING: This must be a URL inside your site. You cannot log in to an external link or to a different subdomain.|mfaredirectonlogin:1|
|mfatrycount|["integer", "string"]|нет|"10"|Maximum MFA tries: Joomla form field mfatrycount; input is validated and filtered according to x-joomla-form.||
|mfatrytime|["integer", "string"]|нет|"1"|MFA limit block time (in hours): Joomla form field mfatrytime; input is validated and filtered according to x-joomla-form.||
|save_history|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable Versions: Joomla form field save_history; input is validated and filtered according to x-joomla-form.||
|history_limit|["integer", "string"]|нет|"5"|Maximum Versions: Joomla form field history_limit; input is validated and filtered according to x-joomla-form.|save_history:1|
|mailSubjectPrefix|"string"|нет|""|Subject Prefix: Joomla form field mailSubjectPrefix; input is validated and filtered according to x-joomla-form.||
|mailBodySuffix|"string"|нет|""|Mailbody Suffix: Joomla form field mailBodySuffix; input is validated and filtered according to x-joomla-form.||
|custom_fields_enable|["integer", "string"]|нет|[0, 1, "0", "1"]|Edit Custom Fields: Joomla form field custom_fields_enable; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
