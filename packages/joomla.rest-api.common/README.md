# joomla.rest-api.common

Пакет знаний ProcessForge. Версия пакета: 1.1.0. Основной выпуск Joomla: 6.2.0.

Source-pinned REST request, response, error, field and browser fallback knowledge; independent of tools and MCP.

## Использование

[Установка и обновление](https://github.com/WebTolk/pf-joomla-rest-api-knowledge/blob/v1.1.0/README.md). [Структура пакетов](https://github.com/WebTolk/pf-joomla-rest-api-knowledge/blob/v1.1.0/docs/knowledge-package-layout.md). [Лицензия](LICENSE).

Зависимости: joomla.rest-api.documentation.

Владелец файлов корпуса: joomla.rest-api.documentation. Корень пакетов: логический global; физический путь выбирается при установке.

## Ресурсы

| Resource ID | Версия данных | Содержимое |
|---|---|---|
|joomla.rest-api.common:common-contract|1.0.0|[Joomla REST common contract](../joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts/common/README.md)|
|joomla.rest-api.common:contracts-catalog|1.0.0|[Joomla REST component contract catalog](../joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts/README.md)|
|joomla.rest-api.common:validation|1.0.0|[Joomla REST contract validation](../joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts/validation.json)|

## Обновление

update_sites в package.yaml указывает на общий штатный сервер обновлений PF. Применение заменяет весь каталог пакета; пользовательские заметки храните отдельно. Пакеты устанавливаются в порядке: documentation, common, компоненты. Версии 5.4.8/6.1.3 архивные; для новой работы выбирать contract-6-2-0.
