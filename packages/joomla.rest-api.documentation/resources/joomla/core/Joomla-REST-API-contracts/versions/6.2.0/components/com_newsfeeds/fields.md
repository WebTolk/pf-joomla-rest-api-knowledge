# com_newsfeeds: заполнение полей, Joomla 6.2.0

См. форму и схему ответа endpoint.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/newsfeeds/feeds

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|да|""|Title: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|catid|"anyOf"|да|""|catid: Existing category ID, or category title (optionally #new#Title) for inline creation when the owner model's canCreateCategory permission allows it. Prefer a known ID unless creation is intended.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|link|"string"|да|""|Link: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|numarticles|["integer", "string"]|нет|"5"|Number of Articles: Joomla form field numarticles; input is validated and filtered according to x-joomla-form.||
|cache_time|["integer", "string"]|нет|"3600"|Cache Time: Joomla form field cache_time; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_first|"string"|нет|""|First Image: Joomla form field image_first; input is validated and filtered according to x-joomla-form.||
|images.float_first|"string"|нет|["", "right", "left", "none"]|Image Float: Joomla form field float_first; input is validated and filtered according to x-joomla-form.||
|images.image_first_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_first_alt; input is validated and filtered according to x-joomla-form.||
|images.image_first_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.image_first_caption|"string"|нет|""|Caption: Joomla form field image_first_caption; input is validated and filtered according to x-joomla-form.||
|images.image_second|"string"|нет|""|Second Image: Joomla form field image_second; input is validated and filtered according to x-joomla-form.||
|images.float_second|"string"|нет|["", "right", "left", "none"]|Image Float: Joomla form field float_second; input is validated and filtered according to x-joomla-form.||
|images.image_second_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_second_alt; input is validated and filtered according to x-joomla-form.||
|images.image_second_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.image_second_caption|"string"|нет|""|Caption: Joomla form field image_second_caption; input is validated and filtered according to x-joomla-form.||
|rtl|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Language Direction: Joomla form field rtl; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_feed_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Image: Joomla form field show_feed_image; input is validated and filtered according to x-joomla-form.||
|params.show_feed_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Description: Joomla form field show_feed_description; input is validated and filtered according to x-joomla-form.||
|params.show_item_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Content: Joomla form field show_item_description; input is validated and filtered according to x-joomla-form.||
|params.feed_character_count|["integer", "string"]|нет|""|Characters Count: 0 will show all the text.||
|params.newsfeed_layout|"string"|нет|""|Layout: Joomla form field newsfeed_layout; input is validated and filtered according to x-joomla-form.||
|params.feed_display_order|"string"|нет|["", "des", "asc"]|Feed Display Order: Joomla form field feed_display_order; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Content Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
## REST PATCH /v1/newsfeeds/feeds/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|name|"string"|нет|""|Title: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|catid|"anyOf"|нет|""|catid: Existing category ID, or category title (optionally #new#Title) for inline creation when the owner model's canCreateCategory permission allows it. Prefer a known ID unless creation is intended.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|link|"string"|нет|""|Link: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|numarticles|["integer", "string"]|нет|"5"|Number of Articles: Joomla form field numarticles; input is validated and filtered according to x-joomla-form.||
|cache_time|["integer", "string"]|нет|"3600"|Cache Time: Joomla form field cache_time; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_first|"string"|нет|""|First Image: Joomla form field image_first; input is validated and filtered according to x-joomla-form.||
|images.float_first|"string"|нет|["", "right", "left", "none"]|Image Float: Joomla form field float_first; input is validated and filtered according to x-joomla-form.||
|images.image_first_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_first_alt; input is validated and filtered according to x-joomla-form.||
|images.image_first_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.image_first_caption|"string"|нет|""|Caption: Joomla form field image_first_caption; input is validated and filtered according to x-joomla-form.||
|images.image_second|"string"|нет|""|Second Image: Joomla form field image_second; input is validated and filtered according to x-joomla-form.||
|images.float_second|"string"|нет|["", "right", "left", "none"]|Image Float: Joomla form field float_second; input is validated and filtered according to x-joomla-form.||
|images.image_second_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_second_alt; input is validated and filtered according to x-joomla-form.||
|images.image_second_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.image_second_caption|"string"|нет|""|Caption: Joomla form field image_second_caption; input is validated and filtered according to x-joomla-form.||
|rtl|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Language Direction: Joomla form field rtl; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_feed_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Image: Joomla form field show_feed_image; input is validated and filtered according to x-joomla-form.||
|params.show_feed_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Description: Joomla form field show_feed_description; input is validated and filtered according to x-joomla-form.||
|params.show_item_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Content: Joomla form field show_item_description; input is validated and filtered according to x-joomla-form.||
|params.feed_character_count|["integer", "string"]|нет|""|Characters Count: 0 will show all the text.||
|params.newsfeed_layout|"string"|нет|""|Layout: Joomla form field newsfeed_layout; input is validated and filtered according to x-joomla-form.||
|params.feed_display_order|"string"|нет|["", "des", "asc"]|Feed Display Order: Joomla form field feed_display_order; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Content Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||

## Инвентарь стандартных форм UI

## administrator/components/com_newsfeeds/forms/category.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## administrator/components/com_newsfeeds/forms/filter_newsfeeds.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search News Feeds: Search in news feed title and alias. Prefix with ID: to search for a news feed ID.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.category_id|["integer", "string"]|нет|""|Category: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.tag|"array"|нет|[]|Tags: Joomla form field tag; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.published ASC", "a.published DESC", "a.name ASC", "a.name DESC", "category_title ASC", "category_title DESC", "access_level ASC", "access_level DESC", "numarticles ASC", "numarticles DESC", "a.cache_time ASC", "a.cache_time DESC", "association ASC", "association DESC", "language_title ASC", "language_title DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_newsfeeds/forms/newsfeed.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|name|"string"|да|""|Title: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|catid|["integer", "string"]|да|""|Category: Joomla form field catid; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Joomla form field tags; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|link|"string"|да|""|Link: URL subject to field relative/scheme settings; empty string may clear an optional URL.||
|numarticles|["integer", "string"]|нет|"5"|Number of Articles: Joomla form field numarticles; input is validated and filtered according to x-joomla-form.||
|cache_time|["integer", "string"]|нет|"3600"|Cache Time: Joomla form field cache_time; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|modified|"string"|нет|""|Modified Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_up|"string"|нет|""|Start Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|publish_down|"string"|нет|""|Finish Publishing: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_first|"string"|нет|""|First Image: Joomla form field image_first; input is validated and filtered according to x-joomla-form.||
|images.float_first|"string"|нет|["", "right", "left", "none"]|Image Float: Joomla form field float_first; input is validated and filtered according to x-joomla-form.||
|images.image_first_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_first_alt; input is validated and filtered according to x-joomla-form.||
|images.image_first_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.image_first_caption|"string"|нет|""|Caption: Joomla form field image_first_caption; input is validated and filtered according to x-joomla-form.||
|images.image_second|"string"|нет|""|Second Image: Joomla form field image_second; input is validated and filtered according to x-joomla-form.||
|images.float_second|"string"|нет|["", "right", "left", "none"]|Image Float: Joomla form field float_second; input is validated and filtered according to x-joomla-form.||
|images.image_second_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_second_alt; input is validated and filtered according to x-joomla-form.||
|images.image_second_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|images.image_second_caption|"string"|нет|""|Caption: Joomla form field image_second_caption; input is validated and filtered according to x-joomla-form.||
|rtl|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Language Direction: Joomla form field rtl; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.show_feed_image|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Image: Joomla form field show_feed_image; input is validated and filtered according to x-joomla-form.||
|params.show_feed_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Description: Joomla form field show_feed_description; input is validated and filtered according to x-joomla-form.||
|params.show_item_description|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Feed Content: Joomla form field show_item_description; input is validated and filtered according to x-joomla-form.||
|params.feed_character_count|["integer", "string"]|нет|""|Characters Count: 0 will show all the text.||
|params.newsfeed_layout|"string"|нет|""|Layout: Joomla form field newsfeed_layout; input is validated and filtered according to x-joomla-form.||
|params.feed_display_order|"string"|нет|["", "des", "asc"]|Feed Display Order: Joomla form field feed_display_order; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|metadata.rights|"string"|нет|""|Content Rights: Joomla form field rights; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_newsfeeds/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|newsfeed_layout|"string"|нет|""|Choose a Layout: Joomla form field newsfeed_layout; input is validated and filtered according to x-joomla-form.||
|save_history|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable Versions: Joomla form field save_history; input is validated and filtered according to x-joomla-form.||
|history_limit|["integer", "string"]|нет|"5"|Maximum Versions: Joomla form field history_limit; input is validated and filtered according to x-joomla-form.|save_history:1|
|show_feed_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Feed Image: Joomla form field show_feed_image; input is validated and filtered according to x-joomla-form.||
|show_feed_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Feed Description: Joomla form field show_feed_description; input is validated and filtered according to x-joomla-form.||
|show_item_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Feed Content: Joomla form field show_item_description; input is validated and filtered according to x-joomla-form.||
|feed_character_count|["integer", "string"]|нет|"0"|Characters Count: 0 will show all the text.||
|feed_display_order|"string"|нет|["des", "asc"]|Feed Display Order: Joomla form field feed_display_order; input is validated and filtered according to x-joomla-form.||
|float_first|"string"|нет|["right", "left", "none"]|First Image Float: Joomla form field float_first; input is validated and filtered according to x-joomla-form.||
|float_second|"string"|нет|["right", "left", "none"]|Second Image Float: Joomla form field float_second; input is validated and filtered according to x-joomla-form.||
|show_tags|["integer", "string"]|нет|[0, 1, "0", "1"]|Tags: Joomla form field show_tags; input is validated and filtered according to x-joomla-form.||
|category_layout|"string"|нет|""|Choose a Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|show_category_title|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Title: Joomla form field show_category_title; input is validated and filtered according to x-joomla-form.||
|show_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|show_description_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Category Image: Joomla form field show_description_image; input is validated and filtered according to x-joomla-form.||
|maxLevel|["integer", "string"]|нет|[0, -1, 1, 2, 3, 4, 5, "0", "-1", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevel; input is validated and filtered according to x-joomla-form.||
|show_empty_categories|["integer", "string"]|нет|[0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories; input is validated and filtered according to x-joomla-form.|maxLevel:-1,1,2,3,4,5|
|show_subcat_desc|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc; input is validated and filtered according to x-joomla-form.|maxLevel:-1,1,2,3,4,5|
|show_subcat_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Image: Joomla form field show_subcat_image; input is validated and filtered according to x-joomla-form.|maxLevel:-1,1,2,3,4,5|
|show_cat_items|["integer", "string"]|нет|[0, 1, "0", "1"]|# Feeds in Category: Joomla form field show_cat_items; input is validated and filtered according to x-joomla-form.||
|show_cat_tags|["integer", "string"]|нет|[0, 1, "0", "1"]|Tags: Joomla form field show_cat_tags; input is validated and filtered according to x-joomla-form.||
|show_base_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Top Level Category Description: Joomla form field show_base_description; input is validated and filtered according to x-joomla-form.||
|maxLevelcat|["integer", "string"]|нет|[-1, 0, 1, 2, 3, 4, 5, "-1", "0", "1", "2", "3", "4", "5"]|Subcategory Levels: Joomla form field maxLevelcat; input is validated and filtered according to x-joomla-form.||
|show_empty_categories_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|Empty Categories: Joomla form field show_empty_categories_cat; input is validated and filtered according to x-joomla-form.|maxLevelcat:-1,1,2,3,4,5|
|show_subcat_desc_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|Subcategories Descriptions: Joomla form field show_subcat_desc_cat; input is validated and filtered according to x-joomla-form.|maxLevelcat:-1,1,2,3,4,5|
|show_cat_items_cat|["integer", "string"]|нет|[0, 1, "0", "1"]|# Feeds in Category: Joomla form field show_cat_items_cat; input is validated and filtered according to x-joomla-form.||
|filter_field|["integer", "string"]|нет|[0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|show_pagination_limit|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|show_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|show_articles|["integer", "string"]|нет|[0, 1, "0", "1"]|# Articles: Joomla form field show_articles; input is validated and filtered according to x-joomla-form.||
|show_link|["integer", "string"]|нет|[0, 1, "0", "1"]|Feed Links: Joomla form field show_link; input is validated and filtered according to x-joomla-form.||
|show_pagination|["integer", "string"]|нет|[1, 0, 2, "1", "0", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|show_pagination_results|["integer", "string"]|нет|[0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.|show_pagination:1,2|
|sef_ids|["integer", "string"]|нет|[0, 1, "0", "1"]|Remove IDs from URLs: Joomla form field sef_ids; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
