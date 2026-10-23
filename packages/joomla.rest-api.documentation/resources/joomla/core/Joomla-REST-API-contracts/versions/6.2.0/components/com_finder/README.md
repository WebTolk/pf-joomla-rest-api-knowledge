# com_finder REST API — Joomla 6.2.0

Пакет joomla.rest-api.finder. Версия ядра: 6.2.0.

В этих снимках отсутствуют штатные REST-маршруты индекса и поиска com_finder.
Не изобретать /v1/finder или REST-команду переиндексации. Настройки доступны
через com_config при допустимых ACL. Индекс, карты и поисковые фильтры управляются
штатным UI; включены схемы core-форм для точного заполнения.
Публикация статьи не доказывает её присутствие в поисковом индексе.
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


Самостоятельных REST-маршрутов ядра для компонента нет. См. операции владельца/config и UI fallback. Пустой paths не означает пропущенный API.

Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.
