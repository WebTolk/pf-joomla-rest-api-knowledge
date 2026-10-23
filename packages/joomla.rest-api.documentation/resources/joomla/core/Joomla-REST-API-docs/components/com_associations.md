# com_associations REST API — Joomla 6.2.0

Пакет joomla.rest-api.associations. Версия ядра: 6.2.0.

В этих снимках нет самостоятельных маршрутов и webservices-плагина com_associations.
Не изобретать /v1/associations. Ассоциации заполняются через поддерживающие их
формы владельцев: обычно associations: {языковой_тег: ID}. Доступность зависит
от многоязычности, владельца и ACL. Язык * не является конкретной локализацией.
Операции вне API владельца выполняются через штатный интерфейс com_associations.
Набор допустимых языковых ключей задаётся профилем сайта. Динамическое поле
включено в схемы владельцев: статьи, контакты, категории, newsfeeds и пункты меню.
Пример PATCH /v1/content/articles/101:
{"language":"en-GB", "associations":{"ru-RU":102}}.
Передавать полный желаемый набор связей с записями соответствующего владельца.
У AdminModel пустой associations:{} пропускается и не означает «удалить все»;
для удаления из переданного непустого набора применяются 0/пустое значение.
Доступность требует включённых ассоциаций и более одного контентного языка;
категории дополнительно зависят от поддержки ассоциаций компонентом-владельцем.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.


## Контракты данных

- [OpenAPI 3.1: запросы, ответы, типы, ошибки и примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_associations/openapi.json)
- [Заполнение REST и UI-форм](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_associations/fields.md)
- [Примеры](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_associations/examples.json)
- [Сверка Postman](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_associations/postman-crosscheck.md)
- [Браузерный fallback](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_associations/browser-fallback.md)
- [Покрытие и SHA-256](../../Joomla-REST-API-contracts/versions/6.2.0/components/com_associations/source-evidence.json)

## Операции

| Метод | Путь | Обработчик | Поддержка |
|---|---|---|---|

Самостоятельного REST API компонента в ядре нет. Использовать документированные операции владельца/config или UI в границах задания.

Примеры синтетические; результат записи проверяется независимо. ID, ACL и сторонние расширения задаются профилем сайта. Контракт относится только к 6.2.0.
