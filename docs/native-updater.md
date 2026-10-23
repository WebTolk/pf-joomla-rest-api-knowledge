# Совместимость со встроенным апдейтером PF

Контракт проверяется по установленному исходнику **ProcessForge 1.2.0**:

- `schemas/normalized-update-manifest.schema.json`;
- `tools/processforge.py`: update manifest validate, candidates refresh,
  stage, verify, apply, rollback, artifact_manifest_from_zip;
- `src/processforge_core/maintenance/versions.py`: нормализация subjects;
- `src/processforge_core/maintenance/registries.py`: выбор install_path;
- штатные smoke-сценарии knowledge package release и file-provider update.

Внешний сервер данного репозитория использует нормализованный формат:

```text
schema_version: 1
product: { id: webtolk.joomla-rest-api-knowledge }
generated_at: <UTC>
subjects:
  - type: knowledge_package
    id: <package-id>
    versions:
      - version: <package-version>
        channels: [stable]
        stability: stable
        prerelease: false
        yanked: false
        source: <release provenance>
        artifacts:
          - type: knowledge_package
            format: zip
            url: <HTTPS release asset>
            sha256: <64 hex>
```

Настоящий JSON: [сервер обновлений](../updates/joomla-rest-api.json).
Каждый пакет имеет `update_sites` с URL сервера и changelog. При discovery PF
выбирает subject по ID, версии канала и установленной версии. При verify сверяет
checksum, ID/type/version из `package.yaml` архива. Значения `compatibility` и
`dependencies` в сервере описывают требования, но текущий нормализатор не
обеспечивает полноценное автоматическое разрешение зависимостей: порядок
documentation → common → компоненты проверяет установщик/оператор.

## Почему корпус включён в пакет

`update apply` делает backup и заменяет целиком установленный каталог субъекта.
Он не синхронизирует произвольные внешние knowledge_roots и не выполняет
удалённые postinstall-команды. Поэтому ZIP documentation содержит и реальные
данные под `resources/`, и описывающий их манифест. Остальные ZIP содержат свои
манифесты/индексы и ссылаются на владельца корпуса.

## Выбор установки

Нативный выбор пути: `candidate.update_policy.install_path`, затем install_path
локального установленного субъекта, затем fallback `<workplace>/packages/<id>`.
Публичный сервер и policy этого комплекта не задают install_path. Установщик
записывает выбранное размещение локально. Проверка обновления должна подтвердить,
что обновлён этот каталог, а fallback не создан по ошибке.

ZIP не переписывает свои path_ref. Архивы используют логический корень global;
его путь в принимающем реестре выбирается локально. Все связанные пакеты должны
видеть один согласованный корень. Перенос логических root IDs требует отдельной
адаптации артефактов, а не только выбора другой папки распаковки.

## Автоматическое обнаружение и применение

Обновления знаний выходят независимо от PF Core. auto_check разрешает проверку
по принятой локальной политике. Источник не устанавливает планировщик или службу.
В проверенной реализации `update apply` требует `--confirm`; `auto_apply: true`
в записи источника не превращает эту команду в фоновую установку.
Манифест использует auto_check=true, auto_stage=false, auto_apply=false.

После применения надо проверить package doctors и зависимости, актуальность
агрегатного реестра и индексов, затем refresh контекста. Сам updater не заменяет
все эти проверки фактом успешной распаковки. Проверка полнотекстового поиска
отдельна от проверки доставки ZIP. Rollback выполняется штатной командой PF.

## Обнаруженное ограничение PF 1.2.0

В изолированной проверке `update rollback` восстановил файлы и прежний
`package.yaml` всех 25 пакетов, но не вернул версии в installed-subjects.yaml:
там осталась 1.1.0 вместо восстановленной 1.0.0. Это ограничение проверенной
реализации PF, а не формат сервера знаний. После rollback требуется отдельно
сверить и согласовать локальный реестр установленных субъектов с манифестами,
прежде чем полагаться на последующее обнаружение версий. Успех восстановления
файлов не считается доказательством полного отката регистрационных данных.
См. [проверку](../evidence/native-updater-local.json).

## Выпуск

1. Обновить корпус и доказательства проверок, README и CHANGELOG.
2. Поднять версию в bundle.json и манифестах выбранного согласованного комплекта.
3. `python tools/check_bundle.py` и `python tools/build_release.py`.
4. Проверить сервер командой PF `update manifest validate --file updates/joomla-rest-api.json`.
5. Проверить локальный lifecycle в отдельном workplace; реальный workplace автора
   не использовать как стенд установки.
6. Зафиксировать исходники и тег v&lt;version&gt;; опубликовать ZIP и SHA256SUMS
   в GitHub Release этого тега.
7. Проверить публичные URL/SHA и обновить стабильный manifest в main.

Сначала доступны артефакты, затем указатель новой версии. Manifest не должен
указывать на ещё не опубликованный ZIP. В опубликованном релизе не изменять
артефакт под прежним номером версии.
