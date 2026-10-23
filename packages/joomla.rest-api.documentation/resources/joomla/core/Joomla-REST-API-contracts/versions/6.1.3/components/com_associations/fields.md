# com_associations: заполнение полей, Joomla 6.1.3

В этих снимках нет самостоятельных маршрутов и webservices-плагина com_associations.
Не изобретать /v1/associations. Ассоциации заполняются через поддерживающие их
формы владельцев: обычно associations: {языковой_тег: ID}. Доступность зависит
от многоязычности, владельца и ACL. Язык * не является конкретной локализацией.
Операции вне API владельца выполняются через штатный интерфейс com_associations.
Набор допустимых языковых ключей задаётся профилем сайта. Динамическое поле
включено в схемы владельцев: статьи, контакты, категории, newsfeeds и пункты меню.
Пример PATCH /v1/content/articles/101:
{"language":"en-GB", "associations":{"ru-RU":102}}.
Передавать полный желаемый набор связей с записями соответствующего владельца.
У AdminModel пустой associations:{} пропускается и не означает «удалить все»;
для удаления из переданного непустого набора применяются 0/пустое значение.
Доступность требует включённых ассоциаций и более одного контентного языка;
категории дополнительно зависят от поддержки ассоциаций компонентом-владельцем.
Для снимка 6.1.3 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.


## Инвентарь стандартных форм UI

## administrator/components/com_associations/forms/association.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|itemlanguage|"string"|нет|""|Select Target Language: Joomla form field itemlanguage; input is validated and filtered according to x-joomla-form.||
|modalassociation|["integer", "string"]|нет|""|modalassociation: Joomla form field modalassociation; input is validated and filtered according to x-joomla-form.||
|params|"object"|нет|""|params: ||
## administrator/components/com_associations/forms/filter_associations.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|itemtype|"string"|нет|""|Select Item Type: Joomla form field itemtype; input is validated and filtered according to x-joomla-form.||
|language|"string"|нет|""|Select Language: Joomla form field language; input is validated and filtered according to x-joomla-form.||
|filter|"object"|нет|""|filter: ||
|filter.search|"string"|нет|""|Search item: Search an item by its title||
|filter.state|"string"|нет|""|Status: Joomla form field state; input is validated and filtered according to x-joomla-form.||
|filter.category_id|["integer", "string"]|нет|""|Category: Joomla form field category_id; input is validated and filtered according to x-joomla-form.||
|filter.menutype|"string"|нет|""|Menu: Joomla form field menutype; input is validated and filtered according to x-joomla-form.||
|filter.access|["integer", "string"]|нет|""|Access: Joomla form field access; input is validated and filtered according to x-joomla-form.||
|filter.level|["integer", "string"]|нет|""|Subcategory Levels: Joomla form field level; input is validated and filtered according to x-joomla-form.||
|list|"object"|нет|""|list: ||
|list.fullordering|"string"|нет|["", "state ASC", "state DESC", "title ASC", "title DESC", "access_level ASC", "access_level DESC", "id ASC", "id DESC"]|Sort Table By:: Joomla form field fullordering; input is validated and filtered according to x-joomla-form.||
|list.limit|"string"|нет|"25"|Select number of items per page.: Joomla form field limit; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_associations/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
