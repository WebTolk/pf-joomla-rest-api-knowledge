# joomla.rest-api.documentation

Пакет знаний ProcessForge. Версия пакета: 1.1.0. Основной выпуск Joomla: 6.2.0.

Joomla 6.2.0 REST API source-verified overview and exact component contracts.

## Использование

[Установка и обновление](https://github.com/WebTolk/pf-joomla-rest-api-knowledge/blob/v1.1.0/README.md). [Структура пакетов](https://github.com/WebTolk/pf-joomla-rest-api-knowledge/blob/v1.1.0/docs/knowledge-package-layout.md). [Лицензия](LICENSE).

Зависимости: нет.

Владелец файлов корпуса: joomla.rest-api.documentation. Корень пакетов: логический global; физический путь выбирается при установке.

## Ресурсы

| Resource ID | Версия данных | Содержимое |
|---|---|---|
|joomla.rest-api.documentation:rest-api-docs|6.2.0|[Joomla 6.2.0 REST API documentation](resources/joomla/core/Joomla-REST-API-docs/README.md)|

## Обновление

update_sites в package.yaml указывает на общий штатный сервер обновлений PF. Применение заменяет весь каталог пакета; пользовательские заметки храните отдельно. Пакеты устанавливаются в порядке: documentation, common, компоненты. Версии 5.4.8/6.1.3 архивные; для новой работы выбирать contract-6-2-0.
