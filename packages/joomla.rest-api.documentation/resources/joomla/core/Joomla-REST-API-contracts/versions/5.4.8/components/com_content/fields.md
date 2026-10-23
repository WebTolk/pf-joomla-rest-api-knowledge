# com_content: заполнение полей, Joomla 5.4.8

catid — ID категории записи; category в ответе — отношение, не ключ записи catid.
Для создания черновика явно передавать state=0: default XML равен 1.
Для исходного текста PATCH использовать introtext/fulltext. articletext — редакторское
поле с readmore; на PATCH оно может быть перекрыто догруженными колонками.
GET text обработан контентными плагинами и не является надёжным raw HTML.
Использовать сохранённый исходник, актуальную contenthistory.version_data либо
разрешённую форму UI. images/urls/metadata/attribs — вложенные структуры.
created_by и metadata.author различаются; API-пользователь не обязательно автор.
Доступность state зависит от workflow и ACL. schemaorg и languageAssociations
условны: зависят от плагинов и многоязычности.
Для снимка 5.4.8 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/content/articles

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|articletext|"string"|нет|""|Article Text: Joomla form field articletext; input is validated and filtered according to x-joomla-form.||
|catid|"anyOf"|да|""|catid: Existing category ID, or category title (optionally #new#Title) for inline creation when the owner model's canCreateCategory permission allows it. Prefer a known ID unless creation is intended.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|featured_up|"string"|нет|""|Start Featured: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|featured:1|
|featured_down|"string"|нет|""|Finish Featured: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|featured:1|
|ordering|["integer", "string"]|нет|"0"|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|featured|["integer", "string"]|нет|[0, 1, "0", "1"]|Featured: Joomla form field featured; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|attribs|"object"|нет|""|attribs: ||
|attribs.article_layout|"string"|нет|""|Layout: Joomla form field article_layout; input is validated and filtered according to x-joomla-form.||
|attribs.show_title|"string"|нет|""|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|attribs.link_titles|"string"|нет|""|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.||
|attribs.show_tags|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|attribs.show_intro|"string"|нет|""|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|attribs.info_block_position|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Position of Article Info: Joomla form field info_block_position; input is validated and filtered according to x-joomla-form.||
|attribs.info_block_show_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Article Info Title: Joomla form field info_block_show_title; input is validated and filtered according to x-joomla-form.||
|attribs.show_category|"string"|нет|""|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|attribs.link_category|"string"|нет|""|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|attribs.show_parent_category|"string"|нет|""|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|attribs.link_parent_category|"string"|нет|""|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|attribs.show_associations|["integer", "string"]|нет|""|Associations: Joomla form field show_associations; input is validated and filtered according to x-joomla-form.||
|attribs.flags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Use Image Flags: Joomla form field flags; input is validated and filtered according to x-joomla-form.|show_associations:1|
|attribs.show_author|"string"|нет|""|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|attribs.link_author|"string"|нет|""|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|attribs.show_create_date|"string"|нет|""|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_modify_date|"string"|нет|""|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_publish_date|"string"|нет|""|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_item_navigation|"string"|нет|""|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|attribs.show_vote|"string"|нет|""|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|attribs.show_hits|"string"|нет|""|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|attribs.show_noauth|"string"|нет|""|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|attribs.urls_position|["integer", "string"]|нет|["", 0, 1, -1, "0", "1", "-1"]|Positioning of the Links: Joomla form field urls_position; input is validated and filtered according to x-joomla-form.||
|attribs.alternative_readmore|"string"|нет|""|Read More Text: Add a custom text instead of Read More.||
|attribs.article_page_title|"string"|нет|""|Browser Page Title: Joomla form field article_page_title; input is validated and filtered according to x-joomla-form.||
|attribs.show_publishing_options|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Publishing Options: Joomla form field show_publishing_options; input is validated and filtered according to x-joomla-form.||
|attribs.show_article_options|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Article Options: Joomla form field show_article_options; input is validated and filtered according to x-joomla-form.||
|attribs.show_urls_images_backend|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Administrator Images and Links: Joomla form field show_urls_images_backend; input is validated and filtered according to x-joomla-form.||
|attribs.show_urls_images_frontend|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Frontend Images and Links: Joomla form field show_urls_images_frontend; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_intro|"string"|нет|""|Intro Image: Joomla form field image_intro; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_intro_alt; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.float_intro|"string"|нет|""|Image Class: You can add any CSS class for your own styling ideas.<br>For image position use for example float-start and float-end.||
|images.image_intro_caption|"string"|нет|""|Caption: Joomla form field image_intro_caption; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext|"string"|нет|""|Full Article Image: Joomla form field image_fulltext; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_fulltext_alt; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.float_fulltext|"string"|нет|""|Image Class: You can add any CSS class for your own styling ideas.<br>For image position use for example float-start and float-end.||
|images.image_fulltext_caption|"string"|нет|""|Caption: Joomla form field image_fulltext_caption; input is validated and filtered according to x-joomla-form.||
|urls|"object"|нет|""|urls: ||
|urls.urla|"string"|нет|""|Link A: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlatext|"string"|нет|""|Link A Text: Joomla form field urlatext; input is validated and filtered according to x-joomla-form.||
|urls.targeta|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targeta; input is validated and filtered according to x-joomla-form.||
|urls.urlb|"string"|нет|""|Link B: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlbtext|"string"|нет|""|Link B Text: Joomla form field urlbtext; input is validated and filtered according to x-joomla-form.||
|urls.targetb|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targetb; input is validated and filtered according to x-joomla-form.||
|urls.urlc|"string"|нет|""|Link C: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlctext|"string"|нет|""|Link C Text: Joomla form field urlctext; input is validated and filtered according to x-joomla-form.||
|urls.targetc|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targetc; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Content Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
|introtext|"string"|нет|""|Intro Text: Joomla form field introtext; input is validated and filtered according to x-joomla-form.||
|fulltext|"string"|нет|""|Full text: Joomla form field fulltext; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
## REST PATCH /v1/content/articles/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|articletext|"string"|нет|""|Article Text: Joomla form field articletext; input is validated and filtered according to x-joomla-form.||
|catid|"anyOf"|нет|""|catid: Existing category ID, or category title (optionally #new#Title) for inline creation when the owner model's canCreateCategory permission allows it. Prefer a known ID unless creation is intended.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|featured_up|"string"|нет|""|Start Featured: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|featured:1|
|featured_down|"string"|нет|""|Finish Featured: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|featured:1|
|ordering|["integer", "string"]|нет|"0"|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|featured|["integer", "string"]|нет|[0, 1, "0", "1"]|Featured: Joomla form field featured; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|attribs|"object"|нет|""|attribs: ||
|attribs.article_layout|"string"|нет|""|Layout: Joomla form field article_layout; input is validated and filtered according to x-joomla-form.||
|attribs.show_title|"string"|нет|""|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|attribs.link_titles|"string"|нет|""|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.||
|attribs.show_tags|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|attribs.show_intro|"string"|нет|""|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|attribs.info_block_position|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Position of Article Info: Joomla form field info_block_position; input is validated and filtered according to x-joomla-form.||
|attribs.info_block_show_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Article Info Title: Joomla form field info_block_show_title; input is validated and filtered according to x-joomla-form.||
|attribs.show_category|"string"|нет|""|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|attribs.link_category|"string"|нет|""|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|attribs.show_parent_category|"string"|нет|""|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|attribs.link_parent_category|"string"|нет|""|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|attribs.show_associations|["integer", "string"]|нет|""|Associations: Joomla form field show_associations; input is validated and filtered according to x-joomla-form.||
|attribs.flags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Use Image Flags: Joomla form field flags; input is validated and filtered according to x-joomla-form.|show_associations:1|
|attribs.show_author|"string"|нет|""|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|attribs.link_author|"string"|нет|""|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|attribs.show_create_date|"string"|нет|""|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_modify_date|"string"|нет|""|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_publish_date|"string"|нет|""|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_item_navigation|"string"|нет|""|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|attribs.show_vote|"string"|нет|""|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|attribs.show_hits|"string"|нет|""|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|attribs.show_noauth|"string"|нет|""|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|attribs.urls_position|["integer", "string"]|нет|["", 0, 1, -1, "0", "1", "-1"]|Positioning of the Links: Joomla form field urls_position; input is validated and filtered according to x-joomla-form.||
|attribs.alternative_readmore|"string"|нет|""|Read More Text: Add a custom text instead of Read More.||
|attribs.article_page_title|"string"|нет|""|Browser Page Title: Joomla form field article_page_title; input is validated and filtered according to x-joomla-form.||
|attribs.show_publishing_options|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Publishing Options: Joomla form field show_publishing_options; input is validated and filtered according to x-joomla-form.||
|attribs.show_article_options|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Article Options: Joomla form field show_article_options; input is validated and filtered according to x-joomla-form.||
|attribs.show_urls_images_backend|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Administrator Images and Links: Joomla form field show_urls_images_backend; input is validated and filtered according to x-joomla-form.||
|attribs.show_urls_images_frontend|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Frontend Images and Links: Joomla form field show_urls_images_frontend; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_intro|"string"|нет|""|Intro Image: Joomla form field image_intro; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_intro_alt; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.float_intro|"string"|нет|""|Image Class: You can add any CSS class for your own styling ideas.<br>For image position use for example float-start and float-end.||
|images.image_intro_caption|"string"|нет|""|Caption: Joomla form field image_intro_caption; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext|"string"|нет|""|Full Article Image: Joomla form field image_fulltext; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_fulltext_alt; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.float_fulltext|"string"|нет|""|Image Class: You can add any CSS class for your own styling ideas.<br>For image position use for example float-start and float-end.||
|images.image_fulltext_caption|"string"|нет|""|Caption: Joomla form field image_fulltext_caption; input is validated and filtered according to x-joomla-form.||
|urls|"object"|нет|""|urls: ||
|urls.urla|"string"|нет|""|Link A: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlatext|"string"|нет|""|Link A Text: Joomla form field urlatext; input is validated and filtered according to x-joomla-form.||
|urls.targeta|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targeta; input is validated and filtered according to x-joomla-form.||
|urls.urlb|"string"|нет|""|Link B: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlbtext|"string"|нет|""|Link B Text: Joomla form field urlbtext; input is validated and filtered according to x-joomla-form.||
|urls.targetb|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targetb; input is validated and filtered according to x-joomla-form.||
|urls.urlc|"string"|нет|""|Link C: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlctext|"string"|нет|""|Link C Text: Joomla form field urlctext; input is validated and filtered according to x-joomla-form.||
|urls.targetc|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targetc; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Content Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
|introtext|"string"|нет|""|Intro Text: Joomla form field introtext; input is validated and filtered according to x-joomla-form.||
|fulltext|"string"|нет|""|Full text: Joomla form field fulltext; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||

## Инвентарь стандартных форм UI

## administrator/components/com_content/forms/article.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|articletext|"string"|нет|""|Article Text: Joomla form field articletext; input is validated and filtered according to x-joomla-form.||
|catid|["integer", "string"]|да|""|Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Joomla form field tags; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|modified|"string"|нет|""|Modified Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|featured_up|"string"|нет|""|Start Featured: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|featured:1|
|featured_down|"string"|нет|""|Finish Featured: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.|featured:1|
|ordering|["integer", "string"]|нет|"0"|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|featured|["integer", "string"]|нет|[0, 1, "0", "1"]|Featured: Joomla form field featured; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|JFIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|attribs|"object"|нет|""|attribs: ||
|attribs.article_layout|"string"|нет|""|Layout: Joomla form field article_layout; input is validated and filtered according to x-joomla-form.||
|attribs.show_title|"string"|нет|""|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|attribs.link_titles|"string"|нет|""|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.||
|attribs.show_tags|["integer", "string"]|нет|["", 1, 0, "1", "0"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|attribs.show_intro|"string"|нет|""|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|attribs.info_block_position|["integer", "string"]|нет|["", 0, 1, 2, "0", "1", "2"]|Position of Article Info: Joomla form field info_block_position; input is validated and filtered according to x-joomla-form.||
|attribs.info_block_show_title|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Article Info Title: Joomla form field info_block_show_title; input is validated and filtered according to x-joomla-form.||
|attribs.show_category|"string"|нет|""|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|attribs.link_category|"string"|нет|""|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.||
|attribs.show_parent_category|"string"|нет|""|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|attribs.link_parent_category|"string"|нет|""|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.||
|attribs.show_associations|["integer", "string"]|нет|""|Associations: Joomla form field show_associations; input is validated and filtered according to x-joomla-form.||
|attribs.flags|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Use Image Flags: Joomla form field flags; input is validated and filtered according to x-joomla-form.|show_associations:1|
|attribs.show_author|"string"|нет|""|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|attribs.link_author|"string"|нет|""|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.||
|attribs.show_create_date|"string"|нет|""|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_modify_date|"string"|нет|""|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_publish_date|"string"|нет|""|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|attribs.show_item_navigation|"string"|нет|""|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|attribs.show_vote|"string"|нет|""|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|attribs.show_hits|"string"|нет|""|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|attribs.show_noauth|"string"|нет|""|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|attribs.urls_position|["integer", "string"]|нет|["", 0, 1, -1, "0", "1", "-1"]|Positioning of the Links: Joomla form field urls_position; input is validated and filtered according to x-joomla-form.||
|attribs.alternative_readmore|"string"|нет|""|Read More Text: Add a custom text instead of Read More.||
|attribs.article_page_title|"string"|нет|""|Browser Page Title: Joomla form field article_page_title; input is validated and filtered according to x-joomla-form.||
|attribs.show_publishing_options|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Publishing Options: Joomla form field show_publishing_options; input is validated and filtered according to x-joomla-form.||
|attribs.show_article_options|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Article Options: Joomla form field show_article_options; input is validated and filtered according to x-joomla-form.||
|attribs.show_urls_images_backend|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Administrator Images and Links: Joomla form field show_urls_images_backend; input is validated and filtered according to x-joomla-form.||
|attribs.show_urls_images_frontend|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Frontend Images and Links: Joomla form field show_urls_images_frontend; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_intro|"string"|нет|""|Intro Image: Joomla form field image_intro; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_intro_alt; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.float_intro|"string"|нет|""|Image Class: You can add any CSS class for your own styling ideas.<br>For image position use for example float-start and float-end.||
|images.image_intro_caption|"string"|нет|""|Caption: Joomla form field image_intro_caption; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext|"string"|нет|""|Full Article Image: Joomla form field image_fulltext; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_fulltext_alt; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.float_fulltext|"string"|нет|""|Image Class: You can add any CSS class for your own styling ideas.<br>For image position use for example float-start and float-end.||
|images.image_fulltext_caption|"string"|нет|""|Caption: Joomla form field image_fulltext_caption; input is validated and filtered according to x-joomla-form.||
|urls|"object"|нет|""|urls: ||
|urls.urla|"string"|нет|""|Link A: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlatext|"string"|нет|""|Link A Text: Joomla form field urlatext; input is validated and filtered according to x-joomla-form.||
|urls.targeta|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targeta; input is validated and filtered according to x-joomla-form.||
|urls.urlb|"string"|нет|""|Link B: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlbtext|"string"|нет|""|Link B Text: Joomla form field urlbtext; input is validated and filtered according to x-joomla-form.||
|urls.targetb|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targetb; input is validated and filtered according to x-joomla-form.||
|urls.urlc|"string"|нет|""|Link C: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|urls.urlctext|"string"|нет|""|Link C Text: Joomla form field urlctext; input is validated and filtered according to x-joomla-form.||
|urls.targetc|["integer", "string"]|нет|["", 0, 1, 2, 3, "0", "1", "2", "3"]|URL Target Window: Joomla form field targetc; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Content Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
|introtext|"string"|нет|""|Intro Text: Joomla form field introtext; input is validated and filtered according to x-joomla-form.||
|fulltext|"string"|нет|""|Full text: Joomla form field fulltext; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_content/forms/category.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|params|"object"|нет|""|params: ||
|params.workflow_id|["integer", "string"]|да|"use_default"|Workflows: SQL selector returns numeric IDs; explicit inheritance/default tokens may also be strings.||
## administrator/components/com_content/forms/filter_articles.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Articles: Search in title, alias and note. Prefix with ID: or AUTHOR: or CONTENT: to search for an article ID, article author or search in article content. Prefix with CHECKEDOUT: to search for content checked out by a specified user.||
|filter.featured|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Featured: Joomla form field featured; input is validated and filtered according to x-joomla-form.||
|filter.stage|["integer", "string"]|нет|""|- Select Stage -: Dynamic workflow option: numeric ID or a static inheritance/default token from x-options.||
|filter.published|"string"|нет|""|- Select Status -: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.category_id|"array"|нет|""|Category: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|filter.access|"array"|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.author_id|"array"|нет|""|- Select Author -: Joomla form field author_id; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.checked_out|["integer", "string"]|нет|["", 0, -1, "0", "-1"]|Checked Out: Joomla form field checked_out; input is validated and filtered according to x-joomla-form.||
|filter.tag|"array"|нет|[]|Tags: Joomla form field tag; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "ws.title ASC", "ws.title DESC", "a.featured ASC", "a.featured DESC", "a.state ASC", "a.state DESC", "a.title ASC", "a.title DESC", "category_title ASC", "category_title DESC", "a.access ASC", "a.access DESC", "a.created_by ASC", "a.created_by DESC", "association ASC", "association DESC", "language ASC", "language DESC", "a.created ASC", "a.created DESC", "a.modified ASC", "a.modified DESC", "a.publish_up ASC", "a.publish_up DESC", "a.publish_down ASC", "a.publish_down DESC", "a.hits ASC", "a.hits DESC", "rating_count ASC", "rating_count DESC", "rating ASC", "rating DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_content/forms/filter_featured.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Articles: Search in title, alias and note. Prefix with ID: or AUTHOR: or CONTENT: to search for an article ID, article author or search in article content. Prefix with CHECKEDOUT: to search for content checked out by a specified user.||
|filter.stage|["integer", "string"]|нет|""|- Select Stage -: Dynamic workflow option: numeric ID or a static inheritance/default token from x-options.||
|filter.published|"string"|нет|""|- Select Status -: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.category_id|"array"|нет|""|Category: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|filter.access|"array"|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.author_id|"array"|нет|""|- Select Author -: Joomla form field author_id; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.tag|"array"|нет|[]|Tags: Joomla form field tag; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "fp.ordering ASC", "fp.ordering DESC", "ws.title ASC", "ws.title DESC", "a.state ASC", "a.state DESC", "a.title ASC", "a.title DESC", "category_title ASC", "category_title DESC", "a.access ASC", "a.access DESC", "a.created_by ASC", "a.created_by DESC", "a.publish_up ASC", "a.publish_up DESC", "a.publish_down ASC", "a.publish_down DESC", "language ASC", "language DESC", "a.created ASC", "a.created DESC", "a.hits ASC", "a.hits DESC", "rating_count ASC", "rating_count DESC", "rating ASC", "rating DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_content/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|article_layout|"string"|нет|""|Choose a Layout: Joomla form field article_layout; input is validated and filtered according to x-joomla-form.||
|show_title|["integer", "string"]|нет|[0, 1, "0", "1"]|Title: Joomla form field show_title; input is validated and filtered according to x-joomla-form.||
|link_titles|["integer", "string"]|нет|[0, 1, "0", "1"]|Linked Titles: Joomla form field link_titles; input is validated and filtered according to x-joomla-form.|show_title:1|
|show_intro|["integer", "string"]|нет|[0, 1, "0", "1"]|Intro Text: Joomla form field show_intro; input is validated and filtered according to x-joomla-form.||
|info_block_position|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Position of Article Info: Joomla form field info_block_position; input is validated and filtered according to x-joomla-form.||
|info_block_show_title|["integer", "string"]|нет|[0, 1, "0", "1"]|Article Info Title: Joomla form field info_block_show_title; input is validated and filtered according to x-joomla-form.||
|show_category|["integer", "string"]|нет|[0, 1, "0", "1"]|Category: Joomla form field show_category; input is validated and filtered according to x-joomla-form.||
|link_category|["integer", "string"]|нет|[0, 1, "0", "1"]|Link Category: Joomla form field link_category; input is validated and filtered according to x-joomla-form.|show_category:1|
|show_parent_category|["integer", "string"]|нет|[0, 1, "0", "1"]|Parent Category: Joomla form field show_parent_category; input is validated and filtered according to x-joomla-form.||
|link_parent_category|["integer", "string"]|нет|[0, 1, "0", "1"]|Link Parent Category: Joomla form field link_parent_category; input is validated and filtered according to x-joomla-form.|show_parent_category:1|
|show_associations|["integer", "string"]|нет|[0, 1, "0", "1"]|Associations: Joomla form field show_associations; input is validated and filtered according to x-joomla-form.||
|flags|["integer", "string"]|нет|[0, 1, "0", "1"]|Use Image Flags: Joomla form field flags; input is validated and filtered according to x-joomla-form.|show_associations:1|
|show_author|["integer", "string"]|нет|[0, 1, "0", "1"]|Author: Joomla form field show_author; input is validated and filtered according to x-joomla-form.||
|link_author|["integer", "string"]|нет|[0, 1, "0", "1"]|Link to Author's Contact Page: Joomla form field link_author; input is validated and filtered according to x-joomla-form.|show_author:1|
|show_create_date|["integer", "string"]|нет|[0, 1, "0", "1"]|Create Date: Joomla form field show_create_date; input is validated and filtered according to x-joomla-form.||
|show_modify_date|["integer", "string"]|нет|[0, 1, "0", "1"]|Modify Date: Joomla form field show_modify_date; input is validated and filtered according to x-joomla-form.||
|show_publish_date|["integer", "string"]|нет|[0, 1, "0", "1"]|Publish Date: Joomla form field show_publish_date; input is validated and filtered according to x-joomla-form.||
|show_item_navigation|["integer", "string"]|нет|[0, 1, "0", "1"]|Navigation: Joomla form field show_item_navigation; input is validated and filtered according to x-joomla-form.||
|show_vote|["integer", "string"]|нет|"0"|Voting: Joomla form field show_vote; input is validated and filtered according to x-joomla-form.||
|show_readmore|["integer", "string"]|нет|[0, 1, "0", "1"]|&quot;Read More&quot; Link: Joomla form field show_readmore; input is validated and filtered according to x-joomla-form.||
|show_readmore_title|["integer", "string"]|нет|[0, 1, "0", "1"]|Read More with Title: Joomla form field show_readmore_title; input is validated and filtered according to x-joomla-form.|show_readmore:1|
|readmore_limit|["integer", "string"]|нет|"100"|Read More Limit (characters): Joomla form field readmore_limit; input is validated and filtered according to x-joomla-form.|show_readmore:1[AND]show_readmore_title:1|
|show_tags|["integer", "string"]|нет|[0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|record_hits|["integer", "string"]|нет|[0, 1, "0", "1"]|Record Hits: Joomla form field record_hits; input is validated and filtered according to x-joomla-form.||
|show_hits|["integer", "string"]|нет|[0, 1, "0", "1"]|Hits: Joomla form field show_hits; input is validated and filtered according to x-joomla-form.||
|show_noauth|["integer", "string"]|нет|[0, 1, "0", "1"]|Unauthorised Links: If set to Yes, links to registered content will be shown even if you are not logged-in. You will need to log in to access the full item.||
|urls_position|["integer", "string"]|нет|[0, 1, -1, "0", "1", "-1"]|Positioning of the Links: Joomla form field urls_position; input is validated and filtered according to x-joomla-form.||
|captcha|["integer", "string"]|нет|""|Allow Captcha on submit: Joomla form field captcha; input is validated and filtered according to x-joomla-form.||
|show_publishing_options|["integer", "string"]|нет|[0, 1, "0", "1"]|Publishing Options: Joomla form field show_publishing_options; input is validated and filtered according to x-joomla-form.||
|show_article_options|["integer", "string"]|нет|[0, 1, "0", "1"]|Article Options: Joomla form field show_article_options; input is validated and filtered according to x-joomla-form.||
|show_configure_edit_options|["integer", "string"]|нет|[0, 1, "0", "1"]|Edit Screen Options: Joomla form field show_configure_edit_options; input is validated and filtered according to x-joomla-form.||
|show_permissions|["integer", "string"]|нет|[0, 1, "0", "1"]|Article Permissions: Joomla form field show_permissions; input is validated and filtered according to x-joomla-form.||
|show_associations_edit|["integer", "string"]|нет|[0, 1, "0", "1"]|Multilingual Associations: Joomla form field show_associations_edit; input is validated and filtered according to x-joomla-form.||
|save_history|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable Versions: Joomla form field save_history; input is validated and filtered according to x-joomla-form.||
|history_limit|["integer", "string"]|нет|"10"|Maximum Versions: Joomla form field history_limit; input is validated and filtered according to x-joomla-form.|save_history:1|
|show_urls_images_frontend|["integer", "string"]|нет|[0, 1, "0", "1"]|Frontend Images and Links: Joomla form field show_urls_images_frontend; input is validated and filtered according to x-joomla-form.||
|show_urls_images_backend|["integer", "string"]|нет|[0, 1, "0", "1"]|Administrator Images and Links: Joomla form field show_urls_images_backend; input is validated and filtered according to x-joomla-form.||
|targeta|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|URL A Target Window: Joomla form field targeta; input is validated and filtered according to x-joomla-form.|show_urls_images_backend:1[OR]show_urls_images_frontend:1|
|targetb|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|URL B Target Window: Joomla form field targetb; input is validated and filtered according to x-joomla-form.|show_urls_images_backend:1[OR]show_urls_images_frontend:1|
|targetc|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|URL C Target Window: Joomla form field targetc; input is validated and filtered according to x-joomla-form.|show_urls_images_backend:1[OR]show_urls_images_frontend:1|
|float_intro|"string"|нет|""|Intro Image Class: Joomla form field float_intro; input is validated and filtered according to x-joomla-form.|show_urls_images_backend:1[OR]show_urls_images_frontend:1|
|float_fulltext|"string"|нет|""|Full Text Image Class: Joomla form field float_fulltext; input is validated and filtered according to x-joomla-form.|show_urls_images_backend:1[OR]show_urls_images_frontend:1|
|category_layout|"string"|нет|""|Choose a Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|show_category_title|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|show_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|show_description_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|maxLevel|["integer", "string"]|нет|[0, -1, 1, 2, 3, 4, 5, "0", "-1", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|show_empty_categories|["integer", "string"]|нет|[0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.||
|show_no_articles|["integer", "string"]|нет|[0, 1, "0", "1"]|No Articles Message: Joomla form field show_no_articles; input is validated and filtered according to x-joomla-form.||
|show_category_heading_title_text|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Heading: Joomla form field show_category_heading_title_text; input is validated and filtered according to x-joomla-form.||
|show_subcat_desc|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.||
|show_cat_num_articles|["integer", "string"]|нет|[0, 1, "0", "1"]|# Articles in Category: Joomla form field show_cat_num_articles; input is validated and filtered according to x-joomla-form.||
|show_cat_tags|["integer", "string"]|нет|[0, 1, "0", "1"]|Tags: Joomla form field show_cat_tags; input is validated and filtered according to x-joomla-form.||
|show_base_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Top Level Category Description: Joomla form field show_base_description; input is validated and filtered according to x-joomla-form.||
|maxLevelcat|["integer", "string"]|нет|[0, -1, 1, 2, 3, 4, 5, "0", "-1", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevelcat; input is validated and filtered according to x-joomla-form.||
|show_empty_categories_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories_cat; input is validated and filtered according to x-joomla-form.|maxLevelcat:-1,1,2,3,4,5|
|show_subcat_desc_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc_cat; input is validated and filtered according to x-joomla-form.|maxLevelcat:-1,1,2,3,4,5|
|show_cat_num_articles_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|# Articles in Category: Joomla form field show_cat_num_articles_cat; input is validated and filtered according to x-joomla-form.||
|num_leading_articles|["integer", "string"]|нет|"1"|# Leading Articles: Joomla form field num_leading_articles; input is validated and filtered according to x-joomla-form.||
|blog_class_leading|"string"|нет|""|Leading Article Class: Joomla form field blog_class_leading; input is validated and filtered according to x-joomla-form.||
|num_intro_articles|["integer", "string"]|нет|"4"|# Intro Articles: Joomla form field num_intro_articles; input is validated and filtered according to x-joomla-form.||
|blog_class|"string"|нет|""|Article Class: You can add any CSS class for your own styling ideas.<br>Add a border on top with class boxed.<br>For image position use for example image-left, image-right. Add image-alternate for alternate ordering of intro images.||
|num_columns|["integer", "string"]|нет|"1"|# Columns: Joomla form field num_columns; input is validated and filtered according to x-joomla-form.||
|multi_column_order|["integer", "string"]|нет|[0, 1, "0", "1"]|Multi Column Direction: Joomla form field multi_column_order; input is validated and filtered according to x-joomla-form.||
|num_links|["integer", "string"]|нет|"4"|# Links: Joomla form field num_links; input is validated and filtered according to x-joomla-form.||
|show_subcategory_content|["integer", "string"]|нет|[0, -1, 1, 2, 3, 4, 5, "0", "-1", "1", "2", "3", "4", "5"]|Include Subcategories: Joomla form field show_subcategory_content; input is validated and filtered according to x-joomla-form.||
|link_intro_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Linked Intro Image: Joomla form field link_intro_image; input is validated and filtered according to x-joomla-form.||
|show_pagination_limit|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|filter_field|"string"|нет|["hide", "title", "author", "hits", "tag", "month"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|show_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|list_show_date|"string"|нет|["0", "created", "modified", "published"]|Date: Joomla form field list_show_date; input is validated and filtered according to x-joomla-form.||
|date_format|"string"|нет|""|Date Format: Joomla form field date_format; input is validated and filtered according to x-joomla-form.|list_show_date:created,modified,published|
|list_show_hits|["integer", "string"]|нет|[0, 1, "0", "1"]|Hits: Joomla form field list_show_hits; input is validated and filtered according to x-joomla-form.||
|list_show_author|["integer", "string"]|нет|[0, 1, "0", "1"]|Author: Joomla form field list_show_author; input is validated and filtered according to x-joomla-form.||
|display_num|["integer", "string"]|нет|[5, 10, 15, 20, 25, 30, 50, 100, 0, "5", "10", "15", "20", "25", "30", "50", "100", "0"]|# Articles to List: Joomla form field display_num; input is validated and filtered according to x-joomla-form.||
|list_show_votes|["integer", "string"]|нет|"0"|Show Votes in List: Joomla form field list_show_votes; input is validated and filtered according to x-joomla-form.||
|list_show_ratings|["integer", "string"]|нет|"0"|Show Ratings in List: Joomla form field list_show_ratings; input is validated and filtered according to x-joomla-form.||
|orderby_pri|"string"|нет|["none", "alpha", "ralpha", "order"]|Category Order: Joomla form field orderby_pri; input is validated and filtered according to x-joomla-form.||
|orderby_sec|"string"|нет|["rdate", "date", "alpha", "ralpha", "author", "rauthor", "hits", "rhits", "order", "rorder", "vote", "rvote", "rank", "rrank"]|Article Order: Joomla form field orderby_sec; input is validated and filtered according to x-joomla-form.||
|order_date|"string"|нет|["created", "modified", "published"]|Date for Ordering: Joomla form field order_date; input is validated and filtered according to x-joomla-form.||
|show_pagination|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|show_pagination_results|["integer", "string"]|нет|[0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.|show_pagination:1,2|
|show_featured|"string"|нет|["show", "hide", "only"]|Featured Articles: Joomla form field show_featured; input is validated and filtered according to x-joomla-form.||
|show_feed_link|["integer", "string"]|нет|[0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
|feed_summary|["integer", "string"]|нет|[0, 1, "0", "1"]|Include in Feed: Joomla form field feed_summary; input is validated and filtered according to x-joomla-form.|show_feed_link:1|
|feed_show_readmore|["integer", "string"]|нет|[0, 1, "0", "1"]|&quot;Read More&quot; Link: Displays a &quot;Read More&quot; link in the news feeds if Intro Text is set to Show.|show_feed_link:1[AND]feed_summary:0|
|sef_ids|["integer", "string"]|нет|[0, 1, "0", "1"]|Remove IDs from URLs: Joomla form field sef_ids; input is validated and filtered according to x-joomla-form.||
|custom_fields_enable|["integer", "string"]|нет|[0, 1, "0", "1"]|Edit Custom Fields: Joomla form field custom_fields_enable; input is validated and filtered according to x-joomla-form.||
|workflow_enabled|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable Workflow: Joomla form field workflow_enabled; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
