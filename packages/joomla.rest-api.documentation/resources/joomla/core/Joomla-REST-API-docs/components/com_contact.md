# com_contact REST API — Joomla 6.2.0

Пакет joomla.rest-api.contact. Версия ядра: 6.2.0.

name/catid/язык/доступ относятся к карточке контакта. state означает регион
и является СТРОКОЙ; состояние публикации — published.
POST contacts/form/{id} отправляет сообщение, а не создаёт контакт. Поля:
contact_name/contact_email/contact_subject/contact_message/contact_email_copy.
Состав зависит от contact-плагинов и captcha. Автоматический повтор может
отправить письмо повторно; успешный ответ операции не является карточкой контакта.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contact/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contact/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contact/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contact/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contact/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_contact/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|
|POST|/v1/contacts/form/{id}|contact.submitForm|source-derived|
|GET|/v1/contacts|contact.displayList|source-derived|
|POST|/v1/contacts|contact.add|source-derived|
|GET|/v1/contacts/{id}|contact.displayItem|source-derived|
|PATCH|/v1/contacts/{id}|contact.edit|source-derived|
|DELETE|/v1/contacts/{id}|contact.delete|source-derived|

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
