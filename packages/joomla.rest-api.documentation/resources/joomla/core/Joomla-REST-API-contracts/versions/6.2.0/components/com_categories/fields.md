# com_categories: заполнение полей, Joomla 6.2.0

Контекст категории фиксируется defaults.extension маршрута: com_content, com_contact,
com_newsfeeds или com_banners. parent_id относится к дереву того же extension.
lft/rgt/level — вычисляемые данные. location/location_reference читаются из тела
JSON после сохранения для перемещения в дереве; это отдельная операция setLocation.
Параметры категории могут дополняться формами конкретного компонента.
В 6.2.0 GET списка поддерживает filter[state] (INT), который передаётся в filter.published модели.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/banners/categories

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
|location|"string"|нет|["before", "after", "first-child", "last-child"]|location: Optional Nested-table positioning after save; relative to location_reference or parent_id. This is read from the JSON body.||
|location_reference|["integer", "string"]|нет|""|location_reference: ||
## REST PATCH /v1/banners/categories/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
|location|"string"|нет|["before", "after", "first-child", "last-child"]|location: Optional Nested-table positioning after save; relative to location_reference or parent_id. This is read from the JSON body.||
|location_reference|["integer", "string"]|нет|""|location_reference: ||
## REST POST /v1/contacts/categories

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
|location|"string"|нет|["before", "after", "first-child", "last-child"]|location: Optional Nested-table positioning after save; relative to location_reference or parent_id. This is read from the JSON body.||
|location_reference|["integer", "string"]|нет|""|location_reference: ||
## REST PATCH /v1/contacts/categories/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
|location|"string"|нет|["before", "after", "first-child", "last-child"]|location: Optional Nested-table positioning after save; relative to location_reference or parent_id. This is read from the JSON body.||
|location_reference|["integer", "string"]|нет|""|location_reference: ||
## REST POST /v1/content/categories

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|params.workflow_id|["integer", "string"]|да|"use_default"|Workflows: SQL selector returns numeric IDs; explicit inheritance/default tokens may also be strings.||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
|location|"string"|нет|["before", "after", "first-child", "last-child"]|location: Optional Nested-table positioning after save; relative to location_reference or parent_id. This is read from the JSON body.||
|location_reference|["integer", "string"]|нет|""|location_reference: ||
## REST PATCH /v1/content/categories/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|params.workflow_id|["integer", "string"]|нет|"use_default"|Workflows: SQL selector returns numeric IDs; explicit inheritance/default tokens may also be strings.||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
|location|"string"|нет|["before", "after", "first-child", "last-child"]|location: Optional Nested-table positioning after save; relative to location_reference or parent_id. This is read from the JSON body.||
|location_reference|["integer", "string"]|нет|""|location_reference: ||
## REST POST /v1/newsfeeds/categories

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
|location|"string"|нет|["before", "after", "first-child", "last-child"]|location: Optional Nested-table positioning after save; relative to location_reference or parent_id. This is read from the JSON body.||
|location_reference|["integer", "string"]|нет|""|location_reference: ||
## REST PATCH /v1/newsfeeds/categories/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Full tag ID list; #new#Title creates a tag only with core.create on com_tags. Omitted tags are restored by ArticlesController, but generic ApiController supplies [] for absent tags; other owners can clear tag relations.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|com_fields|"object"|нет|""|com_fields: ||
|associations|"object"|нет|""|associations: Installed content-language tag -> owner record ID (integer/numeric string; 0 or empty string removes an entry from the supplied map). Dynamic form exists only with enabled associations and more than one content language; categories also require an association-capable owner. Supply the full desired mapping. An empty object is skipped by AdminModel and does not mean unlink all.||
|location|"string"|нет|["before", "after", "first-child", "last-child"]|location: Optional Nested-table positioning after save; relative to location_reference or parent_id. This is read from the JSON body.||
|location_reference|["integer", "string"]|нет|""|location_reference: ||

## Инвентарь стандартных форм UI

## administrator/components/com_categories/forms/category.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|parent_id|["integer", "string"]|нет|""|Parent: Joomla form field parent_id; input is validated and filtered according to x-joomla-form.||
|path|"string"|нет|""|Category Path: Joomla form field path; input is validated and filtered according to x-joomla-form.||
|extension|"string"|нет|""|extension: Joomla form field extension; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|alias|"string"|нет|""|Alias: The Alias will be used as part of the URL.||
|version_note|"string"|нет|""|Version Note: Joomla form field version_note; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|published|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|metadesc|"string"|нет|""|Meta Description: Joomla form field metadesc; input is validated and filtered according to x-joomla-form.||
|metakey|"string"|нет|""|Keywords: Joomla form field metakey; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|modified_time|"string"|нет|""|Modified Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|tags|"array"|нет|""|Tags: Joomla form field tags; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.category_layout|"string"|нет|""|Layout: Joomla form field category_layout; input is validated and filtered according to x-joomla-form.||
|params.image|"string"|нет|""|Image: Joomla form field image; input is validated and filtered according to x-joomla-form.||
|params.image_alt|"string"|нет|""|Image Description (Alt Text): Joomla form field image_alt; input is validated and filtered according to x-joomla-form.||
|params.image_alt_empty|"string"|нет|""|No Description: Decorative Image - no description required||
|metadata|"object"|нет|""|metadata: ||
|metadata.author|"string"|нет|""|Author: Joomla form field author; input is validated and filtered according to x-joomla-form.||
|metadata.robots|"string"|нет|["", "index, follow", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_categories/forms/filter_categories.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Categories: Search in title, alias and note. Prefix with ID: to search for a category ID.||
|filter.published|"string"|нет|""|Status: Joomla form field published; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.tag|"array"|нет|[]|Tags: Joomla form field tag; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|filter.category_id|"array"|нет|""|- Select Category -: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.lft ASC", "a.lft DESC", "a.published ASC", "a.published DESC", "a.title ASC", "a.title DESC", "access_level ASC", "access_level DESC", "association ASC", "association DESC", "language_title ASC", "language_title DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
