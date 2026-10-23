# com_fields: заполнение полей, Joomla 6.2.0

Определение поля, группа и значение поля у владельца — разные сущности.
Контекст задан маршрутом: com_content.article/categories, com_contact.contact/categories/mail,
com_users.user. name — ключ значения; id — ID определения. assigned_cat_ids
ограничивает применимость. fieldparams выбирается по типу из plugins/fields.
params описывает отображение/поведение. Значения передаются через com_fields
в операции владельца; поддерживаемые контроллеры также принимают имя поля сверху.
Subform сохраняет строки целиком; частичный merge rowN ядром не гарантируется.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/fields/contacts/contact

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST PATCH /v1/fields/contacts/contact/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST POST /v1/fields/contacts/mail

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST PATCH /v1/fields/contacts/mail/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST POST /v1/fields/contacts/categories

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST PATCH /v1/fields/contacts/categories/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST POST /v1/fields/groups/contacts/contact

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/fields/groups/contacts/contact/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/fields/groups/contacts/mail

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/fields/groups/contacts/mail/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/fields/groups/contacts/categories

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/fields/groups/contacts/categories/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/fields/content/articles

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST PATCH /v1/fields/content/articles/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST POST /v1/fields/content/categories

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST PATCH /v1/fields/content/categories/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST POST /v1/fields/groups/content/articles

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/fields/groups/content/articles/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/fields/groups/content/categories

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/fields/groups/content/categories/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST POST /v1/fields/users

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST PATCH /v1/fields/users/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|нет|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
|fieldparams|"object"|нет|""|fieldparams: ||
## REST POST /v1/fields/groups/users

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/fields/groups/users/{id}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|title|"string"|нет|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||

## Инвентарь стандартных форм UI

## administrator/components/com_fields/forms/field.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|group_id|["integer", "string"]|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|assigned_cat_ids|"array"|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.|only_use_in_subform:0|
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|name|"string"|нет|""|Name: Joomla form field name; input is validated and filtered according to x-joomla-form.||
|type|"string"|да|"text"|Type: Joomla form field type; input is validated and filtered according to x-joomla-form.||
|required|["integer", "string"]|нет|[0, 1, "0", "1"]|Required: Joomla form field required; input is validated and filtered according to x-joomla-form.||
|only_use_in_subform|["integer", "string"]|нет|[0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|default_value|"string"|нет|""|Default Value: Joomla form field default_value; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created_user_id|["integer", "string"]|нет|""|Created By: Joomla form field created_user_id; input is validated and filtered according to x-joomla-form.||
|created_time|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|modified_time|"string"|нет|""|Modified Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|label|"string"|нет|""|Label: Joomla form field label; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.hint|"string"|нет|""|Placeholder: Placeholder text which will appear inside the field as a hint to the user for the required input.||
|params.class|"string"|нет|""|Field Class: Joomla form field class; input is validated and filtered according to x-joomla-form.||
|params.label_class|"string"|нет|""|Label Class (Form): Joomla form field label_class; input is validated and filtered according to x-joomla-form.||
|params.show_on|["integer", "string"]|нет|[1, 2, "", "1", "2"]|Editable In: Joomla form field show_on; input is validated and filtered according to x-joomla-form.||
|params.showon|"string"|нет|""|Showon Attribute: Conditionally show or hide the field depending on the value of other fields.||
|params.render_class|"string"|нет|""|Display Class: The class of the field container in the output.||
|params.value_render_class|"string"|нет|""|Value Class: The class of the field value in the output.||
|params.showlabel|["integer", "string"]|нет|[0, 1, "0", "1"]|Label: Joomla form field showlabel; input is validated and filtered according to x-joomla-form.||
|params.label_render_class|"string"|нет|""|Label Class (Output): Joomla form field label_render_class; input is validated and filtered according to x-joomla-form.|showlabel:1|
|params.display|["integer", "string"]|нет|[1, 2, 3, 0, "1", "2", "3", "0"]|Automatic Display: Joomla form field display; input is validated and filtered according to x-joomla-form.||
|params.prefix|"string"|нет|""|Prefix: Joomla form field prefix; input is validated and filtered according to x-joomla-form.||
|params.suffix|"string"|нет|""|Suffix: Joomla form field suffix; input is validated and filtered according to x-joomla-form.||
|params.layout|"string"|нет|""|Layout: Joomla form field layout; input is validated and filtered according to x-joomla-form.||
|params.display_readonly|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
|params.searchindex|["integer", "string"]|нет|[0, 1, 2, 3, "0", "1", "2", "3"]|Search Index: Warning: When 'Make searchable' is selected, content from the field is indexed with the viewing permissions of the content item. This might lead to unexpected information disclosure.||
## administrator/components/com_fields/forms/filter_fields.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Fields: Search in field name, title or note. Prefix with ID: to search for a field ID. Prefix with AUTHOR: to search for a field author.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.group_id|"string"|нет|""|Field Group: Joomla form field group_id; input is validated and filtered according to x-joomla-form.||
|filter.assigned_cat_ids|["integer", "string"]|нет|""|Category: Joomla form field assigned_cat_ids; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter.only_use_in_subform|["integer", "string"]|нет|["", 0, 1, "0", "1"]|Only Use In Subform: Joomla form field only_use_in_subform; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.state ASC", "a.state DESC", "a.title ASC", "a.title DESC", "a.type ASC", "a.type DESC", "g.title ASC", "g.title DESC", "a.access ASC", "a.access DESC", "a.language ASC", "a.language DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_fields/forms/filter_groups.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search Field Groups: Search in field group title. Prefix with ID: to search for a field group ID.||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "a.ordering ASC", "a.ordering DESC", "a.state ASC", "a.state DESC", "a.title ASC", "a.title DESC", "a.access ASC", "a.access DESC", "a.language ASC", "a.language DESC", "a.id ASC", "a.id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_fields/forms/group.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|id|["integer", "string"]|нет|"0"|ID: Joomla form field id; input is validated and filtered according to x-joomla-form.||
|context|"string"|нет|""|context: Joomla form field context; input is validated and filtered according to x-joomla-form.||
|title|"string"|да|""|Title: Joomla form field title; input is validated and filtered according to x-joomla-form.||
|state|["integer", "string"]|нет|[1, 0, 2, -2, "1", "0", "2", "-2"]|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|created|"string"|нет|""|Created Date: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input.||
|created_by|["integer", "string"]|нет|""|Created By: Joomla form field created_by; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|note|"string"|нет|""|Note: Joomla form field note; input is validated and filtered according to x-joomla-form.||
|description|"string"|нет|""|Description: Joomla form field description; input is validated and filtered according to x-joomla-form.||
|access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|Group Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|ordering|["integer", "string"]|нет|""|Ordering: Joomla form field ordering; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
|params.display_readonly|["integer", "string"]|нет|[0, 1, "0", "1"]|Display When Read-Only: Joomla form field display_readonly; input is validated and filtered according to x-joomla-form.||
