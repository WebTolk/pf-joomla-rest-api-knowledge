# com_contenthistory REST API — Joomla 6.2.0

Пакет joomla.rest-api.contenthistory. Версия ядра: 6.2.0.

GET history использует ID владельца и type_alias/type_id из маршрута.
PATCH history/keep и DELETE history используют числовой сегмент как ID версии;
одно имя id не означает одну сущность у всех действий.
keep переключает keep_forever, а не принимает вымышленное {keep:true}.
version_data — JSON-строка снимка. Перед использованием raw-источника проверить
соответствие текущей версии и изменяемой записи.
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
|GET|/v1/banners/{id}/contenthistory|history.displayList|source-derived|
|PATCH|/v1/banners/{id}/contenthistory/keep|history.keep|source-derived|
|DELETE|/v1/banners/{id}/contenthistory|history.delete|source-derived|
|GET|/v1/contacts/{id}/contenthistory|history.displayList|source-derived|
|PATCH|/v1/contacts/{id}/contenthistory/keep|history.keep|source-derived|
|DELETE|/v1/contacts/{id}/contenthistory|history.delete|source-derived|
|GET|/v1/content/articles/{id}/contenthistory|history.displayList|source-derived|
|PATCH|/v1/content/articles/{id}/contenthistory/keep|history.keep|source-derived|
|DELETE|/v1/content/articles/{id}/contenthistory|history.delete|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
