# Joomla REST API — пакеты знаний ProcessForge

Это **пакеты знаний для ProcessForge (PF)**: схемы REST API Joomla, типы и правила
заполнения полей, примеры запросов и ответов, ошибки и браузерный fallback.
Основная версия Joomla — **6.2.0**; контракты 5.4.8 и 6.1.3 сохранены как архивные.
Код сайта и MCP-сервер для использования знаний не требуются.

Версия дистрибутива знаний: **1.1.0**. Она меняется независимо от версии Joomla
и выпуска ядра PF. В составе 25 пакетов и 73 ресурса.

## Что читать

- [Каталог контрактов Joomla](packages/joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts/README.md).
- [Общие правила REST](packages/joomla.rest-api.documentation/resources/joomla/core/Joomla-REST-API-contracts/common/README.md).
- [Предлагаемая общая структура пакета знаний](docs/knowledge-package-layout.md).
- [Контракт обновления и проверенная реализация PF](docs/native-updater.md).
- [Состав дистрибутива](bundle.json), [история изменений](CHANGELOG.md).

`README.md` — единый человеческий вход в пакет. `package.yaml` и
`indexes/resource-index.yaml` содержат машиночитаемое описание PF.

## Структура

```text
README.md
LICENSE
NOTICE.md
CHANGELOG.md
bundle.json                         # каталог этого репозитория
packages/
  joomla.rest-api.documentation/     # владелец общего корпуса
    README.md
    package.yaml
    indexes/resource-index.yaml
    resources/joomla/core/
      Joomla-REST-API-contracts/
      Joomla-REST-API-docs/
  joomla.rest-api.common/
    README.md
    package.yaml
    indexes/resource-index.yaml
  joomla.rest-api.content/            # аналогично остальные компоненты
updates/joomla-rest-api.json          # штатный сервер обновлений PF
docs/
templates/
tools/
evidence/
```

`joomla.rest-api.documentation` хранит весь корпус один раз. Общий и компонентные
пакеты ссылаются на него через `path_ref` и объявляют зависимости. При обновлении
этого пакета обновляются и сами файлы знаний. Внешнее дерево исходников Joomla
для чтения контрактов не нужно; оно служило источником при подготовке.

## Установка: инструкция агенту

**Окончательное расположение выбирает агент-установщик** по актуальному контексту,
реестрам и правилам принимающего workplace. Ниже предлагается структура, а не
фиксированные пути конкретного компьютера.

1. Прочитать правила принимающего PF, определить workplace и разрешённый корень
   из `registries/package-roots.yaml`. Сверить наличие пакетов с такими же ID,
   их происхождение, версии и локальные изменения.
