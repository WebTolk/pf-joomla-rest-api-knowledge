# Joomla REST API: независимые пакеты знаний

Основная версия: **Joomla 6.2.0**. Снимки 5.4.8 и 6.1.3 — архивные контракты. Каждый снимок имеет отдельные маршруты, схемы и evidence.

Начать с [общих правил](common/README.md). Параметры стандартных расширений включены; сторонние требуют своего профиля/пакета. Пакеты содержат знания о REST и формах, не требуют MCP или backend.

## Подключение

Общий ресурс: joomla.rest-api.common:common-contract. Пример точного компонентного ресурса: joomla.rest-api.content:contract-6-2-0. Выбирать версию ядра, а не произвольный newest. Версионный контракт имеет приоритет над типовыми примерами общего обзора.

| Пакет | Компонент |Joomla 6.2.0|Joomla 5.4.8|Joomla 6.1.3|
|---|---|---|---|---|
|joomla.rest-api.associations|com_associations|[Контракт](versions/6.2.0/components/com_associations/README.md)|[Контракт](versions/5.4.8/components/com_associations/README.md)|[Контракт](versions/6.1.3/components/com_associations/README.md)|
|joomla.rest-api.banners|com_banners|[Контракт](versions/6.2.0/components/com_banners/README.md)|[Контракт](versions/5.4.8/components/com_banners/README.md)|[Контракт](versions/6.1.3/components/com_banners/README.md)|
|joomla.rest-api.categories|com_categories|[Контракт](versions/6.2.0/components/com_categories/README.md)|[Контракт](versions/5.4.8/components/com_categories/README.md)|[Контракт](versions/6.1.3/components/com_categories/README.md)|
|joomla.rest-api.config|com_config|[Контракт](versions/6.2.0/components/com_config/README.md)|[Контракт](versions/5.4.8/components/com_config/README.md)|[Контракт](versions/6.1.3/components/com_config/README.md)|
|joomla.rest-api.contact|com_contact|[Контракт](versions/6.2.0/components/com_contact/README.md)|[Контракт](versions/5.4.8/components/com_contact/README.md)|[Контракт](versions/6.1.3/components/com_contact/README.md)|
|joomla.rest-api.content|com_content|[Контракт](versions/6.2.0/components/com_content/README.md)|[Контракт](versions/5.4.8/components/com_content/README.md)|[Контракт](versions/6.1.3/components/com_content/README.md)|
|joomla.rest-api.contenthistory|com_contenthistory|[Контракт](versions/6.2.0/components/com_contenthistory/README.md)|[Контракт](versions/5.4.8/components/com_contenthistory/README.md)|[Контракт](versions/6.1.3/components/com_contenthistory/README.md)|
|joomla.rest-api.fields|com_fields|[Контракт](versions/6.2.0/components/com_fields/README.md)|[Контракт](versions/5.4.8/components/com_fields/README.md)|[Контракт](versions/6.1.3/components/com_fields/README.md)|
|joomla.rest-api.finder|com_finder|[Контракт](versions/6.2.0/components/com_finder/README.md)|[Контракт](versions/5.4.8/components/com_finder/README.md)|[Контракт](versions/6.1.3/components/com_finder/README.md)|
|joomla.rest-api.installer|com_installer|[Контракт](versions/6.2.0/components/com_installer/README.md)|[Контракт](versions/5.4.8/components/com_installer/README.md)|[Контракт](versions/6.1.3/components/com_installer/README.md)|
|joomla.rest-api.joomlaupdate|com_joomlaupdate|[Контракт](versions/6.2.0/components/com_joomlaupdate/README.md)|[Контракт](versions/5.4.8/components/com_joomlaupdate/README.md)|[Контракт](versions/6.1.3/components/com_joomlaupdate/README.md)|
|joomla.rest-api.languages|com_languages|[Контракт](versions/6.2.0/components/com_languages/README.md)|[Контракт](versions/5.4.8/components/com_languages/README.md)|[Контракт](versions/6.1.3/components/com_languages/README.md)|
|joomla.rest-api.media|com_media|[Контракт](versions/6.2.0/components/com_media/README.md)|[Контракт](versions/5.4.8/components/com_media/README.md)|[Контракт](versions/6.1.3/components/com_media/README.md)|
|joomla.rest-api.menus|com_menus|[Контракт](versions/6.2.0/components/com_menus/README.md)|[Контракт](versions/5.4.8/components/com_menus/README.md)|[Контракт](versions/6.1.3/components/com_menus/README.md)|
|joomla.rest-api.messages|com_messages|[Контракт](versions/6.2.0/components/com_messages/README.md)|[Контракт](versions/5.4.8/components/com_messages/README.md)|[Контракт](versions/6.1.3/components/com_messages/README.md)|
|joomla.rest-api.modules|com_modules|[Контракт](versions/6.2.0/components/com_modules/README.md)|[Контракт](versions/5.4.8/components/com_modules/README.md)|[Контракт](versions/6.1.3/components/com_modules/README.md)|
|joomla.rest-api.newsfeeds|com_newsfeeds|[Контракт](versions/6.2.0/components/com_newsfeeds/README.md)|[Контракт](versions/5.4.8/components/com_newsfeeds/README.md)|[Контракт](versions/6.1.3/components/com_newsfeeds/README.md)|
|joomla.rest-api.plugins|com_plugins|[Контракт](versions/6.2.0/components/com_plugins/README.md)|[Контракт](versions/5.4.8/components/com_plugins/README.md)|[Контракт](versions/6.1.3/components/com_plugins/README.md)|
|joomla.rest-api.privacy|com_privacy|[Контракт](versions/6.2.0/components/com_privacy/README.md)|[Контракт](versions/5.4.8/components/com_privacy/README.md)|[Контракт](versions/6.1.3/components/com_privacy/README.md)|
|joomla.rest-api.redirect|com_redirect|[Контракт](versions/6.2.0/components/com_redirect/README.md)|[Контракт](versions/5.4.8/components/com_redirect/README.md)|[Контракт](versions/6.1.3/components/com_redirect/README.md)|
|joomla.rest-api.tags|com_tags|[Контракт](versions/6.2.0/components/com_tags/README.md)|[Контракт](versions/5.4.8/components/com_tags/README.md)|[Контракт](versions/6.1.3/components/com_tags/README.md)|
|joomla.rest-api.templates|com_templates|[Контракт](versions/6.2.0/components/com_templates/README.md)|[Контракт](versions/5.4.8/components/com_templates/README.md)|[Контракт](versions/6.1.3/components/com_templates/README.md)|
|joomla.rest-api.users|com_users|[Контракт](versions/6.2.0/components/com_users/README.md)|[Контракт](versions/5.4.8/components/com_users/README.md)|[Контракт](versions/6.1.3/components/com_users/README.md)|

[Машинная валидация](validation.json). Инвентарь получен без базы, сетевых вызовов и загрузки CMS. Примеры синтетические. Проверка данных сайта/ACL/результата записи обязательна и не является выяснением стандартной схемы.

## Основной контракт 6.2.0

[Машинный выбор ресурсов](common/current-contract.json). [Проверка всех обработчиков](common/current-api-audit-6.2.0.json).
