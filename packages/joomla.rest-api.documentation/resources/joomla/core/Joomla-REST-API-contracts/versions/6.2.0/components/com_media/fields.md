# com_media: заполнение полей, Joomla 6.2.0

path включает адаптер, например local-images:/example.webp; ID адаптера — данные сайта.
GET files/{path}/ с завершающим / возвращает список, без / — элемент.
POST требует path; для файла нужен base64 content, для папки content отсутствует.
POST override по умолчанию false; PATCH override по умолчанию true: для запрета
перезаписи явно передавать false. В PATCH path тела — новый путь, URL path — старый.
Нужен хотя бы path или content. Не передавать multipart, data: URL или сырые байты.
Лимиты размера, допустимые MIME/расширения и возможности определяются настройками
и адаптером. content/url/tempUrl в ответе условны.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST POST /v1/media/files

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|path|"string"|да|""|path: Adapter-prefixed path||
|content|"string"|нет|""|content: Nonempty base64-encoded file content. Empty/false decoded content is treated as a folder; zero-byte uploads and decoded string '0' are not reliable file creation.||
|override|"boolean"|нет|false|override: ||
## REST PATCH /v1/media/files/{path}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|path|"string"|нет|""|path: Adapter-prefixed path||
|content|"string"|нет|""|content: Nonempty base64-encoded file content. Empty/false decoded content is treated as a folder; zero-byte uploads and decoded string '0' are not reliable file creation.||
|override|"boolean"|нет|true|override: ||

## Инвентарь стандартных форм UI

## administrator/components/com_media/forms/file.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
## administrator/components/com_media/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|upload_maxsize|["integer", "string"]|нет|"10"|Maximum Size (in MB): Use zero for no limit. Note: your server has a maximum limit.||
|file_path|"string"|нет|"files"|Path to Files Folder: Enter the path to the files folder relative to the root of your webspace. Warning! Changing to another path than the default 'images' may break your links. Note: Do not start the path with a slash!||
|image_path|"string"|нет|"images"|Path to Images Folder: Enter the path to the images folder relative to the root of your webspace. This path <strong>has to be the same as path to files (default) or to a subfolder of the path to file folder.</strong> Note: Do not start the path with a slash!||
|restrict_uploads|["integer", "string"]|нет|[0, 1, "0", "1"]|Restrict Uploads: Restrict uploads for lower than manager users to images if Fileinfo or MIME Magic isn't installed.||
|restrict_uploads_extensions|"string"|нет|"bmp,gif,jpg,jpeg,png,webp,avif,ico,mp3,mp4,odg,odp,ods,odt,pdf,ppt,txt,xcf,xls,csv"|Allowed Extensions: Restrict uploads for lower than manager users to files in the list.|restrict_uploads:1|
|check_mime|["integer", "string"]|нет|[0, 1, "0", "1"]|Check MIME Types: Use MIME Magic or Fileinfo to attempt to verify files. Try disabling this if you get invalid mime type errors.|restrict_uploads:1|
|image_extensions|"string"|нет|"bmp,gif,jpg,jpeg,png,webp,avif"|Legal Image Extensions (File Types): Image extensions (file types) you are allowed to upload (comma separated). These are used to check for valid image headers.||
|audio_extensions|"string"|нет|"mp3,m4a,mp4a,ogg"|Legal Audio Extensions (File Types): Audio extensions (file types) you are allowed to upload (comma separated). These are used to check for valid audio headers.||
|video_extensions|"string"|нет|"mp4,mp4v,mpeg,mov,webm"|Legal Video Extensions (File Types): Video extensions (file types) you are allowed to upload (comma separated). These are used to check for valid video headers.||
|doc_extensions|"string"|нет|"doc,odg,odp,ods,odt,pdf,ppt,txt,xcf,xls,csv"|Legal Document Extensions (File Types): Document extensions (file types) you are allowed to upload (comma separated). These are used to check for valid document headers.||
|ignore_extensions|"string"|нет|""|Ignored Extensions: Ignored file extensions for MIME type checking and restricted uploads.||
|upload_mime|"string"|нет|"image/jpeg,image/gif,image/png,image/bmp,image/webp,image/avif,audio/ogg,audio/mpeg,audio/mp4,video/mp4,video/mpeg,video/quicktime,video/webm,application/msword,application/excel,application/pdf,application/powerpoint,text/plain,application/x-zip"|Legal MIME Types: A comma separated list of legal MIME types to upload.|restrict_uploads:1|
|rules|"object"|нет|""|Permissions: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