2. Скачать проверенный [релиз](https://github.com/WebTolk/pf-joomla-rest-api-knowledge/releases)
   и сверить `SHA256SUMS`. Общий ZIP предназначен для первичной распаковки
   дистрибутива. Для `update stage/verify/apply` используются отдельные ZIP пакетов,
   на которые указывает сервер обновлений.
3. Предлагаемое размещение: `<package-root>/<package-id>/package.yaml`, рядом
   `README.md`, `indexes/`, а у владельца корпуса — `resources/`.
   Крупный исходник Joomla и служебные файлы workplace в этот дистрибутив не входят.
4. Архивы используют логический `package_roots:global`. Физический путь за этим
   ID выбирается локально. Он не обязан быть `<workplace>/packages`.
   Если workplace использует другой логический ID, до установки согласовать
   отображение корня: распаковка ZIP сама не переписывает `path_ref`.
5. Установить владельца `joomla.rest-api.documentation`, затем
   `joomla.rest-api.common`, затем нужные компонентные пакеты. Для полного комплекта
   использовать список и зависимости из `bundle.json`.
6. Зарегистрировать пакеты и ресурсы штатными средствами установленного PF,
   обновить пакетные индексы и агрегатный реестр знаний. Зафиксировать каждый
   установленный `knowledge_package`, его версию и **реальный install_path**
   в локальном реестре installed subjects через поддерживаемые средства PF.
   Это нужно для последующих обновлений в выбранный агентом каталог.
7. Выполнить package doctors, проверить разрешение ресурсов и зависимости;
   после подключения к процессу обновить его контекст. Существующие закреплённые
   execution capsules сохраняют свои версии до штатного перехода.

Сервер не задаёт `install_path`: путь установленного субъекта остаётся локальным.
Не заменять целиком чужие реестры, не перенаправлять существующие knowledge roots
и не затирать отличающиеся пакеты без обработки обнаруженного конфликта.
Пользовательские заметки хранить отдельно от обновляемого каталога пакета.

## Подключение знаний

Сначала загрузить `joomla.rest-api.common:common-contract`, затем точный ресурс
компонента, например `joomla.rest-api.content:contract-6-2-0`.
Сохраняется вход `joomla.rest-api.documentation:rest-api-docs`.
В компонентах `associations` и `finder` описано отсутствие самостоятельных
штатных REST-маршрутов и доступные операции владельцев/config/UI.

Пакеты содержат схемы ядра. ID, ACL, включённые языки/плагины, адаптеры и схемы
сторонних расширений задаются профилем конкретного сайта. Примеры синтетические;
после записи на сайт требуется независимая проверка результата.

## Обновления

Манифест сервера:
[updates/joomla-rest-api.json](https://raw.githubusercontent.com/WebTolk/pf-joomla-rest-api-knowledge/main/updates/joomla-rest-api.json).

Каждый `package.yaml` объявляет `update_sites`. Манифест использует штатный
нормализованный формат PF: `schema_version`, `product`, `subjects[].versions[]`,
канал `stable`, ZIP-артефакты и SHA-256. ZIP содержит `package.yaml` в корне,
его ID/type/version совпадают с субъектом обновления. Файлы знаний входят в ZIP
владельца, поэтому их доставка не требует удалённого postinstall-скрипта.

Обычный цикл встроенного апдейтера из каталога установленного PF:

```bash
python bin/pf.py update entity-sources rebuild --workplace <workplace>
python bin/pf.py update candidates refresh --workplace <workplace>
python bin/pf.py update candidates list --workplace <workplace>
python bin/pf.py update stage --workplace <workplace> --candidate <candidate-id>
python bin/pf.py update verify --workplace <workplace> --candidate <candidate-id>
python bin/pf.py update apply --workplace <workplace> --candidate <candidate-id> --confirm
```

Знания выпускаются и обнаруживаются отдельно от ядра PF. `auto_check: true` и
интервал 24 часа задают политику проверки источника; манифест не запускает
планировщик сам. В проверенной реализации PF 1.2.0 применение требует `--confirm`,
а `auto_apply` не включает фоновую установку. Порядок обновления — владелец,
common, компоненты; штатный rollback сохраняется. Политика принимающего workplace
может закрепить версию, отключить источник или потребовать ручное применение.
Для PF 1.2.0 обнаружено [ограничение rollback реестра версий](docs/native-updater.md#обнаруженное-ограничение-pf-120),
которое установщик должен учитывать после отката файлов.

## Проверка и выпуск следующей версии

```bash
python -m pip install -r requirements.txt
python tools/check_bundle.py
python tools/build_release.py
```

Обновить знания, поднять версии пакетов и `bundle.json`, описать изменение в
`CHANGELOG.md`, проверить совместимость с установленным PF и опубликовать новые
ZIP в GitHub Release. Затем обновить основной манифест в `main`.
У опубликованной версии сохраняются артефакты и контрольные суммы; исправление
оформляется новой версией. См. [подробный порядок](docs/native-updater.md).

## Происхождение и лицензия

Схемы подготовлены по локальным снимкам Joomla с контрольными суммами исходников;
сопоставление с Postman включено как дополнительная проверка.
[Доказательства](evidence/) описывают статическую и локальную проверку, а не
live acceptance сайта. [Лицензия GPL-2.0-or-later](LICENSE), [атрибуция](NOTICE.md).
