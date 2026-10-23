# com_languages: заполнение полей, Joomla 6.1.3

lang_code — тег языка, sef — сегмент URL, title_native — родное название.
Пути overrides/{site|administrator}/{lang_code} создаются для установленных языков.
ID override — строковая константа [A-Z0-9_]+. Запись: key/override; ответ: value.
Сохранение OverridesController читает app/lang_code из post input. ApiApplication
помещает параметры маршрута в post для POST, но в общий input для PATCH. Поэтому
POST получает правильный контекст, а PATCH не гарантирует его из одного route/JSON.
При неподдерживаемом сохранении использовать UI fallback, сохранив клиент/язык.
Поиск требует searchstring и searchtype=constant|value.
Для снимка 6.1.3 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/languages/content

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|lang_code|"string"|да|""|Language Tag: Enter the language tag – example: en-GB for English (en-GB). This should be the exact prefix used for the language installed or to be installed.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|title_native|"string"|да|""|Title in Native Language: Joomla form field title_native; input is validated and filtered according to x-joomla-form.||
|sef|"string"|да|""|URL Language Code: This Language Code will be included in the site URL. Note <em>the Language Code must be unique among all the languages</em>.||
|image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|sitename|"string"|нет|""|Custom Site Name: Joomla form field sitename; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/languages/content/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|lang_code|"string"|нет|""|Language Tag: Enter the language tag – example: en-GB for English (en-GB). This should be the exact prefix used for the language installed or to be installed.||
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|title_native|"string"|нет|""|Title in Native Language: Joomla form field title_native; input is validated and filtered according to x-joomla-form.||
|sef|"string"|нет|""|URL Language Code: This Language Code will be included in the site URL. Note <em>the Language Code must be unique among all the languages</em>.||
|image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|sitename|"string"|нет|""|Custom Site Name: Joomla form field sitename; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/languages/overrides/search

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|searchstring|"string"|да|""|searchstring: ||
|searchtype|"string"|да|["constant", "value"]|searchtype: ||
## REST POST /v1/languages/overrides/site/{lang_code}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|key|"string"|да|""|Language Constant: Joomla form field key; input is validated and filtered according to x-joomla-form.||
|override|"string"|нет|""|Text: Joomla form field override; input is validated and filtered according to x-joomla-form.||
|both|"boolean"|нет|""|For Both Locations: Joomla form field both; input is validated and filtered according to x-joomla-form.||
|searchstring|"string"|нет|""|Search Text: Joomla form field searchstring; input is validated and filtered according to x-joomla-form.||
|searchtype|"string"|нет|["constant", "value"]|Search For: Joomla form field searchtype; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/languages/overrides/site/{lang_code}/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|key|"string"|нет|""|Language Constant: Joomla form field key; input is validated and filtered according to x-joomla-form.||
|override|"string"|нет|""|Text: Joomla form field override; input is validated and filtered according to x-joomla-form.||
|both|"boolean"|нет|""|For Both Locations: Joomla form field both; input is validated and filtered according to x-joomla-form.||
|searchstring|"string"|нет|""|Search Text: Joomla form field searchstring; input is validated and filtered according to x-joomla-form.||
|searchtype|"string"|нет|["constant", "value"]|Search For: Joomla form field searchtype; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/languages/overrides/administrator/{lang_code}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|key|"string"|да|""|Language Constant: Joomla form field key; input is validated and filtered according to x-joomla-form.||
|override|"string"|нет|""|Text: Joomla form field override; input is validated and filtered according to x-joomla-form.||
|both|"boolean"|нет|""|For Both Locations: Joomla form field both; input is validated and filtered according to x-joomla-form.||
|searchstring|"string"|нет|""|Search Text: Joomla form field searchstring; input is validated and filtered according to x-joomla-form.||
|searchtype|"string"|нет|["constant", "value"]|Search For: Joomla form field searchtype; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/languages/overrides/administrator/{lang_code}/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|key|"string"|нет|""|Language Constant: Joomla form field key; input is validated and filtered according to x-joomla-form.||
|override|"string"|нет|""|Text: Joomla form field override; input is validated and filtered according to x-joomla-form.||
|both|"boolean"|нет|""|For Both Locations: Joomla form field both; input is validated and filtered according to x-joomla-form.||
|searchstring|"string"|нет|""|Search Text: Joomla form field searchstring; input is validated and filtered according to x-joomla-form.||
|searchtype|"string"|нет|["constant", "value"]|Search For: Joomla form field searchtype; input is validated and filtered according to x-joomla-form.||

## Инвентарь стандартных форм UI

## administrator/components/com_languages/forms/filter_installed.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|client_id|["integer", "string"]|нет|[0, 1, "0", "1"]|Select Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Installed Languages: Search in title and language tag.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "name ASC", "name DESC", "nativeName ASC", "nativeName DESC", "language ASC", "language DESC", "published ASC", "published DESC", "version ASC", "version DESC", "creationDate ASC", "creationDate DESC", "author ASC", "author DESC", "authorEmail ASC", "authorEmail DESC", "extension_id ASC", "extension_id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_languages/forms/filter_languages.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search: Search in title.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.published ASC", "a.published DESC", "a.title ASC", "a.title DESC", "a.title_native ASC", "a.title_native DESC", "a.lang_code ASC", "a.lang_code DESC", "a.sef ASC", "a.sef DESC", "a.image ASC", "a.image DESC", "a.access ASC", "a.access DESC", "l.home ASC", "l.home DESC", "a.lang_id ASC", "a.lang_id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_languages/forms/filter_overrides.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|language_client|"string"|нет|""|Select Language & Client: Joomla form field language_client; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search: Search constant or text.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "key ASC", "key DESC", "text ASC", "text DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_languages/forms/language.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|lang_id|["integer", "string"]|нет|"0"|ID: Joomla form field lang_id; input is validated and filtered according to x-joomla-form.||
|lang_code|"string"|да|""|Language Tag: Enter the language tag – example: en-GB for English (en-GB). This should be the exact prefix used for the language installed or to be installed.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|title_native|"string"|да|""|Title in Native Language: Joomla form field title_native; input is validated and filtered according to x-joomla-form.||
|sef|"string"|да|""|URL Language Code: This Language Code will be included in the site URL. Note <em>the Language Code must be unique among all the languages</em>.||
|image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, -2, "1", "0", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|sitename|"string"|нет|""|Custom Site Name: Joomla form field sitename; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_languages/forms/override.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|key|"string"|да|""|Language Constant: Joomla form field key; input is validated and filtered according to x-joomla-form.||
|override|"string"|нет|""|Text: Joomla form field override; input is validated and filtered according to x-joomla-form.||
|both|"boolean"|нет|""|For Both Locations: Joomla form field both; input is validated and filtered according to x-joomla-form.||
|searchstring|"string"|нет|""|Search Text: Joomla form field searchstring; input is validated and filtered according to x-joomla-form.||
|searchtype|"string"|нет|["constant", "value"]|Search For: Joomla form field searchtype; input is validated and filtered according to x-joomla-form.||
|id|"string"|нет|""|id: Joomla form field id; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_languages/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|site|"string"|нет|""|site: Joomla form field site; input is validated and filtered according to x-joomla-form.||
|administrator|"string"|нет|""|administrator: Joomla form field administrator; input is validated and filtered according to x-joomla-form.||
