# com_contact REST API — Joomla 6.2.0

Пакет joomla.rest-api.contact. Версия ядра: 6.2.0.

name/catid/язык/доступ относятся к карточке контакта. state означает регион
и является СТРОКОЙ; состояние публикации — published.
POST contacts/form/{id} отправляет сообщение, а не создаёт контакт. Поля:
contact_name/contact_email/contact_subject/contact_message/contact_email_copy.
Состав зависит от contact-плагинов и captcha. Автоматический повтор может
отправить письмо повторно; успешный ответ операции не является карточкой контакта.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

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
|POST|/v1/contacts/form/{id}|contact.submitForm|source-derived|
|GET|/v1/contacts|contact.displayList|source-derived|
|GET|/v1/contacts/{id}|contact.displayItem|source-derived|
|POST|/v1/contacts|contact.add|source-derived|
|PATCH|/v1/contacts/{id}|contact.edit|source-derived|
|DELETE|/v1/contacts/{id}|contact.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
