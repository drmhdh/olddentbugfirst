class script(object):
    START_MSG = """๐๐ฒ๐น๐ผ {},
๐๐ฎ๐บ <a href=https://t.me/search_dentalbooks_bot> ๐ ๐๐ฒ๐ป๐ ๐ง๐ฒ๐ฐ๐ต ๐ ๐๐ถ๐ฏ๐ฟ๐ฎ๐ฟ๐ถ๐ฎ๐ป ๐งโโ</a>, ๐ ๐ฐ๐ฎ๐ป ๐ฃ๐ฟ๐ผ๐๐ถ๐ฑ๐ฒ ๐ฌ๐ผ๐ ๐๐๐ฎ๐ถ๐น๐ฎ๐ฏ๐น๐ฒ ๐๐ฒ๐ป๐๐ฎ๐น ๐ฅ๐ฒ๐ณ๐ฒ๐ฟ๐ฒ๐ป๐ฐ๐ฒ๐ ๐๐ฟ๐ฒ๐ฒ. ๐๐ผ๐ถ๐ป ๐ข๐๐ฟ <a href='https://t.me/dent_tech_for_books'> ๐ ๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐ ๐ ๐๐ฟ๐ผ๐๐ฝ ๐งโโ </a> ๐ฎ๐ป๐ฑ ๐๐ป๐ท๐ผ๐ ๐

<b>๐ สแดสแด สแดแด แดแดษด sแดแดสแดส าษชสแดs ษชษด โคต๏ธษชษดสษชษดแด แดแดแดแด แดs แดกแดสส แดs ๐ฑแดแด, แดsแด แดสแด สแดสแดแดก สแดแดแดแดษดs แดแด sแดแดสแดส าษชสแดs แดส sแดษดแด แดแด แดสแด ษดแดแดแด แดา าษชสแด แดแด sแดแดสแดส. ๐</b>

<b>๐ฅฒ๐๐ฆ ๐๐๐ ๐ก๐๐๐  ๐๐๐ ๐๐ก๐๐๐ ๐๐๐๐๐๐๐ ๐๐ ๐๐โ. ๐๐ข๐๐๐๐๐ก ๐๐ ๐พ๐๐๐ ๐๐ ๐ด๐๐๐ฃ๐</b> ๐"""
      
    ABOUT_TXT = """โฏ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}
โฏ ๐ฒ๐๐ด๐ฐ๐๐พ๐: <a href='https://t.me/dent_tech_for_books'> ๐๐ณ๐ ๐ ๐๐พ๐พ๐ผ๐โ</a>
โฏ ๐ป๐ธ๐ฑ๐๐ฐ๐๐: ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ
โฏ ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด: ๐ฟ๐๐๐ท๐พ๐ฝ ๐น
โฏ ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด: ๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ
โฏ ๐ฑ๐พ๐ ๐๐ด๐๐๐ด๐: ๐ท๐ด๐๐พ๐บ๐
โฏ ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐: v1.0.1 [ ๐ฑ๐ด๐๐ฐ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- ๐ Our Motto&Goal is to Spread Knowledge and Dental Science for All Dentists & Students Around The World for Free ๐. 
- ๐ฌ๐๐๐ก๐ง ๐ฆท ๐ง๐๐๐ ๐ - https://t.me/dent_tech_for_u  
<b>DEVS:</b>
- <a href='https://t.me/dent_tech_for_books'> ๐SUPPORT ๐ GROUP๐งโโ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message
<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- Eva Maria Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Eva Maria
<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """๐ ๐ฃ๐ธ๐ฝ๐ช๐ต ๐๐ฒ๐ต๐ฎ๐ผ: <code>{}</code>
๐ค ๐ฃ๐ธ๐ฝ๐ช๐ต ๐ค๐ผ๐ฎ๐ป๐ผ: <code>{}</code>
๐ฅ ๐ฃ๐ธ๐ฝ๐ช๐ต ๐๐ฑ๐ช๐ฝ๐ผ: <code>{}</code>
๐พ ๐ค๐ผ๐ฎ๐ญ ๐ข๐ฝ๐ธ๐ป๐ช๐ฐ๐ฎ: <code>{}</code> ๐ผ๐๐ฑ
โณ ๐๐ป๐ฎ๐ฎ ๐ข๐ฝ๐ธ๐ป๐ช๐ฐ๐ฎ: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
