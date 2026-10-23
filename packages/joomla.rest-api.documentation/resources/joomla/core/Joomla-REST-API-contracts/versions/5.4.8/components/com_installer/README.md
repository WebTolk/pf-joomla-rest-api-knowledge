# com_installer REST API — Joomla 5.4.8

Пакет joomla.rest-api.installer. Версия ядра: 5.4.8.

GET extensions перечисляет расширения; GET languages — доступные языковые пакеты.
POST languages -> languages.install зарегистрирован, но метод install отсутствует
в API LanguagesController и ApiController этих снимков. Он отмечен как
registered-unimplemented: успешный ответ не выдумывается. Установка через UI
требует соответствующей области задания.
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
|GET|/v1/extensions|manage.displayList|source-derived|
|GET|/v1/languages|languages.displayList|source-derived|
|POST|/v1/languages|languages.install|registered-unimplemented|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
