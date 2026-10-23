# com_joomlaupdate: браузерный fallback

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

1. Зафиксировать причину fallback и разрешённую операцию.
2. Открыть administrator/index.php?option=com_joomlaupdate и выбрать нужный client/context/язык/запись.
3. По fields.md сопоставить name/label/тип/showon. Для параметров выбрать схему соответствующего расширения.
4. Заполнить разрешённые поля, сохранить и заново открыть форму.
5. Проверить значения; при доступном API выполнить GET. Для публичных изменений проверить страницу.

Селекторы и подписи определяются фактической формой инстанса. Общие правила: ../../../../common/README.md.
