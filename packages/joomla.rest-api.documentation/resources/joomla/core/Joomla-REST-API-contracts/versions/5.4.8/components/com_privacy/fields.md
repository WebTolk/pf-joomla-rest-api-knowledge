# com_privacy: заполнение полей, Joomla 5.4.8

Списки/элементы запросов и согласий, а также экспорт требуют core.admin
на com_privacy в API-контроллерах. Удаление consent не имеет REST-маршрута.
Экспорт требует request_type=export и подтверждённый status=1; иначе модель
не возвращает данные, представление вызывает RouteNotFoundException.
Результат формируется privacy-плагинами; REST export не равнозначен файлу
экспорта в админке. Подробности фактической сериализации см. в схеме ответа.
Для снимка 5.4.8 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/privacy/requests

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|email|"string"|да|""|Email: The email address of the individual owning the information being requested.||
|request_type|"string"|нет|["export", "remove"]|Request Type: Joomla form field request_type; input is validated and filtered according to x-joomla-form.||

## Инвентарь стандартных форм UI

## administrator/components/com_privacy/forms/filter_consents.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Requests: Search in username. Prefix with Name: to search for a name. Prefix with ID: to search for a consent ID. Prefix with UID: to search for a User ID.||
|filter.state|["integer", "string"]|нет|["", 1, 0, -1, "1", "0", "-1"]|State of Consents: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.subject|"string"|нет|""|Subject: Joomla form field subject; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["a.state ASC", "a.state DESC", "u.name ASC", "u.name DESC", "u.username ASC", "u.username DESC", "a.user_id ASC", "a.user_id DESC", "a.subject ASC", "a.subject DESC", "a.created ASC", "a.created DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_privacy/forms/filter_requests.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Requests: Search in requestor email address. Prefix with ID: to search for a request ID.||
|filter.status|"string"|нет|""|Status: Joomla form field status; input is validated and filtered according to x-joomla-form.||
|filter.request_type|"string"|нет|""|Request Type: Joomla form field request_type; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.email ASC", "a.email DESC", "a.request_type ASC", "a.request_type DESC", "a.requested_at ASC", "a.requested_at DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_privacy/forms/request.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|email|"string"|да|""|Email: The email address of the individual owning the information being requested.||
|status|["integer", "string"]|нет|[0, -1, 1, 2, "0", "-1", "1", "2"]|Request Status: Joomla form field status; input is validated and filtered according to x-joomla-form.||
|request_type|"string"|нет|["export", "remove"]|Request Type: Joomla form field request_type; input is validated and filtered according to x-joomla-form.||
|id|["integer", "string"]|нет|"0"|ID: Record number in the database.||
## administrator/components/com_privacy/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|notify|["integer", "string"]|нет|"14"|Days To Consider Request Urgent: Show a notification when there are requests older than the specified number of days.||
