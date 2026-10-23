# joomla.rest-api.languages

Пакет знаний ProcessForge. Версия пакета: 1.1.0. Основной выпуск Joomla: 6.2.0.

Versioned Joomla REST schemas, field semantics, responses, errors and browser fallback. Knowledge only; no tools or MCP.

## Использование

[Установка и обновление](https://github.com/WebTolk/pf-joomla-rest-api-knowledge/blob/v1.1.0/README.md). [Структура пакетов](https://github.com/WebTolk/pf-joomla-rest-api-knowledge/blob/v1.1.0/docs/knowledge-package-layout.md). [Лицензия](LICENSE).

Зависимости: joomla.rest-api.documentation, joomla.rest-api.common.

Владелец файлов корпуса: joomla.rest-api.documentation. Корень пакетов: логический global; физический путь выбирается при установке.

## Ресурсы

| Resource ID | Версия данных | Содержимое |
|---|---|---|
|joomla.rest-api.languages:contract-5-4-8|5.4.8|[Joomla 5.4.8 com_languages REST contract](../joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts/versions/5.4.8/components/com_languages/README.md)|
|joomla.rest-api.languages:contract-6-1-3|6.1.3|[Joomla 6.1.3 com_languages REST contract](../joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts/versions/6.1.3/components/com_languages/README.md)|
|joomla.rest-api.languages:contract-6-2-0|6.2.0|[Joomla 6.2.0 com_languages REST contract](../joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts/versions/6.2.0/components/com_languages/README.md)|

## Обновление

update_sites в package.yaml указывает на общий штатный сервер обновлений PF. Применение заменяет весь каталог пакета; пользовательские заметки храните отдельно. Пакеты устанавливаются в порядке: documentation, common, компоненты. Версии 5.4.8/6.1.3 архивные; для новой работы выбирать contract-6-2-0.
