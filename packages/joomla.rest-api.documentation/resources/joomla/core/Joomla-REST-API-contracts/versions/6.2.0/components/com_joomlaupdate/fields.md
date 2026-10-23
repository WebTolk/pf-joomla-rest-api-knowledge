# com_joomlaupdate: заполнение полей, Joomla 6.2.0

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

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/joomlaupdate/prepareUpdate

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|targetVersion|"string"|да|""|targetVersion: ||
## REST POST /v1/joomlaupdate/finalizeUpdate

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|fromVersion|"string"|нет|""|fromVersion: ||
|updateFileName|"string"|нет|""|updateFileName: ||
## REST POST /v1/joomlaupdate/notificationSuccess

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|fromVersion|"string"|нет|""|fromVersion: ||
|toVersion|"string"|нет|""|toVersion: ||
## REST POST /v1/joomlaupdate/notificationFailed

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|fromVersion|"string"|нет|""|fromVersion: ||
|toVersion|"string"|нет|""|toVersion: ||

## Инвентарь стандартных форм UI

## administrator/components/com_joomlaupdate/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|updatesource|"string"|нет|["default", "next", "custom"]|Update Channel: Joomla form field updatesource; input is validated and filtered according to x-joomla-form.||
|minimum_stability|["integer", "string"]|нет|[0, 1, 2, 3, 4, "0", "1", "2", "3", "4"]|Minimum Stability: The minimum stability of the Joomla updates you would like to see. Development is the least stable, Stable is production quality. If an update doesn't specify a level it is assumed to be Stable.||
|customurl|"string"|нет|""|Custom URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.|updatesource:custom|
|versioncheck|["integer", "string"]|нет|[0, 1, "0", "1"]|Potentially incompatible extensions checkbox: Shows the checkbox in the pre–update check if any of the extensions installed on your site is potentially incompatible with the version of Joomla you are upgrading to. Note: the checkbox is displayed when upgrading to a new Joomla version family (minor or major version).||
|backupcheck|["integer", "string"]|нет|[0, 1, "0", "1"]|Confirm Backup Checkbox: Shows the checkbox to confirm you have taken a backup and you're ready to update in the final step before the update is actually applied.||
|autoupdate|["integer", "string"]|нет|[0, 1, "0", "1"]|Automated Update: Automatically update Joomla to the latest version when it is available.|updatesource:default[AND]minimum_stability:4|
|autoupdate_status|"string"|нет|""|autoupdate_status: Joomla form field autoupdate_status; input is validated and filtered according to x-joomla-form.||
|update_token|"string"|нет|""|Update Token: This is the update token that this site uses to authenticate with the Joomla Automated Updates server. It is used to ensure that only your site can update itself.|updatesource:default[AND]minimum_stability:4[AND]autoupdate:1|
|update_last_check|"string"|нет|""|Last Checked: Calendar input. A date-only field uses YYYY-MM-DD. With time, use the effective form/language format (normally YYYY-MM-DD HH:mm:ss), in the effective API user timezone for USER_UTC; stored UTC is not interchangeable with local input. The last time the automated updates server could reach this site. If this date is too old, something is wrong with the automated updates and you should re-initiate the process by re-saving the configuration.|updatesource:default[AND]minimum_stability:4[AND]autoupdate:1|
|automated_updates_email_groups|"array"|нет|""|Send Email to User Groups: All users in the selected groups will receive the emails. If no users are found, the emails are sent to all Super Users. Recipients MUST have the Receive System Emails option enabled.|updatesource:default[AND]minimum_stability:4[AND]autoupdate:1|
