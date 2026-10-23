# com_messages: заполнение полей, Joomla 6.2.0

См. форму и схему ответа endpoint.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/messages

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|user_id_to|["integer", "string"]|да|"0"|Recipient: Joomla form field user_id_to; input is validated and filtered according to x-joomla-form.||
|subject|"string"|да|""|Subject: Joomla form field subject; input is validated and filtered according to x-joomla-form.||
|message|"string"|да|""|Message: Joomla form field message; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/messages/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|user_id_to|["integer", "string"]|нет|"0"|Recipient: Joomla form field user_id_to; input is validated and filtered according to x-joomla-form.||
|subject|"string"|нет|""|Subject: Joomla form field subject; input is validated and filtered according to x-joomla-form.||
|message|"string"|нет|""|Message: Joomla form field message; input is validated and filtered according to x-joomla-form.||

## Инвентарь стандартных форм UI

## administrator/components/com_messages/forms/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|lock|["integer", "string"]|нет|[0, 1, "0", "1"]|Lock Inbox: Joomla form field lock; input is validated and filtered according to x-joomla-form.||
|mail_on_new|["integer", "string"]|нет|[0, 1, "0", "1"]|Email New Messages: Joomla form field mail_on_new; input is validated and filtered according to x-joomla-form.||
|auto_purge|["integer", "string"]|нет|"7"|Auto-delete Messages (days): Joomla form field auto_purge; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_messages/forms/filter_messages.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Messages: Search in message subject and description.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.subject ASC", "a.subject DESC", "a.state ASC", "a.state DESC", "a.user_id_from ASC", "a.user_id_from DESC", "a.date_time ASC", "a.date_time DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"5"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_messages/forms/message.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|user_id_to|["integer", "string"]|да|"0"|Recipient: Joomla form field user_id_to; input is validated and filtered according to x-joomla-form.||
|subject|"string"|да|""|Subject: Joomla form field subject; input is validated and filtered according to x-joomla-form.||
|message|"string"|да|""|Message: Joomla form field message; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_messages/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
