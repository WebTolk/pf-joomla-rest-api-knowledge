# com_tags: заполнение полей, Joomla 5.4.8

См. форму и схему ответа endpoint.
Для снимка 5.4.8 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/tags

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.tag_layout|"string"|нет|""|Layout: Joomla form field tag_layout; input is validated and filtered according to x-joomla-form.||
|params.tag_link_class|"string"|нет|""|CSS Class for tag link: Joomla form field tag_link_class; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_intro|"string"|нет|""|Teaser Image: Joomla form field image_intro; input is validated and filtered according to x-joomla-form.||
|images.float_intro|"string"|нет|["", "right", "left", "none"]|Float: Joomla form field float_intro; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt|"string"|нет|""|Alt Text: Joomla form field image_intro_alt; input is validated and filtered according to x-joomla-form.||
|images.image_intro_caption|"string"|нет|""|Caption: Joomla form field image_intro_caption; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext|"string"|нет|""|Full Image: Joomla form field image_fulltext; input is validated and filtered according to x-joomla-form.||
|images.float_fulltext|"string"|нет|["", "right", "left", "none"]|Float: Joomla form field float_fulltext; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt|"string"|нет|""|Alt Text: Joomla form field image_fulltext_alt; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_caption|"string"|нет|""|Caption: Joomla form field image_fulltext_caption; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/tags/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.tag_layout|"string"|нет|""|Layout: Joomla form field tag_layout; input is validated and filtered according to x-joomla-form.||
|params.tag_link_class|"string"|нет|""|CSS Class for tag link: Joomla form field tag_link_class; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_intro|"string"|нет|""|Teaser Image: Joomla form field image_intro; input is validated and filtered according to x-joomla-form.||
|images.float_intro|"string"|нет|["", "right", "left", "none"]|Float: Joomla form field float_intro; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt|"string"|нет|""|Alt Text: Joomla form field image_intro_alt; input is validated and filtered according to x-joomla-form.||
|images.image_intro_caption|"string"|нет|""|Caption: Joomla form field image_intro_caption; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext|"string"|нет|""|Full Image: Joomla form field image_fulltext; input is validated and filtered according to x-joomla-form.||
|images.float_fulltext|"string"|нет|["", "right", "left", "none"]|Float: Joomla form field float_fulltext; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt|"string"|нет|""|Alt Text: Joomla form field image_fulltext_alt; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_caption|"string"|нет|""|Caption: Joomla form field image_fulltext_caption; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||

## Инвентарь стандартных форм UI

