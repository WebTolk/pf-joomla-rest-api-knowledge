# Joomla 6.2.0 REST API

Документация обновлена по фактическим webservices-маршрутам, контроллерам, моделям, XML-формам и JSON:API-представлениям зарегистрированного исходника Joomla 6.2.0. Это основной выпуск; старые контракты доступны отдельно в [каталоге версий](../Joomla-REST-API-contracts/README.md).

База: `/api/index.php`. Accept: `application/vnd.api+json`; Content-Type записи JSON: `application/json`. Основной заголовок авторизации: `X-Joomla-Token`; Basic зависит от включённого API-плагина. Bearer не является универсальным способом аутентификации Joomla. Автообновление использует отдельный `X-JUpdate-Token`.

Обычный CRUD принимает плоское тело; POST/PATCH обычно возвращают 200, DELETE — 204. Специальные обработчики могут ограничивать ключи и формат тела. Общая XML-форма админки не равна writable-схеме REST.

[Общие правила и границы применения](../Joomla-REST-API-contracts/common/README.md). [Полная машинная валидация](../Joomla-REST-API-contracts/validation.json).

| Компонент | Операции | Документация |
|---|---|---|
|com_associations|0|[Контракт](components/com_associations.md)|
|com_banners|10|[Контракт](components/com_banners.md)|
|com_categories|20|[Контракт](components/com_categories.md)|
|com_config|4|[Контракт](components/com_config.md)|
|com_contact|6|[Контракт](components/com_contact.md)|
|com_content|5|[Контракт](components/com_content.md)|
|com_contenthistory|9|[Контракт](components/com_contenthistory.md)|
|com_fields|60|[Контракт](components/com_fields.md)|
|com_finder|0|[Контракт](components/com_finder.md)|
|com_installer|3|[Контракт](components/com_installer.md)|
|com_joomlaupdate|6|[Контракт](components/com_joomlaupdate.md)|
|com_languages|17|[Контракт](components/com_languages.md)|
|com_media|8|[Контракт](components/com_media.md)|
|com_menus|22|[Контракт](components/com_menus.md)|
|com_messages|5|[Контракт](components/com_messages.md)|
|com_modules|12|[Контракт](components/com_modules.md)|
|com_newsfeeds|5|[Контракт](components/com_newsfeeds.md)|
|com_plugins|3|[Контракт](components/com_plugins.md)|
|com_privacy|6|[Контракт](components/com_privacy.md)|
|com_redirect|5|[Контракт](components/com_redirect.md)|
|com_tags|5|[Контракт](components/com_tags.md)|
|com_templates|10|[Контракт](components/com_templates.md)|
|com_users|15|[Контракт](components/com_users.md)|

Всего: **236 зарегистрированных операций**; 21 компонент-владелец REST и 2 дополнительных пакета без вымышленных endpoints.

[Сверка с экспортом Postman](POSTMAN-CHECK-REPORT.md). Примеры не являются live acceptance.
