# com_finder REST API — Joomla 6.2.0

Пакет joomla.rest-api.finder. Версия ядра: 6.2.0.

В этих снимках отсутствуют штатные REST-маршруты индекса и поиска com_finder.
Не изобретать /v1/finder или REST-команду переиндексации. Настройки доступны
через com_config при допустимых ACL. Индекс, карты и поисковые фильтры управляются
штатным UI; включены схемы core-форм для точного заполнения.
Публикация статьи не доказывает её присутствие в поисковом индексе.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_finder/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_finder/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_finder/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_finder/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_finder/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_finder/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|

Самостоятельного REST API компонента в ядре нет. Использовать документированные операции владельца/config или UI в границах задания.

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
