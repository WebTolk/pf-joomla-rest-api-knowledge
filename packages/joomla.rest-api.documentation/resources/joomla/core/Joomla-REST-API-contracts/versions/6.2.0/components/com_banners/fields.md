# com_banners: заполнение полей, Joomla 6.2.0

См. форму и схему ответа endpoint.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/banners

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|да|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|catid|["integer", "string"]|да|""|Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|type|["integer", "string"]|нет|[0, 1, "0", "1"]|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|custombannercode|"string"|нет|""|Custom Code: Joomla form field custombannercode; input is validated and filtered according to x-joomla-form.||
|clickurl|"string"|нет|""|Click URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|sticky|["integer", "string"]|нет|[0, 1, "0", "1"]|Pinned: If one or more Banners in a Category are pinned, they will take priority over Banners that are not pinned. For example, if two Banners in a Category are pinned and a third Banner is not pinned, the third Banner will not display if the module setting is 'Pinned, Randomise'. Only the two pinned Banners will display.||
|imptotal|["integer", "string"]|нет|"0"|Max. Impressions: Joomla form field imptotal; input is validated and filtered according to x-joomla-form.||
|impmade|["integer", "string"]|нет|"0"|Total Impressions: Joomla form field impmade; input is validated and filtered according to x-joomla-form.||
|clicks|["integer", "string"]|нет|"0"|Total Clicks: Joomla form field clicks; input is validated and filtered according to x-joomla-form.||
|cid|["integer", "string"]|нет|""|Client: Joomla form field cid; input is validated and filtered according to x-joomla-form.||
|purchase_type|["integer", "string"]|нет|[-1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Purchase Type: Joomla form field purchase_type; input is validated and filtered according to x-joomla-form.||
|track_impressions|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Impressions: Joomla form field track_impressions; input is validated and filtered according to x-joomla-form.||
|track_clicks|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Clicks: Joomla form field track_clicks; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|own_prefix|["integer", "string"]|нет|[0, 1, "0", "1"]|Use Own Prefix: Joomla form field own_prefix; input is validated and filtered according to x-joomla-form.||
|metakey_prefix|"string"|нет|""|Keyword Prefix: When matching Keywords, only search for Keywords with this prefix (improves performance).||
|params|"object"|нет|""|params: ||
|params.imageurl|"string"|нет|""|Image: Joomla form field imageurl; input is validated and filtered according to x-joomla-form.||
|params.width|["integer", "string"]|нет|""|Width: Joomla form field width; input is validated and filtered according to x-joomla-form.||
|params.height|["integer", "string"]|нет|""|Height: Joomla form field height; input is validated and filtered according to x-joomla-form.||
|params.alt|"string"|нет|""|Alt Text: Joomla form field alt; input is validated and filtered according to x-joomla-form.||
|bannercode|"string"|нет|""|Custom Code: Joomla form field bannercode; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/banners/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|catid|["integer", "string"]|нет|""|Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|type|["integer", "string"]|нет|[0, 1, "0", "1"]|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|custombannercode|"string"|нет|""|Custom Code: Joomla form field custombannercode; input is validated and filtered according to x-joomla-form.||
|clickurl|"string"|нет|""|Click URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|sticky|["integer", "string"]|нет|[0, 1, "0", "1"]|Pinned: If one or more Banners in a Category are pinned, they will take priority over Banners that are not pinned. For example, if two Banners in a Category are pinned and a third Banner is not pinned, the third Banner will not display if the module setting is 'Pinned, Randomise'. Only the two pinned Banners will display.||
|imptotal|["integer", "string"]|нет|"0"|Max. Impressions: Joomla form field imptotal; input is validated and filtered according to x-joomla-form.||
|impmade|["integer", "string"]|нет|"0"|Total Impressions: Joomla form field impmade; input is validated and filtered according to x-joomla-form.||
|clicks|["integer", "string"]|нет|"0"|Total Clicks: Joomla form field clicks; input is validated and filtered according to x-joomla-form.||
|cid|["integer", "string"]|нет|""|Client: Joomla form field cid; input is validated and filtered according to x-joomla-form.||
|purchase_type|["integer", "string"]|нет|[-1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Purchase Type: Joomla form field purchase_type; input is validated and filtered according to x-joomla-form.||
|track_impressions|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Impressions: Joomla form field track_impressions; input is validated and filtered according to x-joomla-form.||
|track_clicks|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Clicks: Joomla form field track_clicks; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|own_prefix|["integer", "string"]|нет|[0, 1, "0", "1"]|Use Own Prefix: Joomla form field own_prefix; input is validated and filtered according to x-joomla-form.||
|metakey_prefix|"string"|нет|""|Keyword Prefix: When matching Keywords, only search for Keywords with this prefix (improves performance).||
|params|"object"|нет|""|params: ||
|params.imageurl|"string"|нет|""|Image: Joomla form field imageurl; input is validated and filtered according to x-joomla-form.||
|params.width|["integer", "string"]|нет|""|Width: Joomla form field width; input is validated and filtered according to x-joomla-form.||
|params.height|["integer", "string"]|нет|""|Height: Joomla form field height; input is validated and filtered according to x-joomla-form.||
|params.alt|"string"|нет|""|Alt Text: Joomla form field alt; input is validated and filtered according to x-joomla-form.||
|bannercode|"string"|нет|""|Custom Code: Joomla form field bannercode; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/banners/clients

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|да|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|contact|"string"|да|""|Contact Name: Joomla form field contact; input is validated and filtered according to x-joomla-form.||
|email|"string"|нет|""|Contact Email: Joomla form field email; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|purchase_type|["integer", "string"]|нет|[-1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Purchase Type: Joomla form field purchase_type; input is validated and filtered according to x-joomla-form.||
|track_impressions|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Impressions: Joomla form field track_impressions; input is validated and filtered according to x-joomla-form.||
|track_clicks|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Clicks: Joomla form field track_clicks; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|own_prefix|["integer", "string"]|нет|[0, 1, "0", "1"]|Use Own Prefix: Joomla form field own_prefix; input is validated and filtered according to x-joomla-form.||
|metakey_prefix|"string"|нет|""|Keyword Prefix: When matching Keywords, only search for Keywords with this prefix (improves performance).||
|extrainfo|"string"|нет|""|Additional Information: Joomla form field extrainfo; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/banners/clients/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|contact|"string"|нет|""|Contact Name: Joomla form field contact; input is validated and filtered according to x-joomla-form.||
|email|"string"|нет|""|Contact Email: Joomla form field email; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|purchase_type|["integer", "string"]|нет|[-1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Purchase Type: Joomla form field purchase_type; input is validated and filtered according to x-joomla-form.||
|track_impressions|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Impressions: Joomla form field track_impressions; input is validated and filtered according to x-joomla-form.||
|track_clicks|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Clicks: Joomla form field track_clicks; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|own_prefix|["integer", "string"]|нет|[0, 1, "0", "1"]|Use Own Prefix: Joomla form field own_prefix; input is validated and filtered according to x-joomla-form.||
|metakey_prefix|"string"|нет|""|Keyword Prefix: When matching Keywords, only search for Keywords with this prefix (improves performance).||
|extrainfo|"string"|нет|""|Additional Information: Joomla form field extrainfo; input is validated and filtered according to x-joomla-form.||

## Инвентарь стандартных форм UI

## administrator/components/com_banners/forms/banner.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|name|"string"|да|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|catid|["integer", "string"]|да|""|Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|type|["integer", "string"]|нет|[0, 1, "0", "1"]|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|custombannercode|"string"|нет|""|Custom Code: Joomla form field custombannercode; input is validated and filtered according to x-joomla-form.||
|clickurl|"string"|нет|""|Click URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|modified|"string"|нет|""|Modified Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|sticky|["integer", "string"]|нет|[0, 1, "0", "1"]|Pinned: If one or more Banners in a Category are pinned, they will take priority over Banners that are not pinned. For example, if two Banners in a Category are pinned and a third Banner is not pinned, the third Banner will not display if the module setting is 'Pinned, Randomise'. Only the two pinned Banners will display.||
|imptotal|["integer", "string"]|нет|"0"|Max. Impressions: Joomla form field imptotal; input is validated and filtered according to x-joomla-form.||
|impmade|["integer", "string"]|нет|"0"|Total Impressions: Joomla form field impmade; input is validated and filtered according to x-joomla-form.||
|clicks|["integer", "string"]|нет|"0"|Total Clicks: Joomla form field clicks; input is validated and filtered according to x-joomla-form.||
|cid|["integer", "string"]|нет|""|Client: Joomla form field cid; input is validated and filtered according to x-joomla-form.||
|purchase_type|["integer", "string"]|нет|[-1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Purchase Type: Joomla form field purchase_type; input is validated and filtered according to x-joomla-form.||
|track_impressions|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Impressions: Joomla form field track_impressions; input is validated and filtered according to x-joomla-form.||
|track_clicks|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Clicks: Joomla form field track_clicks; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|own_prefix|["integer", "string"]|нет|[0, 1, "0", "1"]|Use Own Prefix: Joomla form field own_prefix; input is validated and filtered according to x-joomla-form.||
|metakey_prefix|"string"|нет|""|Keyword Prefix: When matching Keywords, only search for Keywords with this prefix (improves performance).||
|params|"object"|нет|""|params: ||
|params.imageurl|"string"|нет|""|Image: Joomla form field imageurl; input is validated and filtered according to x-joomla-form.||
|params.width|["integer", "string"]|нет|""|Width: Joomla form field width; input is validated and filtered according to x-joomla-form.||
|params.height|["integer", "string"]|нет|""|Height: Joomla form field height; input is validated and filtered according to x-joomla-form.||
|params.alt|"string"|нет|""|Alt Text: Joomla form field alt; input is validated and filtered according to x-joomla-form.||
|bannercode|"string"|нет|""|Custom Code: Joomla form field bannercode; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_banners/forms/category.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## administrator/components/com_banners/forms/client.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|name|"string"|да|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|contact|"string"|да|""|Contact Name: Joomla form field contact; input is validated and filtered according to x-joomla-form.||
|email|"string"|нет|""|Contact Email: Joomla form field email; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|purchase_type|["integer", "string"]|нет|[-1, 1, 2, 3, 4, 5, "-1", "1", "2", "3", "4", "5"]|Purchase Type: Joomla form field purchase_type; input is validated and filtered according to x-joomla-form.||
|track_impressions|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Impressions: Joomla form field track_impressions; input is validated and filtered according to x-joomla-form.||
|track_clicks|["integer", "string"]|нет|[-1, 0, 1, "-1", "0", "1"]|Track Clicks: Joomla form field track_clicks; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|own_prefix|["integer", "string"]|нет|[0, 1, "0", "1"]|Use Own Prefix: Joomla form field own_prefix; input is validated and filtered according to x-joomla-form.||
|metakey_prefix|"string"|нет|""|Keyword Prefix: When matching Keywords, only search for Keywords with this prefix (improves performance).||
|extrainfo|"string"|нет|""|Additional Information: Joomla form field extrainfo; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_banners/forms/download.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|compressed|["integer", "string"]|нет|[0, 1, "0", "1"]|Compressed: Joomla form field compressed; input is validated and filtered according to x-joomla-form.||
|basename|"string"|нет|""|File Name: File name pattern which can have<br>__SITE__ for the site name<br>__CATID__ for the category ID<br>__CATNAME__ for the category name<br>__CLIENTID__ for the client ID<br>__CLIENTNAME__ for the client name<br>__TYPE__ for the type<br>__TYPENAME__ for the type name<br>__BEGIN__ for the begin date<br>__END__ for the end date.||
## administrator/components/com_banners/forms/filter_banners.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Banners: Search in banner name and alias. Prefix with ID: to search for a banner ID.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.category_id|["integer", "string"]|нет|""|Category: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|filter.client_id|"string"|нет|""|Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.state ASC", "a.state DESC", "a.name ASC", "a.name DESC", "category_title ASC", "category_title DESC", "a.sticky ASC", "a.sticky DESC", "client_name ASC", "client_name DESC", "impmade ASC", "impmade DESC", "clicks ASC", "clicks DESC", "a.language ASC", "a.language DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_banners/forms/filter_clients.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Clients: Search in client name. Prefix with ID: to search for a client ID.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.purchase_type|["integer", "string"]|нет|["", 1, 2, 3, 4, 5, "1", "2", "3", "4", "5"]|Type: Joomla form field purchase_type; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.state ASC", "a.state DESC", "a.name ASC", "a.name DESC", "a.contact ASC", "a.contact DESC", "a.purchase_type ASC", "a.purchase_type DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_banners/forms/filter_tracks.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Tracks: Search in track name and track client name.||
|filter.category_id|["integer", "string"]|нет|""|Category: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|filter.client_id|"string"|нет|""|Client: Joomla form field client_id; input is validated and filtered according to x-joomla-form.||
|filter.type|["integer", "string"]|нет|["", 1, 2, "1", "2"]|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|filter.begin|"string"|нет|""|Begin Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|filter.end|"string"|нет|""|End Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "b.name ASC", "b.name DESC", "cl.name ASC", "cl.name DESC", "a.track_type ASC", "a.track_type DESC", "a.count ASC", "a.count DESC", "a.track_date ASC", "a.track_date DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"5"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_banners/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|purchase_type|["integer", "string"]|нет|[1, 2, 3, 4, 5, "1", "2", "3", "4", "5"]|Purchase Type: Joomla form field purchase_type; input is validated and filtered according to x-joomla-form.||
|track_impressions|["integer", "string"]|нет|[0, 1, "0", "1"]|Track Impressions: Joomla form field track_impressions; input is validated and filtered according to x-joomla-form.||
|track_robots_impressions|["integer", "string"]|нет|[0, 1, "0", "1"]|Include impressions by Search Engines: Joomla form field track_robots_impressions; input is validated and filtered according to x-joomla-form.||
|track_clicks|["integer", "string"]|нет|[0, 1, "0", "1"]|Track Clicks: Joomla form field track_clicks; input is validated and filtered according to x-joomla-form.||
|metakey_prefix|"string"|нет|""|Keyword Prefix: When matching Keywords, only search for Keywords with this prefix (improves performance).||
|save_history|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable Versions: Joomla form field save_history; input is validated and filtered according to x-joomla-form.||
|history_limit|["integer", "string"]|нет|"10"|Maximum Versions: Joomla form field history_limit; input is validated and filtered according to x-joomla-form.|save_history:1|
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
