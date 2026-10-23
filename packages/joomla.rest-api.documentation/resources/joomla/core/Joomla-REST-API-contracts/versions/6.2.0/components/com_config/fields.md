# com_config: заполнение полей, Joomla 6.2.0

GET application возвращает коллекцию, где ресурс содержит ОДНУ настройку.
PATCH application принимает плоский объект настроек.
GET config/{component_name} также возвращает настройки отдельными ресурсами.
PATCH компонента принимает плоские параметры, не {params:{...}}, и накладывает
их на существующие до валидации. PATCH не возвращает новый объект конфигурации.
Схема выбирается по component_name из Config_com_*; сторонний компонент
требует отдельной схемы. Реальные пароли и локальные пути в примерах отсутствуют.
В 6.2.0 smtpauth — варианты 0/1/2 (отключено, пароль, OAuth 2.0), включая числовые строки; прежний boolean-контракт не применять. Поля smtp_oauth2_* описаны в форме. REST-запись настроек сама по себе не выполняет браузерное согласие OAuth.
В базовом ApiController 6.2.0 для редактирования нужны core.manage и права записи core.edit либо core.edit.own с совпадающим владельцем; контроллер компонента может переопределять проверку. Пропущенные календарные поля SERVER_UTC/USER_UTC восстанавливаются из БД без второй конвертации UTC.

## Приоритет схем

Точный requestBody операции — допустимое тело REST. Инвентарь XML ниже содержит также поля UI и read-only данные; он не разрешает автоматически отправлять их в API. Условные варианты params выбираются по x-extension-parameter-schemas.

