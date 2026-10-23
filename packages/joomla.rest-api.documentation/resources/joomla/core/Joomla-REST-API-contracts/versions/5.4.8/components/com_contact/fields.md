# com_contact: заполнение полей, Joomla 5.4.8

name/catid/язык/доступ относятся к карточке контакта. state означает регион
и является СТРОКОЙ; состояние публикации — published.
POST contacts/form/{id} отправляет сообщение, а не создаёт контакт. Поля:
contact_name/contact_email/contact_subject/contact_message/contact_email_copy.
Состав зависит от contact-плагинов и captcha. Автоматический повтор может
отправить письмо повторно; успешный ответ операции не является карточкой контакта.
Для снимка 5.4.8 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/contacts/form/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|contact_name|"string"|да|""|Name: Joomla form field contact_name; input is validated and filtered according to x-joomla-form.||
|contact_email|"string"|да|""|Email: Joomla form field contact_email; input is validated and filtered according to x-joomla-form.||
|contact_subject|"string"|да|""|Subject: Joomla form field contact_subject; input is validated and filtered according to x-joomla-form.||
|contact_message|"string"|да|""|Message: Joomla form field contact_message; input is validated and filtered according to x-joomla-form.||
|contact_email_copy|"string"|нет|""|Send a copy to yourself: Joomla form field contact_email_copy; input is validated and filtered according to x-joomla-form.||
|captcha|"string"|нет|""|Captcha: Joomla form field captcha; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
## REST POST /v1/contacts

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|да|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|user_id|["integer", "string"]|нет|""|Linked User: Joomla form field user_id; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|catid|"anyOf"|да|""|catid: Existing category ID, or category title (optionally #new#Title) for inline creation when the owner model's canCreateCategory permission allows it. Prefer a known ID unless creation is intended.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|misc|"string"|нет|""|Miscellaneous Information: Joomla form field misc; input is validated and filtered according to x-joomla-form.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|featured|["integer", "string"]|нет|[0, 1, "0", "1"]|Featured: Joomla form field featured; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|con_position|"string"|нет|""|Position: Joomla form field con_position; input is validated and filtered according to x-joomla-form.||
|email_to|"string"|нет|""|Email: Joomla form field email_to; input is validated and filtered according to x-joomla-form.||
|address|"string"|нет|""|Address: Joomla form field address; input is validated and filtered according to x-joomla-form.||
|suburb|"string"|нет|""|City or Suburb: Joomla form field suburb; input is validated and filtered according to x-joomla-form.||
|state|"string"|нет|""|State or County: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|postcode|"string"|нет|""|Postal/ZIP Code: Joomla form field postcode; input is validated and filtered according to x-joomla-form.||
|country|"string"|нет|""|Country: Joomla form field country; input is validated and filtered according to x-joomla-form.||
|telephone|"string"|нет|""|Telephone: Joomla form field telephone; input is validated and filtered according to x-joomla-form.||
|mobile|"string"|нет|""|Mobile: Joomla form field mobile; input is validated and filtered according to x-joomla-form.||
|fax|"string"|нет|""|Fax: Joomla form field fax; input is validated and filtered according to x-joomla-form.||
|webpage|"string"|нет|""|Website: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|sortname1|"string"|нет|""|First Sort Field: Joomla form field sortname1; input is validated and filtered according to x-joomla-form.||
|sortname2|"string"|нет|""|Second Sort Field: Joomla form field sortname2; input is validated and filtered according to x-joomla-form.||
|sortname3|"string"|нет|""|Third Sort Field: Joomla form field sortname3; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_contact_category|"string"|нет|["", "hide", "show_no_link", "show_with_link"]|Category: Joomla form field show_contact_category; input is validated and filtered according to x-joomla-form.||
|params.show_contact_list|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Select List: Joomla form field show_contact_list; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_info|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Information: Joomla form field show_info; input is validated and filtered according to x-joomla-form.||
|params.show_name|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Name: Joomla form field show_name; input is validated and filtered according to x-joomla-form.|show_info:1|
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
|params.show_misc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Miscellaneous Information: Joomla form field show_misc; input is validated and filtered according to x-joomla-form.||
|params.allow_vcard|["integer", "string"]|нет|["", 0, 1, "0", "1"]|vCard: Joomla form field allow_vcard; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.articles_display_num|["integer", "string"]|нет|["", 5, 10, 15, 20, 25, 30, 50, 75, 100, 150, 200, 250, 300, 0, "5", "10", "15", "20", "25", "30", "50", "75", "100", "150", "200", "250", "300", "0"]|# Articles to List: Joomla form field articles_display_num; input is validated and filtered according to x-joomla-form.||
|params.show_profile|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Profile: Joomla form field show_profile; input is validated and filtered according to x-joomla-form.||
|params.show_user_custom_fields|"array"|нет|""|User Custom Field Groups: Joomla form field show_user_custom_fields; input is validated and filtered according to x-joomla-form.||
|params.contact_layout|"string"|нет|""|Layout: Joomla form field contact_layout; input is validated and filtered according to x-joomla-form.||
|params.show_links|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Links: Joomla form field show_links; input is validated and filtered according to x-joomla-form.||
|params.linka_name|"string"|нет|""|Link A Label: Joomla form field linka_name; input is validated and filtered according to x-joomla-form.||
|params.linka|"string"|нет|""|Link A URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkb_name|"string"|нет|""|Link B Label: Joomla form field linkb_name; input is validated and filtered according to x-joomla-form.||
|params.linkb|"string"|нет|""|Link B URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkc_name|"string"|нет|""|Link C Label: Joomla form field linkc_name; input is validated and filtered according to x-joomla-form.||
|params.linkc|"string"|нет|""|Link C URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkd_name|"string"|нет|""|Link D Label: Joomla form field linkd_name; input is validated and filtered according to x-joomla-form.||
|params.linkd|"string"|нет|""|Link D URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linke_name|"string"|нет|""|Link E Label: Joomla form field linke_name; input is validated and filtered according to x-joomla-form.||
|params.linke|"string"|нет|""|Link E URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.show_email_form|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Form: Joomla form field show_email_form; input is validated and filtered according to x-joomla-form.||
|params.show_email_copy|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Send Copy to Submitter: Joomla form field show_email_copy; input is validated and filtered according to x-joomla-form.||
|params.validate_session|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Session Check: Joomla form field validate_session; input is validated and filtered according to x-joomla-form.||
|params.custom_reply|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Custom Reply: Stops Joomla from sending the email, allowing for Plugins to handle integration with other systems.||
|params.redirect|"string"|нет|""|Contact Redirect URL: Joomla form field redirect; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
## REST PATCH /v1/contacts/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|user_id|["integer", "string"]|нет|""|Linked User: Joomla form field user_id; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|catid|"anyOf"|нет|""|catid: Existing category ID, or category title (optionally #new#Title) for inline creation when the owner model's canCreateCategory permission allows it. Prefer a known ID unless creation is intended.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|misc|"string"|нет|""|Miscellaneous Information: Joomla form field misc; input is validated and filtered according to x-joomla-form.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|featured|["integer", "string"]|нет|[0, 1, "0", "1"]|Featured: Joomla form field featured; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|con_position|"string"|нет|""|Position: Joomla form field con_position; input is validated and filtered according to x-joomla-form.||
|email_to|"string"|нет|""|Email: Joomla form field email_to; input is validated and filtered according to x-joomla-form.||
|address|"string"|нет|""|Address: Joomla form field address; input is validated and filtered according to x-joomla-form.||
|suburb|"string"|нет|""|City or Suburb: Joomla form field suburb; input is validated and filtered according to x-joomla-form.||
|state|"string"|нет|""|State or County: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|postcode|"string"|нет|""|Postal/ZIP Code: Joomla form field postcode; input is validated and filtered according to x-joomla-form.||
|country|"string"|нет|""|Country: Joomla form field country; input is validated and filtered according to x-joomla-form.||
|telephone|"string"|нет|""|Telephone: Joomla form field telephone; input is validated and filtered according to x-joomla-form.||
|mobile|"string"|нет|""|Mobile: Joomla form field mobile; input is validated and filtered according to x-joomla-form.||
|fax|"string"|нет|""|Fax: Joomla form field fax; input is validated and filtered according to x-joomla-form.||
|webpage|"string"|нет|""|Website: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|sortname1|"string"|нет|""|First Sort Field: Joomla form field sortname1; input is validated and filtered according to x-joomla-form.||
|sortname2|"string"|нет|""|Second Sort Field: Joomla form field sortname2; input is validated and filtered according to x-joomla-form.||
|sortname3|"string"|нет|""|Third Sort Field: Joomla form field sortname3; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_contact_category|"string"|нет|["", "hide", "show_no_link", "show_with_link"]|Category: Joomla form field show_contact_category; input is validated and filtered according to x-joomla-form.||
|params.show_contact_list|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Select List: Joomla form field show_contact_list; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_info|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Information: Joomla form field show_info; input is validated and filtered according to x-joomla-form.||
|params.show_name|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Name: Joomla form field show_name; input is validated and filtered according to x-joomla-form.|show_info:1|
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
|params.show_misc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Miscellaneous Information: Joomla form field show_misc; input is validated and filtered according to x-joomla-form.||
|params.allow_vcard|["integer", "string"]|нет|["", 0, 1, "0", "1"]|vCard: Joomla form field allow_vcard; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.articles_display_num|["integer", "string"]|нет|["", 5, 10, 15, 20, 25, 30, 50, 75, 100, 150, 200, 250, 300, 0, "5", "10", "15", "20", "25", "30", "50", "75", "100", "150", "200", "250", "300", "0"]|# Articles to List: Joomla form field articles_display_num; input is validated and filtered according to x-joomla-form.||
|params.show_profile|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Profile: Joomla form field show_profile; input is validated and filtered according to x-joomla-form.||
|params.show_user_custom_fields|"array"|нет|""|User Custom Field Groups: Joomla form field show_user_custom_fields; input is validated and filtered according to x-joomla-form.||
|params.contact_layout|"string"|нет|""|Layout: Joomla form field contact_layout; input is validated and filtered according to x-joomla-form.||
|params.show_links|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Links: Joomla form field show_links; input is validated and filtered according to x-joomla-form.||
|params.linka_name|"string"|нет|""|Link A Label: Joomla form field linka_name; input is validated and filtered according to x-joomla-form.||
|params.linka|"string"|нет|""|Link A URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkb_name|"string"|нет|""|Link B Label: Joomla form field linkb_name; input is validated and filtered according to x-joomla-form.||
|params.linkb|"string"|нет|""|Link B URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkc_name|"string"|нет|""|Link C Label: Joomla form field linkc_name; input is validated and filtered according to x-joomla-form.||
|params.linkc|"string"|нет|""|Link C URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkd_name|"string"|нет|""|Link D Label: Joomla form field linkd_name; input is validated and filtered according to x-joomla-form.||
|params.linkd|"string"|нет|""|Link D URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linke_name|"string"|нет|""|Link E Label: Joomla form field linke_name; input is validated and filtered according to x-joomla-form.||
|params.linke|"string"|нет|""|Link E URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.show_email_form|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Form: Joomla form field show_email_form; input is validated and filtered according to x-joomla-form.||
|params.show_email_copy|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Send Copy to Submitter: Joomla form field show_email_copy; input is validated and filtered according to x-joomla-form.||
|params.validate_session|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Session Check: Joomla form field validate_session; input is validated and filtered according to x-joomla-form.||
|params.custom_reply|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Custom Reply: Stops Joomla from sending the email, allowing for Plugins to handle integration with other systems.||
|params.redirect|"string"|нет|""|Contact Redirect URL: Joomla form field redirect; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||

## Инвентарь стандартных форм UI

## administrator/components/com_contact/forms/category.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## administrator/components/com_contact/forms/contact.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|name|"string"|да|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|user_id|["integer", "string"]|нет|""|Linked User: Joomla form field user_id; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|catid|["integer", "string"]|да|""|Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|misc|"string"|нет|""|Miscellaneous Information: Joomla form field misc; input is validated and filtered according to x-joomla-form.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|modified|"string"|нет|""|Modified Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|featured|["integer", "string"]|нет|[0, 1, "0", "1"]|Featured: Joomla form field featured; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Joomla form field tags; input is validated and filtered according to x-joomla-form.||
|image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|con_position|"string"|нет|""|Position: Joomla form field con_position; input is validated and filtered according to x-joomla-form.||
|email_to|"string"|нет|""|Email: Joomla form field email_to; input is validated and filtered according to x-joomla-form.||
|address|"string"|нет|""|Address: Joomla form field address; input is validated and filtered according to x-joomla-form.||
|suburb|"string"|нет|""|City or Suburb: Joomla form field suburb; input is validated and filtered according to x-joomla-form.||
|state|"string"|нет|""|State or County: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|postcode|"string"|нет|""|Postal/ZIP Code: Joomla form field postcode; input is validated and filtered according to x-joomla-form.||
|country|"string"|нет|""|Country: Joomla form field country; input is validated and filtered according to x-joomla-form.||
|telephone|"string"|нет|""|Telephone: Joomla form field telephone; input is validated and filtered according to x-joomla-form.||
|mobile|"string"|нет|""|Mobile: Joomla form field mobile; input is validated and filtered according to x-joomla-form.||
|fax|"string"|нет|""|Fax: Joomla form field fax; input is validated and filtered according to x-joomla-form.||
|webpage|"string"|нет|""|Website: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|sortname1|"string"|нет|""|First Sort Field: Joomla form field sortname1; input is validated and filtered according to x-joomla-form.||
|sortname2|"string"|нет|""|Second Sort Field: Joomla form field sortname2; input is validated and filtered according to x-joomla-form.||
|sortname3|"string"|нет|""|Third Sort Field: Joomla form field sortname3; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_contact_category|"string"|нет|["", "hide", "show_no_link", "show_with_link"]|Category: Joomla form field show_contact_category; input is validated and filtered according to x-joomla-form.||
|params.show_contact_list|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Select List: Joomla form field show_contact_list; input is validated and filtered according to x-joomla-form.||
|params.show_tags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|params.show_info|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Information: Joomla form field show_info; input is validated and filtered according to x-joomla-form.||
|params.show_name|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Name: Joomla form field show_name; input is validated and filtered according to x-joomla-form.|show_info:1|
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
|params.show_misc|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Miscellaneous Information: Joomla form field show_misc; input is validated and filtered according to x-joomla-form.||
|params.allow_vcard|["integer", "string"]|нет|["", 0, 1, "0", "1"]|vCard: Joomla form field allow_vcard; input is validated and filtered according to x-joomla-form.||
|params.show_articles|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|params.articles_display_num|["integer", "string"]|нет|["", 5, 10, 15, 20, 25, 30, 50, 75, 100, 150, 200, 250, 300, 0, "5", "10", "15", "20", "25", "30", "50", "75", "100", "150", "200", "250", "300", "0"]|# Articles to List: Joomla form field articles_display_num; input is validated and filtered according to x-joomla-form.||
|params.show_profile|["integer", "string"]|нет|["", 0, 1, "0", "1"]|User Profile: Joomla form field show_profile; input is validated and filtered according to x-joomla-form.||
|params.show_user_custom_fields|"array"|нет|""|User Custom Field Groups: Joomla form field show_user_custom_fields; input is validated and filtered according to x-joomla-form.||
|params.contact_layout|"string"|нет|""|Layout: Joomla form field contact_layout; input is validated and filtered according to x-joomla-form.||
|params.show_links|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Links: Joomla form field show_links; input is validated and filtered according to x-joomla-form.||
|params.linka_name|"string"|нет|""|Link A Label: Joomla form field linka_name; input is validated and filtered according to x-joomla-form.||
|params.linka|"string"|нет|""|Link A URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkb_name|"string"|нет|""|Link B Label: Joomla form field linkb_name; input is validated and filtered according to x-joomla-form.||
|params.linkb|"string"|нет|""|Link B URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkc_name|"string"|нет|""|Link C Label: Joomla form field linkc_name; input is validated and filtered according to x-joomla-form.||
|params.linkc|"string"|нет|""|Link C URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linkd_name|"string"|нет|""|Link D Label: Joomla form field linkd_name; input is validated and filtered according to x-joomla-form.||
|params.linkd|"string"|нет|""|Link D URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.linke_name|"string"|нет|""|Link E Label: Joomla form field linke_name; input is validated and filtered according to x-joomla-form.||
|params.linke|"string"|нет|""|Link E URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|params.show_email_form|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Contact Form: Joomla form field show_email_form; input is validated and filtered according to x-joomla-form.||
|params.show_email_copy|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Send Copy to Submitter: Joomla form field show_email_copy; input is validated and filtered according to x-joomla-form.||
|params.validate_session|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Session Check: Joomla form field validate_session; input is validated and filtered according to x-joomla-form.||
|params.custom_reply|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Custom Reply: Stops Joomla from sending the email, allowing for Plugins to handle integration with other systems.||
|params.redirect|"string"|нет|""|Contact Redirect URL: Joomla form field redirect; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_contact/forms/filter_contacts.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Contacts: Search in contact name and alias. Prefix with ID: to search for a contact ID.||
|filter.featured|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Featured: Joomla form field featured; input is validated and filtered according to x-joomla-form.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.category_id|"array"|нет|""|Category: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.tag|"array"|нет|[]|Tags: Joomla form field tag; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.featured ASC", "a.featured DESC", "a.published ASC", "a.published DESC", "a.name ASC", "a.name DESC", "category_title ASC", "category_title DESC", "ul.name ASC", "ul.name DESC", "access_level ASC", "access_level DESC", "association ASC", "association DESC", "language_title ASC", "language_title DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_contact/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|contact_layout|"string"|нет|""|Choose a Layout: Joomla form field contact_layout; input is validated and filtered according to x-joomla-form.||
|show_contact_category|"string"|нет|["hide", "show_no_link", "show_with_link"]|Contact Category: Joomla form field show_contact_category; input is validated and filtered according to x-joomla-form.||
|save_history|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable Versions: Joomla form field save_history; input is validated and filtered according to x-joomla-form.||
|history_limit|["integer", "string"]|нет|"10"|Maximum Versions: Joomla form field history_limit; input is validated and filtered according to x-joomla-form.|save_history:1|
|show_contact_list|["integer", "string"]|нет|[0, 1, "0", "1"]|Contact Select List: Joomla form field show_contact_list; input is validated and filtered according to x-joomla-form.||
|show_tags|["integer", "string"]|нет|[0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|show_info|["integer", "string"]|нет|[0, 1, "0", "1"]|Contact Information: Joomla form field show_info; input is validated and filtered according to x-joomla-form.||
|show_name|["integer", "string"]|нет|[0, 1, "0", "1"]|Name: Joomla form field show_name; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_position|["integer", "string"]|нет|[0, 1, "0", "1"]|Contact's Position: Joomla form field show_position; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_email|["integer", "string"]|нет|[0, 1, "0", "1"]|Email: Joomla form field show_email; input is validated and filtered according to x-joomla-form.|show_info:1|
|add_mailto_link|["integer", "string"]|нет|[0, 1, "0", "1"]|Add Mailto: Link: Joomla form field add_mailto_link; input is validated and filtered according to x-joomla-form.|show_info:1[AND]show_email:1|
|show_street_address|["integer", "string"]|нет|[0, 1, "0", "1"]|Street Address: Joomla form field show_street_address; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_suburb|["integer", "string"]|нет|[0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_TOWN-SUBURB_LABEL: Joomla form field show_suburb; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_state|["integer", "string"]|нет|[0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_STATE-COUNTY_LABEL: Joomla form field show_state; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_postcode|["integer", "string"]|нет|[0, 1, "0", "1"]|COM_CONTACT_FIELD_PARAMS_POST-ZIP_CODE_LABEL: Joomla form field show_postcode; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_country|["integer", "string"]|нет|[0, 1, "0", "1"]|Country: Joomla form field show_country; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_telephone|["integer", "string"]|нет|[0, 1, "0", "1"]|Telephone: Joomla form field show_telephone; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_mobile|["integer", "string"]|нет|[0, 1, "0", "1"]|Mobile Phone: Joomla form field show_mobile; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_fax|["integer", "string"]|нет|[0, 1, "0", "1"]|Fax: Joomla form field show_fax; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_webpage|["integer", "string"]|нет|[0, 1, "0", "1"]|Webpage: Joomla form field show_webpage; input is validated and filtered according to x-joomla-form.|show_info:1|
|show_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Image: Joomla form field show_image; input is validated and filtered according to x-joomla-form.|show_info:1|
|image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.|show_info:1[AND]show_image:1|
|show_misc|["integer", "string"]|нет|[0, 1, "0", "1"]|Miscellaneous Information: Joomla form field show_misc; input is validated and filtered according to x-joomla-form.||
|allow_vcard|["integer", "string"]|нет|[0, 1, "0", "1"]|vCard: Joomla form field allow_vcard; input is validated and filtered according to x-joomla-form.||
|show_articles|["integer", "string"]|нет|[0, 1, "0", "1"]|User Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|articles_display_num|"string"|нет|["use_contact", "5", "10", "15", "20", "25", "30", "50", "75", "100", "150", "200", "250", "300", "0"]|# Articles to List: Joomla form field articles_display_num; input is validated and filtered according to x-joomla-form.|show_articles:1|
|show_profile|["integer", "string"]|нет|[0, 1, "0", "1"]|User Profile: Joomla form field show_profile; input is validated and filtered according to x-joomla-form.||
|show_user_custom_fields|"array"|нет|""|User Custom Field Groups: Joomla form field show_user_custom_fields; input is validated and filtered according to x-joomla-form.||
|show_links|["integer", "string"]|нет|[0, 1, "0", "1"]|Contact Links: Joomla form field show_links; input is validated and filtered according to x-joomla-form.||
|linka_name|"string"|нет|""|Link A Label: Joomla form field linka_name; input is validated and filtered according to x-joomla-form.|show_links:1|
|linkb_name|"string"|нет|""|Link B Label: Joomla form field linkb_name; input is validated and filtered according to x-joomla-form.|show_links:1|
|linkc_name|"string"|нет|""|Link C Label: Joomla form field linkc_name; input is validated and filtered according to x-joomla-form.|show_links:1|
|linkd_name|"string"|нет|""|Link D Label: Joomla form field linkd_name; input is validated and filtered according to x-joomla-form.|show_links:1|
|linke_name|"string"|нет|""|Link E Label: Joomla form field linke_name; input is validated and filtered according to x-joomla-form.|show_links:1|
|contact_icons|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Settings: Joomla form field contact_icons; input is validated and filtered according to x-joomla-form.||
|icon_address|"string"|нет|""|Custom Address Icon: Joomla form field icon_address; input is validated and filtered according to x-joomla-form.|contact_icons:0|
|icon_email|"string"|нет|""|Custom Email Icon: Joomla form field icon_email; input is validated and filtered according to x-joomla-form.|contact_icons:0|
|icon_telephone|"string"|нет|""|Custom Telephone Icon: Joomla form field icon_telephone; input is validated and filtered according to x-joomla-form.|contact_icons:0|
|icon_mobile|"string"|нет|""|Custom Mobile Icon: Joomla form field icon_mobile; input is validated and filtered according to x-joomla-form.|contact_icons:0|
|icon_fax|"string"|нет|""|Custom Fax Icon: Joomla form field icon_fax; input is validated and filtered according to x-joomla-form.|contact_icons:0|
|icon_webpage|"string"|нет|""|Custom Webpage Icon: Joomla form field icon_webpage; input is validated and filtered according to x-joomla-form.|contact_icons:0|
|icon_misc|"string"|нет|""|Custom Misc Icon: Joomla form field icon_misc; input is validated and filtered according to x-joomla-form.|contact_icons:0|
|category_layout|"string"|нет|""|Choose a Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|show_category_title|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|show_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|show_description_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|maxLevel|["integer", "string"]|нет|[-1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|show_no_contacts|["integer", "string"]|нет|[0, 1, "0", "1"]|No Contacts Message: Joomla form field show_no_contacts; input is validated and filtered according to x-joomla-form.||
|show_category_heading_title_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Heading: Joomla form field show_category_heading_title_text; input is validated and filtered according to x-joomla-form.||
|show_subcat_desc|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.|maxLevel:-1,1,2,3,4,5|
|show_empty_categories|["integer", "string"]|нет|[0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.|maxLevel:-1,1,2,3,4,5|
|show_cat_items|["integer", "string"]|нет|[0, 1, "0", "1"]|# Contacts in Category: Joomla form field show_cat_items; input is validated and filtered according to x-joomla-form.||
|show_cat_tags|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Tags: Joomla form field show_cat_tags; input is validated and filtered according to x-joomla-form.||
|show_base_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Top Level Category Description: Joomla form field show_base_description; input is validated and filtered according to x-joomla-form.||
|maxLevelcat|["integer", "string"]|нет|[-1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevelcat; input is validated and filtered according to x-joomla-form.||
|show_subcat_desc_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc_cat; input is validated and filtered according to x-joomla-form.|maxLevelcat:-1,1,2,3,4,5|
|show_empty_categories_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories_cat; input is validated and filtered according to x-joomla-form.|maxLevelcat:-1,1,2,3,4,5|
|show_cat_items_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|# Contacts in Category: Joomla form field show_cat_items_cat; input is validated and filtered according to x-joomla-form.||
|filter_field|["integer", "string"]|нет|[0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|show_pagination_limit|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|show_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|show_image_heading|["integer", "string"]|нет|[0, 1, "0", "1"]|Image: Joomla form field show_image_heading; input is validated and filtered according to x-joomla-form.||
|show_position_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Position: Joomla form field show_position_headings; input is validated and filtered according to x-joomla-form.|show_headings:1|
|show_email_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Email: Joomla form field show_email_headings; input is validated and filtered according to x-joomla-form.|show_headings:1|
|show_telephone_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Phone: Joomla form field show_telephone_headings; input is validated and filtered according to x-joomla-form.|show_headings:1|
|show_mobile_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Mobile: Joomla form field show_mobile_headings; input is validated and filtered according to x-joomla-form.|show_headings:1|
|show_fax_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Fax: Joomla form field show_fax_headings; input is validated and filtered according to x-joomla-form.|show_headings:1|
|show_suburb_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|City or Suburb: Joomla form field show_suburb_headings; input is validated and filtered according to x-joomla-form.|show_headings:1|
|show_state_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|State or County: Joomla form field show_state_headings; input is validated and filtered according to x-joomla-form.|show_headings:1|
|show_country_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Country: Joomla form field show_country_headings; input is validated and filtered according to x-joomla-form.|show_headings:1|
|show_pagination|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|show_pagination_results|["integer", "string"]|нет|[0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.|show_pagination:1,2|
|contacts_display_num|["integer", "string"]|нет|[5, 10, 15, 20, 25, 30, 50, 100, 0, "5", "10", "15", "20", "25", "30", "50", "100", "0"]|# Contacts to List: Joomla form field contacts_display_num; input is validated and filtered according to x-joomla-form.||
|initial_sort|"string"|нет|["name", "sortname", "ordering", "featuredordering"]|Sort By: Joomla form field initial_sort; input is validated and filtered according to x-joomla-form.||
|captcha|["integer", "string"]|нет|""|Allow Captcha on Contact: Joomla form field captcha; input is validated and filtered according to x-joomla-form.||
|show_email_form|["integer", "string"]|нет|[0, 1, "0", "1"]|Contact Form: Joomla form field show_email_form; input is validated and filtered according to x-joomla-form.||
|show_email_copy|["integer", "string"]|нет|[0, 1, "0", "1"]|Send Copy to Submitter: Joomla form field show_email_copy; input is validated and filtered according to x-joomla-form.|show_email_form:1|
|banned_email|"string"|нет|""|Banned Email Address: Separate multiple email addresses with a semicolon. Emails from a complete domain can be banned by using @example.com or a partial domain using ple.com.|show_email_form:1|
|banned_subject|"string"|нет|""|Banned Subject: Separate multiple subjects with a semicolon.|show_email_form:1|
|banned_text|"string"|нет|""|Banned Text: Separate multiple words with a semicolon.|show_email_form:1|
|validate_session|["integer", "string"]|нет|[0, 1, "0", "1"]|Session Check: Joomla form field validate_session; input is validated and filtered according to x-joomla-form.|show_email_form:1|
|custom_reply|["integer", "string"]|нет|[0, 1, "0", "1"]|Custom Reply: Stops Joomla from sending the email, allowing for Plugins to handle integration with other systems.|show_email_form:1|
|redirect|"string"|нет|""|Contact Redirect URL: Joomla form field redirect; input is validated and filtered according to x-joomla-form.|show_email_form:1|
|show_feed_link|["integer", "string"]|нет|[0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
|sef_ids|["integer", "string"]|нет|[0, 1, "0", "1"]|Remove IDs from URLs: Joomla form field sef_ids; input is validated and filtered according to x-joomla-form.||
|custom_fields_enable|["integer", "string"]|нет|[0, 1, "0", "1"]|Edit Custom Fields: Joomla form field custom_fields_enable; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
