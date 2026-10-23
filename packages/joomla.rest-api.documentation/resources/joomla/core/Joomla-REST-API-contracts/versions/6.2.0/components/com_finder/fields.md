# com_finder: заполнение полей, Joomla 6.2.0

В этих снимках отсутствуют штатные REST-маршруты индекса и поиска com_finder.
Не изобретать /v1/finder или REST-команду переиндексации. Настройки доступны
через com_config при допустимых ACL. Индекс, карты и поисковые фильтры управляются
штатным UI; включены схемы core-форм для точного заполнения.
Публикация статьи не доказывает её присутствие в поисковом индексе.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.


## Инвентарь стандартных форм UI

## administrator/components/com_finder/forms/filter.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter_id|"string"|нет|"0"|ID: Joomla form field filter_id; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|modified|"string"|нет|""|Modified Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|created_by_alias|"string"|нет|""|Created by Alias: Joomla form field created_by_alias; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, "1", "0"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|map_count|"string"|нет|"0"|Map Count: Joomla form field map_count; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.w1|["integer", "string"]|нет|["", -1, 0, 1, "-1", "0", "1"]|When (Start Date): Joomla form field w1; input is validated and filtered according to x-joomla-form.||
|params.d1|"string"|нет|""|Start Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|params.w2|["integer", "string"]|нет|["", -1, 0, 1, "-1", "0", "1"]|When (End Date): Joomla form field w2; input is validated and filtered according to x-joomla-form.||
|params.d2|"string"|нет|""|End Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
## administrator/components/com_finder/forms/filter_filters.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Filters: Search in filter title.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.state ASC", "a.state DESC", "a.title ASC", "a.title DESC", "a.created_by_alias ASC", "a.created_by_alias DESC", "a.created ASC", "a.created DESC", "a.map_count ASC", "a.map_count DESC", "a.filter_id ASC", "a.filter_id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_finder/forms/filter_index.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Indexed Content: Search in title, URL and last updated date.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.type|"string"|нет|""|Content Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|filter.content_map|"string"|нет|""|Content Map: Joomla form field content_map; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "l.published ASC", "l.published DESC", "l.title ASC", "l.title DESC", "t.title ASC", "t.title DESC", "l.indexdate ASC", "l.indexdate DESC", "l.language ASC", "l.language DESC", "l.url ASC", "l.url DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_finder/forms/filter_maps.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Content Maps: Search in content map title.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.branch|"string"|нет|"0"|Map Group: Joomla form field branch; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.state ASC", "a.state DESC", "branch_title ASC, a.lft ASC", "branch_title DESC, a.lft DESC", "a.language ASC", "a.language DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_finder/forms/filter_searches.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Filter by searched phrase: Search for the logged phrase of a search.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.searchterm ASC", "a.searchterm DESC", "a.hits ASC", "a.hits DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_finder/forms/indexer.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|plugin|"string"|да|""|Finder Plugin: Joomla form field plugin; input is validated and filtered according to x-joomla-form.||
|id|"string"|да|""|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_finder/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|word_match|"string"|нет|["exact", "begin", "fuzzy"]|Word Match: Set how search terms are matched in the index. By default a word is matched exactly, but when a language supports compound words, this allows to match the search term to the beginning or in a random place inside of words in the index.||
|show_taxonomy|["integer", "string"]|нет|[0, 1, "0", "1"]|Result Taxonomy: Joomla form field show_taxonomy; input is validated and filtered according to x-joomla-form.||
|show_description|["integer", "string"]|нет|[0, 1, "0", "1"]|Result Description: Joomla form field show_description; input is validated and filtered according to x-joomla-form.||
|description_length|["integer", "string"]|нет|"255"|Description Length: Joomla form field description_length; input is validated and filtered according to x-joomla-form.|show_description:1|
|show_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Result Image: Joomla form field show_image; input is validated and filtered according to x-joomla-form.||
|image_class|"string"|нет|""|Image Class: Joomla form field image_class; input is validated and filtered according to x-joomla-form.|show_image:1|
|link_image|["integer", "string"]|нет|[0, 1, "0", "1"]|Linked Image: Joomla form field link_image; input is validated and filtered according to x-joomla-form.|show_image:1|
|show_date|["integer", "string"]|нет|[0, 1, "0", "1"]|Result Date: Joomla form field show_date; input is validated and filtered according to x-joomla-form.||
|show_url|["integer", "string"]|нет|[0, 1, "0", "1"]|Result URL: Joomla form field show_url; input is validated and filtered according to x-joomla-form.||
|gather_search_statistics|["integer", "string"]|нет|[0, 1, "0", "1"]|Gather Search Statistics: Joomla form field gather_search_statistics; input is validated and filtered according to x-joomla-form.||
|allow_empty_query|["integer", "string"]|нет|[0, 1, "0", "1"]|Allow Empty Search: Joomla form field allow_empty_query; input is validated and filtered according to x-joomla-form.||
|show_autosuggest|["integer", "string"]|нет|[0, 1, "0", "1"]|Search Suggestions: Joomla form field show_autosuggest; input is validated and filtered according to x-joomla-form.||
|show_suggested_query|["integer", "string"]|нет|[0, 1, "0", "1"]|Did You Mean: Joomla form field show_suggested_query; input is validated and filtered according to x-joomla-form.||
|show_explained_query|["integer", "string"]|нет|[0, 1, "0", "1"]|Query Explanation: Joomla form field show_explained_query; input is validated and filtered according to x-joomla-form.||
|show_advanced|["integer", "string"]|нет|[0, 1, "0", "1"]|Advanced Search: Joomla form field show_advanced; input is validated and filtered according to x-joomla-form.||
|show_advanced_tips|["integer", "string"]|нет|[0, 1, "0", "1"]|Advanced Tips: Joomla form field show_advanced_tips; input is validated and filtered according to x-joomla-form.|show_advanced:1|
|expand_advanced|["integer", "string"]|нет|[0, 1, "0", "1"]|Expand Advanced Search: Joomla form field expand_advanced; input is validated and filtered according to x-joomla-form.|show_advanced:1|
|show_date_filters|["integer", "string"]|нет|[0, 1, "0", "1"]|Date Filters: Joomla form field show_date_filters; input is validated and filtered according to x-joomla-form.|show_advanced:1|
|sort_order|"string"|нет|["relevance", "title", "date", "price", "sale_price"]|Sort Field: Joomla form field sort_order; input is validated and filtered according to x-joomla-form.||
|sort_direction|"string"|нет|["desc", "asc"]|Sort Direction: Joomla form field sort_direction; input is validated and filtered according to x-joomla-form.||
|highlight_terms|["integer", "string"]|нет|[0, 1, "0", "1"]|Highlight Search Terms: For performance reasons, this will not highlight more than 10 different terms in the search results.||
|opensearch|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable OpenSearch: Joomla form field opensearch; input is validated and filtered according to x-joomla-form.||
|opensearch_name|"string"|нет|""|OpenSearch Name: Joomla form field opensearch_name; input is validated and filtered according to x-joomla-form.|opensearch:1|
|opensearch_description|"string"|нет|""|OpenSearch Description: Joomla form field opensearch_description; input is validated and filtered according to x-joomla-form.|opensearch:1|
|tuplecount|["integer", "string"]|нет|[1, 3, "1", "3"]|Search for Phrases: Joomla form field tuplecount; input is validated and filtered according to x-joomla-form.||
|batch_size|["integer", "string"]|нет|[5, 10, 25, 50, 75, 100, 150, 200, 250, 300, "5", "10", "25", "50", "75", "100", "150", "200", "250", "300"]|Indexer Batch Size: Joomla form field batch_size; input is validated and filtered according to x-joomla-form.||
|title_multiplier|["integer", "string"]|нет|"1.7"|Title Text Weight Multiplier: Joomla form field title_multiplier; input is validated and filtered according to x-joomla-form.||
|text_multiplier|["integer", "string"]|нет|"0.7"|Body Text Weight Multiplier: Joomla form field text_multiplier; input is validated and filtered according to x-joomla-form.||
|meta_multiplier|["integer", "string"]|нет|"1.2"|Metadata Weight Multiplier: Joomla form field meta_multiplier; input is validated and filtered according to x-joomla-form.||
|path_multiplier|["integer", "string"]|нет|"2.0"|Path Text Weight Multiplier: Joomla form field path_multiplier; input is validated and filtered according to x-joomla-form.||
|misc_multiplier|["integer", "string"]|нет|"0.3"|Misc. Text Weight Multiplier: Joomla form field misc_multiplier; input is validated and filtered according to x-joomla-form.||
|enable_logging|["integer", "string"]|нет|[0, 1, "0", "1"]|Enable Logging: Joomla form field enable_logging; input is validated and filtered according to x-joomla-form.||
|language_default|["integer", "string"]|нет|""|Default Language: Set the language to be used for non-multilingual sites or content marked as "All".||
|filter_commonwords|["integer", "string"]|нет|[0, 1, "0", "1"]|Filter Common Words: Joomla form field filter_commonwords; input is validated and filtered according to x-joomla-form.||
|filter_numerics|["integer", "string"]|нет|[0, 1, "0", "1"]|Filter Numeric Terms: Joomla form field filter_numerics; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