## REST PATCH /v1/config/application

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|caching|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|System Cache: Joomla form field caching; input is validated and filtered according to x-joomla-form.||
|cache_handler|"string"|нет|""|Cache Handler: Joomla form field cache_handler; input is validated and filtered according to x-joomla-form.|caching:1,2|
|cache_platformprefix|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Platform Specific Caching: Joomla form field cache_platformprefix; input is validated and filtered according to x-joomla-form.|caching:1,2|
|cachetime|["integer", "string"]|нет|"15"|Cache Time (minutes): Joomla form field cachetime; input is validated and filtered according to x-joomla-form.|caching:1,2|
|cache_path|"string"|нет|""|Path to Cache Folder: Joomla form field cache_path; input is validated and filtered according to x-joomla-form.|cache_handler:file[AND]caching:1,2|
|memcached_persist|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Persistent Memcache(d): Joomla form field memcached_persist; input is validated and filtered according to x-joomla-form.|cache_handler:memcached[AND]caching:1,2|
|memcached_compress|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Memcache(d) Compression: Joomla form field memcached_compress; input is validated and filtered according to x-joomla-form.|cache_handler:memcached[AND]caching:1,2|
|memcached_server_host|"string"|нет|"localhost"|Memcache(d) Server Host: Joomla form field memcached_server_host; input is validated and filtered according to x-joomla-form.|cache_handler:memcached[AND]caching:1,2|
|memcached_server_port|["integer", "string"]|нет|"11211"|Memcache(d) Server Port: Joomla form field memcached_server_port; input is validated and filtered according to x-joomla-form.|cache_handler:memcached[AND]caching:1,2|
|redis_persist|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Persistent Redis: Joomla form field redis_persist; input is validated and filtered according to x-joomla-form.|cache_handler:redis[AND]caching:1,2|
|redis_server_host|"string"|нет|"localhost"|Redis Server Host/Sock: Joomla form field redis_server_host; input is validated and filtered according to x-joomla-form.|cache_handler:redis[AND]caching:1,2|
|redis_server_port|["integer", "string"]|нет|"6379"|Redis Server Port: Port discarded if connecting to Redis server over Unix sockets.|cache_handler:redis[AND]caching:1,2|
|redis_server_auth|"string"|нет|""|Redis Server Authentication: Joomla form field redis_server_auth; input is validated and filtered according to x-joomla-form.|cache_handler:redis[AND]caching:1,2|
|redis_server_db|["integer", "string"]|нет|"0"|Redis Database: Joomla form field redis_server_db; input is validated and filtered according to x-joomla-form.|cache_handler:redis[AND]caching:1,2|
|dbtype|"string"|нет|""|Database Type: Do not change this to a different database technology e.g. from MySQLi (MariaDB/MySQL database technology) to PostgreSQL (Postgres database technology); it will break your site.||
|host|"string"|нет|""|Host: Joomla form field host; input is validated and filtered according to x-joomla-form.||
|user|"string"|нет|""|Database Username: Joomla form field user; input is validated and filtered according to x-joomla-form.||
|password|"string"|нет|""|Database Password: Do not edit this field unless absolutely necessary (eg after the transfer of the database to a new hosting provider).||
|db|"string"|нет|""|Database Name: Joomla form field db; input is validated and filtered according to x-joomla-form.||
|dbprefix|"string"|нет|"jos_"|Database Tables Prefix: Joomla form field dbprefix; input is validated and filtered according to x-joomla-form.||
|dbencryption|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Connection Encryption: Joomla form field dbencryption; input is validated and filtered according to x-joomla-form.||
|dbsslkey|"string"|нет|""|Path to Private Key File: Joomla form field dbsslkey; input is validated and filtered according to x-joomla-form.|dbencryption:2|
|dbsslcert|"string"|нет|""|Path to Certificate File: Joomla form field dbsslcert; input is validated and filtered according to x-joomla-form.|dbencryption:2|
|dbsslverifyservercert|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Verify Server Certificate: Joomla form field dbsslverifyservercert; input is validated and filtered according to x-joomla-form.|dbencryption:1,2|
|dbsslca|"string"|нет|""|Path to CA File: Joomla form field dbsslca; input is validated and filtered according to x-joomla-form.|dbencryption:1,2[AND]dbsslverifyservercert:1|
|dbsslcipher|"string"|нет|""|Supported Cipher Suite (optional): Joomla form field dbsslcipher; input is validated and filtered according to x-joomla-form.|dbtype:mysql,mysqli[AND]dbencryption:2|
|debug|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Debug System: Use it only for troubleshooting, ideally on <em>private</em> copies of your site. The more technical information displayed in this mode can be a security risk if left enabled on live sites. Remember to publish the "System - Debug" plugin to get detailed information on each page being loaded.||
|debug_lang|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Debug Language: Displays <strong><code>??</code></strong> around a language string constant when the string is not present in the currently loaded language files or <strong><code>**</code></strong> around the string value when the string is present. If none of the above is displayed, it could mean the text is hardcoded and needs a language string.||
|debug_lang_const|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Language Display: Select if you should display the language constant or the language value when debugging the language strings.|debug_lang:1|
|cors|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Enable CORS: Cross-Origin Resource Sharing (CORS) enables scripts running in a browser to interact with resources from a different origin.||
|cors_allow_origin|"string"|нет|"*"|Access-Control-Allow-Origin: Specifies the origin allowed to access Web services on this site, sent back in response to a preflight request. Default: * (=all).|cors:1|
|cors_allow_headers|"string"|нет|"Content-Type,X-Joomla-Token,Authorization"|Access-Control-Allow-Headers: Specifies the header(s) sent back in response to a preflight request. Default: Content-Type,X-Joomla-Token|cors:1|
|cors_allow_methods|"string"|нет|""|Access-Control-Allow-Methods: Specifies the Web service method(s) allowed to access on this site, sent back in response to a preflight request. Default: all methods available for the requested route.|cors:1|
|behind_loadbalancer|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Behind Load Balancer: If your site is behind a load balancer or reverse proxy, enable this setting so that IP addresses and other configurations within Joomla automatically take this into account.||
|proxy_enable|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Enable Outbound Proxy: Some hosts do not allow any network access from your site to the outside world by default and require you to manually configure an outbound proxy.||
|proxy_host|"string"|нет|""|Outbound Proxy Host: Host (domain) name or IP address.|proxy_enable:1|
|proxy_port|["integer", "string"]|нет|""|Outbound Proxy Port: Joomla form field proxy_port; input is validated and filtered according to x-joomla-form.|proxy_enable:1|
|proxy_user|"string"|нет|""|Outbound Proxy Username: Leave blank if your outbound proxy does not require authentication.|proxy_enable:1|
|proxy_pass|"string"|нет|""|Outbound Proxy Password: Joomla form field proxy_pass; input is validated and filtered according to x-joomla-form.|proxy_enable:1|
|offset|"string"|нет|"UTC"|Website Time Zone: Used by default to display dates and times (Joomla stores them internally as UTC). This can be different than the time zone of your server. Users can override their preferred time zone in their user profile.||
|mailonline|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Send Mail: Joomla form field mailonline; input is validated and filtered according to x-joomla-form.||
|massmailoff|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Disable Mass Mail: Joomla offers a Mass Mail feature which allows a user with administrator access to send an email to all users of the site. On sites with more than a few dozen users this can be problematic or time out.|mailonline:1|
|mailfrom|"string"|нет|""|From Email: Joomla form field mailfrom; input is validated and filtered according to x-joomla-form.|mailonline:1|
|fromname|"string"|нет|""|From Name: Joomla form field fromname; input is validated and filtered according to x-joomla-form.|mailonline:1|
|replyto|"string"|нет|""|Reply To Email: Joomla form field replyto; input is validated and filtered according to x-joomla-form.|mailonline:1|
|replytoname|"string"|нет|""|Reply To Name: Joomla form field replytoname; input is validated and filtered according to x-joomla-form.|mailonline:1|
|mailer|"string"|нет|["mail", "sendmail", "smtp"]|Mailer: Joomla form field mailer; input is validated and filtered according to x-joomla-form.|mailonline:1|
|sendmail|"string"|нет|"/usr/sbin/sendmail"|Sendmail Path: Joomla form field sendmail; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:sendmail|
|smtphost|"string"|нет|"localhost"|SMTP Host: Joomla form field smtphost; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp|
|smtpport|["integer", "string"]|нет|"25"|SMTP Port: Joomla form field smtpport; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp|
|smtpsecure|"string"|нет|["none", "ssl", "tls"]|SMTP Security: Joomla form field smtpsecure; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp|
|smtpauth|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|SMTP Authentication: Joomla form field smtpauth; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp|
|smtpuser|"string"|нет|""|SMTP Username: Joomla form field smtpuser; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:1,2|
|smtppass|"string"|нет|""|SMTP Password: Joomla form field smtppass; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:1|
|smtp_oauth2_client_id|"string"|нет|""|OAuth2 Client ID: Joomla form field smtp_oauth2_client_id; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_client_secret|"string"|нет|""|OAuth2 Client Secret: Joomla form field smtp_oauth2_client_secret; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_scope|"string"|нет|""|OAuth2 Scope: Joomla form field smtp_oauth2_scope; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_authorize_url|"string"|нет|""|OAuth2 Authorize URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_token_url|"string"|нет|""|OAuth2 Token URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_auth_wizard|"string"|нет|""|OAuth2 Token: Joomla form field smtp_oauth2_auth_wizard; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|MetaDesc|"string"|нет|""|Site Meta Description: Joomla form field MetaDesc; input is validated and filtered according to x-joomla-form.||
|robots|"string"|нет|["", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|MetaRights|"string"|нет|""|Content Rights: Describe what rights others have to use this content. This is conveyed to search engines using the <code>rights</code> meta tag in the HTML head.||
|MetaAuthor|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Author Meta Tag: Joomla form field MetaAuthor; input is validated and filtered according to x-joomla-form.||
|MetaVersion|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Joomla Version: Controls whether the <code>generator</code> meta tag in the HTML document's header in the frontend and in Atom feeds includes the exact version of your Joomla site. It is recommended to hide it for security reasons.||
|sef|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Search Engine Friendly URLs: Joomla URLs normally look like <code>index.php?option=com_example&task=item.display&id=1</code> which isn't easy to convey verbally or in writing. Search Engine Friendly (SEF) URLs are more human–readable, e.g. <code>index.php/example/display/something</code>.||
|sef_rewrite|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Use URL Rewriting: Removes the <code>index.php/</code> part from the URLs.|sef:1|
|sef_suffix|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Add Suffix to URL: By default, Joomla URLs are "bare", without an extension. This options tells Joomla to add an extension such as <code>.html</code>, <code>.feed</code> etc based on the type of content being displayed by the URL.|sef:1|
|unicodeslugs|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Unicode Aliases: No: Joomla transliterates aliases which contain non–latin-1 characters using the transliteration engine provided by the Joomla language pack for the content's selected language, e.g. über becomes ueber for en-GB (English, Great Britain). Yes: Joomla does not transliterate aliases; the alias is used as is, e.g. über remains as–is.|sef:1|
|sitename_pagetitles|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Site Name in Page Titles: Joomla form field sitename_pagetitles; input is validated and filtered according to x-joomla-form.||
|tmp_path|"string"|нет|""|Path to Temp Folder: Joomla needs to temporarily store some files to perform actions such as installing / updating extensions or uploading files. Enter the absolute path of a directory that is writable by PHP. <em>Do not</em> use the system–wide temporary folder (e.g. <code>/tmp</code>) for security reasons.||
|gzip|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Gzip Page Compression: Joomla can automatically compress the generated HTML pages with GZip, making them smaller and increasing your site's speed score. Disable it if your server is already doing that for you or if it conflicts with third party extensions.||
|error_reporting|"string"|нет|["default", "none", "simple", "maximum"]|Error Reporting: Control whether PHP error messages should be displayed at all and how verbose they will be. On live sites use None for security reasons. Only use Maximum while troubleshooting — remember to set that back to None when you're done!||
|force_ssl|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Force HTTPS: HTTPS must be enabled on your server or load balancer to utilise this option. Enable 'Behind Load Balancer' if your SSL terminates on your load balancer but your site is served on http on its webserver.||
|session_handler|"string"|нет|"filesystem"|Session Handler: Joomla form field session_handler; input is validated and filtered according to x-joomla-form.||
|session_filesystem_path|"string"|нет|""|Session Save Path: The filesystem path where session data will be stored.<br>If empty, the system's temporary directory will be used.|session_handler:filesystem|
|session_memcached_server_host|"string"|нет|"localhost"|Memcache(d) Server Host: Joomla form field session_memcached_server_host; input is validated and filtered according to x-joomla-form.|session_handler:memcached|
|session_memcached_server_port|["integer", "string"]|нет|"11211"|Memcache(d) Server Port: Joomla form field session_memcached_server_port; input is validated and filtered according to x-joomla-form.|session_handler:memcached|
|session_redis_persist|["integer", "string"]|нет|[0, 1, "0", "1"]|Persistent Redis: Joomla form field session_redis_persist; input is validated and filtered according to x-joomla-form.|session_handler:redis|
|session_redis_server_host|"string"|нет|"localhost"|Redis Server Host/Sock: Joomla form field session_redis_server_host; input is validated and filtered according to x-joomla-form.|session_handler:redis|
|session_redis_server_port|["integer", "string"]|нет|"6379"|Redis Server Port: Port discarded if connecting to Redis server over Unix sockets.|session_handler:redis|
|session_redis_server_auth|"string"|нет|""|Redis Server Authentication: Joomla form field session_redis_server_auth; input is validated and filtered according to x-joomla-form.|session_handler:redis|
|session_redis_server_db|["integer", "string"]|нет|"0"|Redis Database: Joomla form field session_redis_server_db; input is validated and filtered according to x-joomla-form.|session_handler:redis|
|lifetime|["integer", "string"]|нет|"15"|Session Lifetime (minutes): Joomla form field lifetime; input is validated and filtered according to x-joomla-form.||
|shared_session|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Shared Sessions: When enabled, a user's session is shared between the frontend and administrator sections of the site. Note that changing this value will invalidate all existing sessions on the site. This is not available when the "Force HTTPS" option is set to "Administrator Only".||
|session_metadata|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Track Session Metadata: If enabled, additional metadata about a user's session (including their username, user ID, and which application they are logged into) will be logged to the session database table.<br>If disabled, features dependent on this data will be unavailable.||
|session_metadata_for_guest|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Track Guest Session Metadata: If enabled, additional metadata about both registered and non registered user's session will be logged to the session database table. <br>If disabled, only data for registered user will be logged.|session_metadata:1|
|sitename|"string"|нет|""|Site Name: Joomla form field sitename; input is validated and filtered according to x-joomla-form.||
|offline|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Site Offline: Joomla form field offline; input is validated and filtered according to x-joomla-form.||
|display_offline_message|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Offline Message: Joomla form field display_offline_message; input is validated and filtered according to x-joomla-form.|offline:1|
|offline_message|"string"|нет|""|Custom Message: Joomla form field offline_message; input is validated and filtered according to x-joomla-form.|offline:1[AND]display_offline_message:1|
|offline_image|"string"|нет|""|Offline Image: Joomla form field offline_image; input is validated and filtered according to x-joomla-form.|offline:1|
|frontediting|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Frontend Editing: Joomla can show an overlay in the public front–end, visible only to users with edit privileges, to directly modify the configuration of each module and/or menu displayed on the site. Set to "None" to disable this feature.||
|editor|"string"|нет|"tinymce"|Default Editor: This editor will be used for editing content and other rich text areas in third party extensions unless a user has chosen a different one in their user profile . This will also be the only editor available and used for users who are not already logged in (the Guest user group).||
|captcha|["integer", "string"]|нет|"0"|Default Captcha: Joomla and third party extensions can use a <a href="https://en.wikipedia.org/wiki/CAPTCHA" target="_blank" rel="noopener noreferrer">CAPTCHA</a> to prevent abuse (spam) on public forms. Each extension can choose to use a different CAPTCHA, if more than one are available. If no selection is made this will be used by default. You can enable additional CAPTCHA methods in System, Manage, Plugins.||
|access|["integer", "string"]|нет|"1"|Default Access Level: Set the Access Level which will be assigned by default to newly created items.||
|list_limit|["integer", "string"]|нет|[5, 10, 15, 20, 25, 30, 50, 100, 200, 500, "5", "10", "15", "20", "25", "30", "50", "100", "200", "500"]|Default List Limit: Joomla form field list_limit; input is validated and filtered according to x-joomla-form.||
|feed_limit|["integer", "string"]|нет|[5, 10, 15, 20, 25, 30, 50, 100, "5", "10", "15", "20", "25", "30", "50", "100"]|Default Feed Limit: How many items will be published by default in RSS and Atom feeds.||
|feed_email|"string"|нет|["author", "site", "none"]|Feed Email Address: Joomla form field feed_email; input is validated and filtered according to x-joomla-form.||
|log_path|"string"|нет|""|Path to Log Folder: Joomla can optionally keep a log file of its own and third party extensions' operations. Provide the absolute path to a folder that is writable by PHP; if it's missing or is not writable Joomla will not load at all. For security reasons you must not use a folder with system–wide access such as <code>/tmp</code>.||
|log_everything|["integer", "string"]|нет|[0, 1, "0", "1"]|Log Almost Everything: Logs everything, except deprecated APIs.||
|log_deprecated|["integer", "string"]|нет|[0, 1, "0", "1"]|Log Deprecated API: Joomla form field log_deprecated; input is validated and filtered according to x-joomla-form.||
|log_priorities|"array"|нет|["all"]|Log Priorities: Joomla form field log_priorities; input is validated and filtered according to x-joomla-form.||
|log_categories|"string"|нет|""|Log Categories: A comma separated list of log categories to include or exclude. If empty, custom logging is disabled.||
|log_category_mode|["integer", "string"]|нет|[0, 1, "0", "1"]|Log Category Mode: Joomla form field log_category_mode; input is validated and filtered according to x-joomla-form.||
|cookie_domain|"string"|нет|""|Cookie Domain: Precede domain with '.' if cookie should be valid for all subdomains. On most servers you do not need to set this or Cookie Path below.||
|cookie_path|"string"|нет|""|Cookie Path: Joomla form field cookie_path; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|FIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|filters|"string"|нет|""|Text Filters: Joomla form field filters; input is validated and filtered according to x-joomla-form.||
## REST PATCH /v1/config/{component_name}

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|

## Инвентарь стандартных форм UI

## administrator/components/com_config/forms/application.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
|caching|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|System Cache: Joomla form field caching; input is validated and filtered according to x-joomla-form.||
|cache_handler|"string"|нет|""|Cache Handler: Joomla form field cache_handler; input is validated and filtered according to x-joomla-form.|caching:1,2|
|cache_platformprefix|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Platform Specific Caching: Joomla form field cache_platformprefix; input is validated and filtered according to x-joomla-form.|caching:1,2|
|cachetime|["integer", "string"]|да|"15"|Cache Time (minutes): Joomla form field cachetime; input is validated and filtered according to x-joomla-form.|caching:1,2|
|cache_path|"string"|нет|""|Path to Cache Folder: Joomla form field cache_path; input is validated and filtered according to x-joomla-form.|cache_handler:file[AND]caching:1,2|
|memcached_persist|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Persistent Memcache(d): Joomla form field memcached_persist; input is validated and filtered according to x-joomla-form.|cache_handler:memcached[AND]caching:1,2|
|memcached_compress|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Memcache(d) Compression: Joomla form field memcached_compress; input is validated and filtered according to x-joomla-form.|cache_handler:memcached[AND]caching:1,2|
|memcached_server_host|"string"|нет|"localhost"|Memcache(d) Server Host: Joomla form field memcached_server_host; input is validated and filtered according to x-joomla-form.|cache_handler:memcached[AND]caching:1,2|
|memcached_server_port|["integer", "string"]|нет|"11211"|Memcache(d) Server Port: Joomla form field memcached_server_port; input is validated and filtered according to x-joomla-form.|cache_handler:memcached[AND]caching:1,2|
|redis_persist|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Persistent Redis: Joomla form field redis_persist; input is validated and filtered according to x-joomla-form.|cache_handler:redis[AND]caching:1,2|
|redis_server_host|"string"|нет|"localhost"|Redis Server Host/Sock: Joomla form field redis_server_host; input is validated and filtered according to x-joomla-form.|cache_handler:redis[AND]caching:1,2|
|redis_server_port|["integer", "string"]|нет|"6379"|Redis Server Port: Port discarded if connecting to Redis server over Unix sockets.|cache_handler:redis[AND]caching:1,2|
|redis_server_auth|"string"|нет|""|Redis Server Authentication: Joomla form field redis_server_auth; input is validated and filtered according to x-joomla-form.|cache_handler:redis[AND]caching:1,2|
|redis_server_db|["integer", "string"]|нет|"0"|Redis Database: Joomla form field redis_server_db; input is validated and filtered according to x-joomla-form.|cache_handler:redis[AND]caching:1,2|
|dbtype|"string"|нет|""|Database Type: Do not change this to a different database technology e.g. from MySQLi (MariaDB/MySQL database technology) to PostgreSQL (Postgres database technology); it will break your site.||
|host|"string"|да|""|Host: Joomla form field host; input is validated and filtered according to x-joomla-form.||
|user|"string"|да|""|Database Username: Joomla form field user; input is validated and filtered according to x-joomla-form.||
|password|"string"|нет|""|Database Password: Do not edit this field unless absolutely necessary (eg after the transfer of the database to a new hosting provider).||
|db|"string"|да|""|Database Name: Joomla form field db; input is validated and filtered according to x-joomla-form.||
|dbprefix|"string"|нет|"jos_"|Database Tables Prefix: Joomla form field dbprefix; input is validated and filtered according to x-joomla-form.||
|dbencryption|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Connection Encryption: Joomla form field dbencryption; input is validated and filtered according to x-joomla-form.||
|dbsslkey|"string"|нет|""|Path to Private Key File: Joomla form field dbsslkey; input is validated and filtered according to x-joomla-form.|dbencryption:2|
|dbsslcert|"string"|нет|""|Path to Certificate File: Joomla form field dbsslcert; input is validated and filtered according to x-joomla-form.|dbencryption:2|
|dbsslverifyservercert|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Verify Server Certificate: Joomla form field dbsslverifyservercert; input is validated and filtered according to x-joomla-form.|dbencryption:1,2|
|dbsslca|"string"|нет|""|Path to CA File: Joomla form field dbsslca; input is validated and filtered according to x-joomla-form.|dbencryption:1,2[AND]dbsslverifyservercert:1|
|dbsslcipher|"string"|нет|""|Supported Cipher Suite (optional): Joomla form field dbsslcipher; input is validated and filtered according to x-joomla-form.|dbtype:mysql,mysqli[AND]dbencryption:2|
|debug|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Debug System: Use it only for troubleshooting, ideally on <em>private</em> copies of your site. The more technical information displayed in this mode can be a security risk if left enabled on live sites. Remember to publish the "System - Debug" plugin to get detailed information on each page being loaded.||
|debug_lang|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Debug Language: Displays <strong><code>??</code></strong> around a language string constant when the string is not present in the currently loaded language files or <strong><code>**</code></strong> around the string value when the string is present. If none of the above is displayed, it could mean the text is hardcoded and needs a language string.||
|debug_lang_const|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Language Display: Select if you should display the language constant or the language value when debugging the language strings.|debug_lang:1|
|cors|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Enable CORS: Cross-Origin Resource Sharing (CORS) enables scripts running in a browser to interact with resources from a different origin.||
|cors_allow_origin|"string"|нет|"*"|Access-Control-Allow-Origin: Specifies the origin allowed to access Web services on this site, sent back in response to a preflight request. Default: * (=all).|cors:1|
|cors_allow_headers|"string"|нет|"Content-Type,X-Joomla-Token,Authorization"|Access-Control-Allow-Headers: Specifies the header(s) sent back in response to a preflight request. Default: Content-Type,X-Joomla-Token|cors:1|
|cors_allow_methods|"string"|нет|""|Access-Control-Allow-Methods: Specifies the Web service method(s) allowed to access on this site, sent back in response to a preflight request. Default: all methods available for the requested route.|cors:1|
|behind_loadbalancer|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Behind Load Balancer: If your site is behind a load balancer or reverse proxy, enable this setting so that IP addresses and other configurations within Joomla automatically take this into account.||
|proxy_enable|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Enable Outbound Proxy: Some hosts do not allow any network access from your site to the outside world by default and require you to manually configure an outbound proxy.||
|proxy_host|"string"|нет|""|Outbound Proxy Host: Host (domain) name or IP address.|proxy_enable:1|
|proxy_port|["integer", "string"]|нет|""|Outbound Proxy Port: Joomla form field proxy_port; input is validated and filtered according to x-joomla-form.|proxy_enable:1|
|proxy_user|"string"|нет|""|Outbound Proxy Username: Leave blank if your outbound proxy does not require authentication.|proxy_enable:1|
|proxy_pass|"string"|нет|""|Outbound Proxy Password: Joomla form field proxy_pass; input is validated and filtered according to x-joomla-form.|proxy_enable:1|
|offset|"string"|нет|"UTC"|Website Time Zone: Used by default to display dates and times (Joomla stores them internally as UTC). This can be different than the time zone of your server. Users can override their preferred time zone in their user profile.||
|mailonline|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Send Mail: Joomla form field mailonline; input is validated and filtered according to x-joomla-form.||
|massmailoff|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Disable Mass Mail: Joomla offers a Mass Mail feature which allows a user with administrator access to send an email to all users of the site. On sites with more than a few dozen users this can be problematic or time out.|mailonline:1|
|mailfrom|"string"|нет|""|From Email: Joomla form field mailfrom; input is validated and filtered according to x-joomla-form.|mailonline:1|
|fromname|"string"|нет|""|From Name: Joomla form field fromname; input is validated and filtered according to x-joomla-form.|mailonline:1|
|replyto|"string"|нет|""|Reply To Email: Joomla form field replyto; input is validated and filtered according to x-joomla-form.|mailonline:1|
|replytoname|"string"|нет|""|Reply To Name: Joomla form field replytoname; input is validated and filtered according to x-joomla-form.|mailonline:1|
|mailer|"string"|нет|["mail", "sendmail", "smtp"]|Mailer: Joomla form field mailer; input is validated and filtered according to x-joomla-form.|mailonline:1|
|sendmail|"string"|нет|"/usr/sbin/sendmail"|Sendmail Path: Joomla form field sendmail; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:sendmail|
|smtphost|"string"|нет|"localhost"|SMTP Host: Joomla form field smtphost; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp|
|smtpport|["integer", "string"]|нет|"25"|SMTP Port: Joomla form field smtpport; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp|
|smtpsecure|"string"|нет|["none", "ssl", "tls"]|SMTP Security: Joomla form field smtpsecure; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp|
|smtpauth|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|SMTP Authentication: Joomla form field smtpauth; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp|
|smtpuser|"string"|нет|""|SMTP Username: Joomla form field smtpuser; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:1,2|
|smtppass|"string"|нет|""|SMTP Password: Joomla form field smtppass; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:1|
|smtp_oauth2_client_id|"string"|нет|""|OAuth2 Client ID: Joomla form field smtp_oauth2_client_id; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_client_secret|"string"|нет|""|OAuth2 Client Secret: Joomla form field smtp_oauth2_client_secret; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_scope|"string"|нет|""|OAuth2 Scope: Joomla form field smtp_oauth2_scope; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_authorize_url|"string"|нет|""|OAuth2 Authorize URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_token_url|"string"|нет|""|OAuth2 Token URL: URL subject to field relative/scheme settings; empty string may clear an optional URL.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_auth_wizard|"string"|нет|""|OAuth2 Token: Joomla form field smtp_oauth2_auth_wizard; input is validated and filtered according to x-joomla-form.|mailonline:1[AND]mailer:smtp[AND]smtpauth:2|
|smtp_oauth2_refresh_token|"string"|нет|""|smtp_oauth2_refresh_token: Joomla form field smtp_oauth2_refresh_token; input is validated and filtered according to x-joomla-form.||
|smtp_oauth2_token_issued_at|"string"|нет|""|smtp_oauth2_token_issued_at: Joomla form field smtp_oauth2_token_issued_at; input is validated and filtered according to x-joomla-form.||
|MetaDesc|"string"|нет|""|Site Meta Description: Joomla form field MetaDesc; input is validated and filtered according to x-joomla-form.||
|robots|"string"|нет|["", "noindex, follow", "index, nofollow", "noindex, nofollow"]|Robots: Joomla form field robots; input is validated and filtered according to x-joomla-form.||
|MetaRights|"string"|нет|""|Content Rights: Describe what rights others have to use this content. This is conveyed to search engines using the <code>rights</code> meta tag in the HTML head.||
|MetaAuthor|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Author Meta Tag: Joomla form field MetaAuthor; input is validated and filtered according to x-joomla-form.||
|MetaVersion|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Joomla Version: Controls whether the <code>generator</code> meta tag in the HTML document's header in the frontend and in Atom feeds includes the exact version of your Joomla site. It is recommended to hide it for security reasons.||
|sef|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Search Engine Friendly URLs: Joomla URLs normally look like <code>index.php?option=com_example&task=item.display&id=1</code> which isn't easy to convey verbally or in writing. Search Engine Friendly (SEF) URLs are more human–readable, e.g. <code>index.php/example/display/something</code>.||
|sef_rewrite|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Use URL Rewriting: Removes the <code>index.php/</code> part from the URLs.|sef:1|
|sef_suffix|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Add Suffix to URL: By default, Joomla URLs are "bare", without an extension. This options tells Joomla to add an extension such as <code>.html</code>, <code>.feed</code> etc based on the type of content being displayed by the URL.|sef:1|
|unicodeslugs|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Unicode Aliases: No: Joomla transliterates aliases which contain non–latin-1 characters using the transliteration engine provided by the Joomla language pack for the content's selected language, e.g. über becomes ueber for en-GB (English, Great Britain). Yes: Joomla does not transliterate aliases; the alias is used as is, e.g. über remains as–is.|sef:1|
|sitename_pagetitles|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Site Name in Page Titles: Joomla form field sitename_pagetitles; input is validated and filtered according to x-joomla-form.||
|tmp_path|"string"|нет|""|Path to Temp Folder: Joomla needs to temporarily store some files to perform actions such as installing / updating extensions or uploading files. Enter the absolute path of a directory that is writable by PHP. <em>Do not</em> use the system–wide temporary folder (e.g. <code>/tmp</code>) for security reasons.||
|gzip|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Gzip Page Compression: Joomla can automatically compress the generated HTML pages with GZip, making them smaller and increasing your site's speed score. Disable it if your server is already doing that for you or if it conflicts with third party extensions.||
|error_reporting|"string"|нет|["default", "none", "simple", "maximum"]|Error Reporting: Control whether PHP error messages should be displayed at all and how verbose they will be. On live sites use None for security reasons. Only use Maximum while troubleshooting — remember to set that back to None when you're done!||
|force_ssl|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Force HTTPS: HTTPS must be enabled on your server or load balancer to utilise this option. Enable 'Behind Load Balancer' if your SSL terminates on your load balancer but your site is served on http on its webserver.||
|session_handler|"string"|нет|"filesystem"|Session Handler: Joomla form field session_handler; input is validated and filtered according to x-joomla-form.||
|session_filesystem_path|"string"|нет|""|Session Save Path: The filesystem path where session data will be stored.<br>If empty, the system's temporary directory will be used.|session_handler:filesystem|
|session_memcached_server_host|"string"|нет|"localhost"|Memcache(d) Server Host: Joomla form field session_memcached_server_host; input is validated and filtered according to x-joomla-form.|session_handler:memcached|
|session_memcached_server_port|["integer", "string"]|нет|"11211"|Memcache(d) Server Port: Joomla form field session_memcached_server_port; input is validated and filtered according to x-joomla-form.|session_handler:memcached|
|session_redis_persist|["integer", "string"]|нет|[0, 1, "0", "1"]|Persistent Redis: Joomla form field session_redis_persist; input is validated and filtered according to x-joomla-form.|session_handler:redis|
|session_redis_server_host|"string"|нет|"localhost"|Redis Server Host/Sock: Joomla form field session_redis_server_host; input is validated and filtered according to x-joomla-form.|session_handler:redis|
|session_redis_server_port|["integer", "string"]|нет|"6379"|Redis Server Port: Port discarded if connecting to Redis server over Unix sockets.|session_handler:redis|
|session_redis_server_auth|"string"|нет|""|Redis Server Authentication: Joomla form field session_redis_server_auth; input is validated and filtered according to x-joomla-form.|session_handler:redis|
|session_redis_server_db|["integer", "string"]|нет|"0"|Redis Database: Joomla form field session_redis_server_db; input is validated and filtered according to x-joomla-form.|session_handler:redis|
|lifetime|["integer", "string"]|нет|"15"|Session Lifetime (minutes): Joomla form field lifetime; input is validated and filtered according to x-joomla-form.||
|shared_session|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Shared Sessions: When enabled, a user's session is shared between the frontend and administrator sections of the site. Note that changing this value will invalidate all existing sessions on the site. This is not available when the "Force HTTPS" option is set to "Administrator Only".||
|session_metadata|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Track Session Metadata: If enabled, additional metadata about a user's session (including their username, user ID, and which application they are logged into) will be logged to the session database table.<br>If disabled, features dependent on this data will be unavailable.||
|session_metadata_for_guest|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Track Guest Session Metadata: If enabled, additional metadata about both registered and non registered user's session will be logged to the session database table. <br>If disabled, only data for registered user will be logged.|session_metadata:1|
|sitename|"string"|да|""|Site Name: Joomla form field sitename; input is validated and filtered according to x-joomla-form.||
|offline|["boolean", "integer", "string"]|нет|[false, true, 0, 1, "0", "1"]|Site Offline: Joomla form field offline; input is validated and filtered according to x-joomla-form.||
|display_offline_message|["integer", "string"]|нет|[0, 1, 2, "0", "1", "2"]|Offline Message: Joomla form field display_offline_message; input is validated and filtered according to x-joomla-form.|offline:1|
|offline_message|"string"|нет|""|Custom Message: Joomla form field offline_message; input is validated and filtered according to x-joomla-form.|offline:1[AND]display_offline_message:1|
|offline_image|"string"|нет|""|Offline Image: Joomla form field offline_image; input is validated and filtered according to x-joomla-form.|offline:1|
|frontediting|["integer", "string"]|нет|[2, 1, 0, "2", "1", "0"]|Frontend Editing: Joomla can show an overlay in the public front–end, visible only to users with edit privileges, to directly modify the configuration of each module and/or menu displayed on the site. Set to "None" to disable this feature.||
|editor|"string"|нет|"tinymce"|Default Editor: This editor will be used for editing content and other rich text areas in third party extensions unless a user has chosen a different one in their user profile . This will also be the only editor available and used for users who are not already logged in (the Guest user group).||
|captcha|["integer", "string"]|нет|"0"|Default Captcha: Joomla and third party extensions can use a <a href="https://en.wikipedia.org/wiki/CAPTCHA" target="_blank" rel="noopener noreferrer">CAPTCHA</a> to prevent abuse (spam) on public forms. Each extension can choose to use a different CAPTCHA, if more than one are available. If no selection is made this will be used by default. You can enable additional CAPTCHA methods in System, Manage, Plugins.||
|access|["integer", "string"]|нет|"1"|Default Access Level: Set the Access Level which will be assigned by default to newly created items.||
|list_limit|["integer", "string"]|нет|[5, 10, 15, 20, 25, 30, 50, 100, 200, 500, "5", "10", "15", "20", "25", "30", "50", "100", "200", "500"]|Default List Limit: Joomla form field list_limit; input is validated and filtered according to x-joomla-form.||
|feed_limit|["integer", "string"]|нет|[5, 10, 15, 20, 25, 30, 50, 100, "5", "10", "15", "20", "25", "30", "50", "100"]|Default Feed Limit: How many items will be published by default in RSS and Atom feeds.||
|feed_email|"string"|нет|["author", "site", "none"]|Feed Email Address: Joomla form field feed_email; input is validated and filtered according to x-joomla-form.||
|log_path|"string"|да|""|Path to Log Folder: Joomla can optionally keep a log file of its own and third party extensions' operations. Provide the absolute path to a folder that is writable by PHP; if it's missing or is not writable Joomla will not load at all. For security reasons you must not use a folder with system–wide access such as <code>/tmp</code>.||
|log_everything|["integer", "string"]|нет|[0, 1, "0", "1"]|Log Almost Everything: Logs everything, except deprecated APIs.||
|log_deprecated|["integer", "string"]|нет|[0, 1, "0", "1"]|Log Deprecated API: Joomla form field log_deprecated; input is validated and filtered according to x-joomla-form.||
|log_priorities|"array"|нет|["all"]|Log Priorities: Joomla form field log_priorities; input is validated and filtered according to x-joomla-form.||
|log_categories|"string"|нет|""|Log Categories: A comma separated list of log categories to include or exclude. If empty, custom logging is disabled.||
|log_category_mode|["integer", "string"]|нет|[0, 1, "0", "1"]|Log Category Mode: Joomla form field log_category_mode; input is validated and filtered according to x-joomla-form.||
|cookie_domain|"string"|нет|""|Cookie Domain: Precede domain with '.' if cookie should be valid for all subdomains. On most servers you do not need to set this or Cookie Path below.||
|cookie_path|"string"|нет|""|Cookie Path: Joomla form field cookie_path; input is validated and filtered according to x-joomla-form.||
|rules|"object"|нет|""|FIELD_RULES_LABEL: Joomla form field rules; input is validated and filtered according to x-joomla-form.||
|filters|"string"|нет|""|Text Filters: Joomla form field filters; input is validated and filtered according to x-joomla-form.||
|asset_id|"string"|нет|""|asset_id: Joomla form field asset_id; input is validated and filtered according to x-joomla-form.||
## administrator/components/com_config/config.xml

| Поле | JSON-тип | Обязательно POST | Enum / default | Назначение | Условия UI |
|---|---|---|---|---|---|
