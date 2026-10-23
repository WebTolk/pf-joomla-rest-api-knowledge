# Сверка Joomla 6.1.3 → 6.2.0

- Маршруты: 236 → 236.
- Добавлено: 0; удалено: 0.
- Изменённые наборы полей JsonApiView: 1.
- Изменённые схемы форм: 13.
- Изменённые файлы API/форм/моделей: 50.

Сверка статическая, по зарегистрированным исходникам. Это не live acceptance.
Новая версия имеет собственные OpenAPI-файлы, поля, примеры и source-evidence.

## Изменённые формы

- administrator/components/com_config/forms/application.xml
- administrator/components/com_contact/config.xml
- administrator/components/com_content/config.xml
- administrator/components/com_content/forms/article.xml
- administrator/components/com_fields/forms/filter_fields.xml
- administrator/components/com_joomlaupdate/config.xml
- administrator/components/com_languages/config.xml
- administrator/components/com_newsfeeds/config.xml
- administrator/components/com_newsfeeds/forms/newsfeed.xml
- components/com_contact/tmpl/category/default.xml
- components/com_content/tmpl/category/blog.xml
- components/com_content/tmpl/category/default.xml
- components/com_newsfeeds/tmpl/category/default.xml

## Изменённые исходники

- administrator/components/com_actionlogs/src/Model/ActionlogModel.php
- administrator/components/com_admin/src/Model/HelpModel.php
- administrator/components/com_admin/src/Model/SysinfoModel.php
- administrator/components/com_banners/src/Model/TracksModel.php
- administrator/components/com_cache/src/Model/CacheModel.php
- administrator/components/com_categories/src/Model/CategoryModel.php
- administrator/components/com_config/forms/application.xml
- administrator/components/com_config/src/Model/ApplicationModel.php
- administrator/components/com_config/src/Model/ComponentModel.php
- administrator/components/com_content/forms/article.xml
- administrator/components/com_content/src/Model/ArticleModel.php
- administrator/components/com_contenthistory/src/Model/CompareModel.php
- administrator/components/com_fields/src/Model/FieldModel.php
- administrator/components/com_finder/src/Model/IndexModel.php
- administrator/components/com_finder/src/Model/MapsModel.php
- administrator/components/com_guidedtours/src/Model/TourModel.php
- administrator/components/com_installer/src/Model/UpdatesitesModel.php
- administrator/components/com_joomlaupdate/src/Model/NotificationModel.php
- administrator/components/com_joomlaupdate/src/Model/UpdateModel.php
- administrator/components/com_languages/src/Model/LanguageModel.php
- administrator/components/com_mails/src/Model/TemplateModel.php
- administrator/components/com_media/src/Model/ApiModel.php
- administrator/components/com_menus/src/Model/ItemModel.php
- administrator/components/com_menus/src/Model/MenuModel.php
- administrator/components/com_messages/src/Model/MessageModel.php
- administrator/components/com_modules/src/Model/ModuleModel.php
- administrator/components/com_newsfeeds/forms/newsfeed.xml
- administrator/components/com_postinstall/src/Model/MessagesModel.php
- administrator/components/com_privacy/src/Model/ExportModel.php
- administrator/components/com_privacy/src/Model/RequestModel.php
- administrator/components/com_tags/src/Model/TagModel.php
- administrator/components/com_templates/src/Model/StyleModel.php
- administrator/components/com_templates/src/Model/TemplateModel.php
- administrator/components/com_users/src/Model/BackupcodesModel.php
- administrator/components/com_users/src/Model/LevelModel.php
- administrator/components/com_users/src/Model/MailModel.php
- administrator/components/com_users/src/Model/NoteModel.php
- administrator/components/com_users/src/Model/UserModel.php
- administrator/components/com_workflow/src/Model/StageModel.php
- administrator/components/com_workflow/src/Model/TransitionModel.php
- administrator/components/com_workflow/src/Model/WorkflowModel.php
- api/components/com_categories/src/Controller/CategoriesController.php
- api/components/com_contact/src/Controller/ContactController.php
- api/components/com_content/src/View/Articles/JsonapiView.php
- api/components/com_fields/src/Controller/FieldsController.php
- api/components/com_fields/src/Controller/GroupsController.php
- api/components/com_joomlaupdate/src/View/Healthcheck/JsonapiView.php
- api/components/com_users/src/Controller/GroupsController.php
- api/components/com_users/src/Controller/LevelsController.php
- libraries/src/MVC/Controller/ApiController.php




## Что изменено в знаниях 6.2.0

- В list/item статей добавлены introtext/fulltext; text помечен deprecated (удаление в 8.0). Контентные плагины могут изменять объект ответа.
- ApiController возвращает сохранённые UTC-значения пропущенных PATCH-полей SERVER_UTC/USER_UTC после валидации, предотвращая вторую конвертацию. Явно переданные даты продолжают фильтроваться.
- Базовый allowEdit проверяет core.manage и права конкретной записи core.edit либо core.edit.own с владельцем. Переопределения компонентов сохраняют приоритет. Для viewlevels com_users в 6.2.0 требуется core.admin.
- В списке категорий появился filter[state] (INT), передаваемый в filter.published.
- smtpauth изменён с boolean на варианты 0/1/2, добавлены smtp_oauth2_* и условия showon. Браузерная авторизация OAuth не объявляется REST-операцией.
- В images статей добавлены imgclass_intro/imgclass_fulltext; float_intro/float_fulltext относятся к figure class. URL newsfeed ограничен схемами http/https.

Контракты 5.4.8/6.1.3 сохранены отдельно. Сведения 6.2.0 не перенесены на другие выпуски без проверки. Поля, параметры и примеры 6.2.0 пересобраны из собственного снимка; SHA-256 исходников проверены валидатором.
