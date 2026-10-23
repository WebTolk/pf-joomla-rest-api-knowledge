# com_joomlaupdate REST API — Joomla 6.2.0

Пакет joomla.rest-api.joomlaupdate. Версия ядра: 6.2.0.

Требуется X-JUpdate-Token и включённое автообновление с допустимыми
updatesource/minimum_stability. Это отдельный токен, не X-Joomla-Token.
Неверный/пропущенный token вызывает InvalidParameterException с code=403,
но обработчик выставляет HTTP 400. HTTP и внутренний code различаются.
prepareUpdate требует доступную targetVersion; иначе generic Exception с code=410
преобразуется стандартным fallback formatter в HTTP 500 и code=500.
finalizeUpdate принимает fromVersion/updateFileName; имя очищается до basename.
success=false/errors при HTTP 200 означает неуспешное действие.
password prepareUpdate — временный секрет, в артефакты реальные значения не входят.
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
|GET|/v1/joomlaupdate/healthcheck|healthcheck.show|source-derived|
|GET|/v1/joomlaupdate/getUpdate|updates.getUpdate|source-derived|
|POST|/v1/joomlaupdate/prepareUpdate|updates.prepareUpdate|source-derived|
|POST|/v1/joomlaupdate/finalizeUpdate|updates.finalizeUpdate|source-derived|
|POST|/v1/joomlaupdate/notificationSuccess|notification.success|source-derived|
|POST|/v1/joomlaupdate/notificationFailed|notification.failed|source-derived|


Для сторонних полей подключается профиль/пакет расширения. Исходники не являются обязательным runtime-входом потребителя знаний.

## Проверка реализации

[Обработчики и контракты всех операций](implementation-audit.json).
