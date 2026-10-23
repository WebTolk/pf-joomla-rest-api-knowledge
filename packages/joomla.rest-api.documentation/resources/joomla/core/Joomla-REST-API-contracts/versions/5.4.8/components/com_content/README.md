# com_content REST API — Joomla 5.4.8

Пакет joomla.rest-api.content. Версия ядра: 5.4.8.

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

## Состав

- [openapi.json](openapi.json): схемы запросов/ответов, параметры, коды и примеры.
- [fields.md](fields.md): типы, обязательность, enum/default, правила форм/showon.
- [extension-parameters.json](extension-parameters.json): параметры штатных расширений.
- [examples.json](examples.json): синтетические request/response fixtures.
- [errors.md](errors.md), [browser-fallback.md](browser-fallback.md).
- [coverage.json](coverage.json), [source-evidence.json](source-evidence.json): покрытие/SHA-256.
- [Общие правила](../../../../common/README.md).

## Маршруты

| Метод | Путь | Действие | Поддержка |
|---|---|---|---|
|GET|/v1/content/articles|articles.displayList|source-derived|
|GET|/v1/content/articles/{id}|articles.displayItem|source-derived|
|POST|/v1/content/articles|articles.add|source-derived|
|PATCH|/v1/content/articles/{id}|articles.edit|source-derived|
|DELETE|/v1/content/articles/{id}|articles.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
