# com_privacy REST API — Joomla 6.1.3

Пакет joomla.rest-api.privacy. Версия ядра: 6.1.3.

Списки/элементы запросов и согласий, а также экспорт требуют core.admin
на com_privacy в API-контроллерах. Удаление consent не имеет REST-маршрута.
Экспорт требует request_type=export и подтверждённый status=1; иначе модель
не возвращает данные, представление вызывает RouteNotFoundException.
Результат формируется privacy-плагинами; REST export не равнозначен файлу
экспорта в админке. Подробности фактической сериализации см. в схеме ответа.
Для снимка 6.1.3 не переносить правила PATCH/ACL и новые поля из 6.2.0. Пропущенные календарные колонки могут повторно пройти UTC-фильтр; после записи сравнивать даты.

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
|GET|/v1/privacy/requests|requests.displayList|source-derived|
|GET|/v1/privacy/requests/{id}|requests.displayItem|source-derived|
|GET|/v1/privacy/requests/export/{id}|requests.export|source-derived|
|POST|/v1/privacy/requests|requests.add|source-derived|
|GET|/v1/privacy/consents|consents.displayList|source-derived|
|GET|/v1/privacy/consents/{id}|consents.displayItem|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