## administrator/components/com_tags/forms/filter_tags.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Tags: Search in tag title, alias and note. Prefix with ID: to search for a tag ID.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|filter.extension|"string"|нет|""|Tag Type: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.lft ASC", "a.lft DESC", "a.published ASC", "a.published DESC", "a.title ASC", "a.title DESC", "a.access ASC", "a.access DESC", "a.language ASC", "a.language DESC", "countTaggedItems ASC", "countTaggedItems DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_tags/forms/tag.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|path|"string"|нет|""|CATEGORIES_PATH_LABEL: CATEGORIES_PATH_DESC||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|modified_time|"string"|нет|""|Modified Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.tag_layout|"string"|нет|""|Layout: Joomla form field tag_layout; input is validated and filtered according to x-joomla-form.||
|params.tag_link_class|"string"|нет|""|CSS Class for tag link: Joomla form field tag_link_class; input is validated and filtered according to x-joomla-form.||
|images|"object"|нет|""|images: ||
|images.image_intro|"string"|нет|""|Teaser Image: Joomla form field image_intro; input is validated and filtered according to x-joomla-form.||
|images.float_intro|"string"|нет|["", "right", "left", "none"]|Float: Joomla form field float_intro; input is validated and filtered according to x-joomla-form.||
|images.image_intro_alt|"string"|нет|""|Alt Text: Joomla form field image_intro_alt; input is validated and filtered according to x-joomla-form.||
|images.image_intro_caption|"string"|нет|""|Caption: Joomla form field image_intro_caption; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext|"string"|нет|""|Full Image: Joomla form field image_fulltext; input is validated and filtered according to x-joomla-form.||
|images.float_fulltext|"string"|нет|["", "right", "left", "none"]|Float: Joomla form field float_fulltext; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_alt|"string"|нет|""|Alt Text: Joomla form field image_fulltext_alt; input is validated and filtered according to x-joomla-form.||
|images.image_fulltext_caption|"string"|нет|""|Caption: Joomla form field image_fulltext_caption; input is validated and filtered according to x-joomla-form.||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_tags/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|tag_layout|"string"|нет|""|Default Tagged Items Layout: Joomla form field tag_layout; input is validated and filtered according to x-joomla-form.||
|save_history|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable Versions: Joomla form field save_history; input is validated and filtered according to x-joomla-form.||
|history_limit|["integer", "string"]|нет|"5"|Maximum Versions: Joomla form field history_limit; input is validated and filtered according to x-joomla-form.|save_history:1|
|show_tag_title|["integer", "string"]|нет|[0, 1, "0", "1"]|Tag Name: Joomla form field show_tag_title; input is validated and filtered according to x-joomla-form.||
|tag_list_show_tag_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Tag Image: Joomla form field tag_list_show_tag_image; input is validated and filtered according to x-joomla-form.||
|tag_list_show_tag_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Tag Description: Joomla form field tag_list_show_tag_description; input is validated and filtered according to x-joomla-form.||
|tag_list_image|"string"|нет|""|Image: Joomla form field tag_list_image; input is validated and filtered according to x-joomla-form.||
|tag_list_orderby|"string"|нет|["c.core_title", "match_count", "c.core_created_time", "c.core_modified_time", "c.core_publish_up"]|Order: Joomla form field tag_list_orderby; input is validated and filtered according to x-joomla-form.||
|tag_list_orderby_direction|"string"|нет|["ASC", "DESC"]|Direction: Joomla form field tag_list_orderby_direction; input is validated and filtered according to x-joomla-form.||
|show_headings|["integer", "string"]|нет|[0, 1, "0", "1"]|Table Headings: Joomla form field show_headings; input is validated and filtered according to x-joomla-form.||
|tag_list_show_date|"string"|нет|["0", "created", "modified", "published"]|Date: Joomla form field tag_list_show_date; input is validated and filtered according to x-joomla-form.||
|tag_list_show_item_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Item Images: Joomla form field tag_list_show_item_image; input is validated and filtered according to x-joomla-form.||
|tag_list_show_item_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Item Description: Joomla form field tag_list_show_item_description; input is validated and filtered according to x-joomla-form.||
|tag_list_item_maximum_characters|["integer", "string"]|нет|""|Maximum Characters: Joomla form field tag_list_item_maximum_characters; input is validated and filtered according to x-joomla-form.|tag_list_show_item_description:1|
|min_term_length|["integer", "string"]|нет|"3"|Minimum Search Length: Joomla form field min_term_length; input is validated and filtered according to x-joomla-form.||
|return_any_or_all|["integer", "string"]|нет|[0, 1, "0", "1"]|Match Type: Joomla form field return_any_or_all; input is validated and filtered according to x-joomla-form.||
|include_children|["integer", "string"]|нет|[0, 1, "0", "1"]|Child Tags: Joomla form field include_children; input is validated and filtered according to x-joomla-form.||
|maximum|["integer", "string"]|нет|"200"|Maximum Items: Joomla form field maximum; input is validated and filtered according to x-joomla-form.||
|tag_list_language_filter|"string"|нет|"all"|Language Filter: Joomla form field tag_list_language_filter; input is validated and filtered according to x-joomla-form.||
|record_hits|["integer", "string"]|нет|[0, 1, "0", "1"]|Record Hits: Joomla form field record_hits; input is validated and filtered according to x-joomla-form.||
|tags_layout|"string"|нет|""|Default List All Tags Layout: Joomla form field tags_layout; input is validated and filtered according to x-joomla-form.||
|all_tags_orderby|"string"|нет|["title", "hits", "created_time", "modified_time", "publish_up"]|Order: Joomla form field all_tags_orderby; input is validated and filtered according to x-joomla-form.||
|all_tags_orderby_direction|"string"|нет|["ASC", "DESC"]|Direction: Joomla form field all_tags_orderby_direction; input is validated and filtered according to x-joomla-form.||
|all_tags_show_tag_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Item Images: Joomla form field all_tags_show_tag_image; input is validated and filtered according to x-joomla-form.||
|all_tags_show_tag_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Tag Descriptions: Joomla form field all_tags_show_tag_description; input is validated and filtered according to x-joomla-form.||
|all_tags_tag_maximum_characters|["integer", "string"]|нет|""|Maximum Characters: Joomla form field all_tags_tag_maximum_characters; input is validated and filtered according to x-joomla-form.|all_tags_show_tag_description:1|
|all_tags_show_tag_hits|["integer", "string"]|нет|[0, 1, "0", "1"]|Hits: Joomla form field all_tags_show_tag_hits; input is validated and filtered according to x-joomla-form.||
|filter_field|["integer", "string"]|нет|[0, 1, "0", "1"]|Filter Field: Joomla form field filter_field; input is validated and filtered according to x-joomla-form.||
|show_pagination_limit|["integer", "string"]|нет|[0, 1, "0", "1"]|Display Select: Joomla form field show_pagination_limit; input is validated and filtered according to x-joomla-form.||
|show_pagination|["integer", "string"]|нет|[1, 0, 2, "1", "0", "2"]|Pagination: Joomla form field show_pagination; input is validated and filtered according to x-joomla-form.||
|show_pagination_results|["integer", "string"]|нет|[0, 1, "0", "1"]|Pagination Summary: Joomla form field show_pagination_results; input is validated and filtered according to x-joomla-form.|show_pagination:1,2|
|tag_field_ajax_mode|["integer", "string"]|нет|[0, 1, "0", "1"]|Tag Entry Mode: Ajax mode searches tags while typing and allows you on the fly tag creation. Nested tags show you a nested view with all the available tags.||
|show_feed_link|["integer", "string"]|нет|[0, 1, "0", "1"]|RSS Feed Link: Joomla form field show_feed_link; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
