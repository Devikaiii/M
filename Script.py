class script(object):
    START_TXT = """đđť Há´ĘĘá´ {}.

đ¨đ đşđ đşđđđ đżđđđđžđ đťđđ đđđđźđ đźđşđ đđđđđđ˝đž đđđđđžđ đđ đđđđ đđđđđđ. đ đ˝đ˝ đŹđž đłđ đ¸đđđ đŚđđđđ đşđđ˝ đđđđđđđž đđž đşđ đşđ˝đđđ đđ đđžđ đđž đđžđ đđ đşđźđđđđ.

đ˘đđđźđ đđ đđđž đ§đžđđ đťđđđđđ đżđđ đŹđđđž..."""
    HELP_TXT = """
đđťââď¸   đ§đžđđđđđ  {} đ¤

â  đđ'đ đ­đđđž đ˘đđđđđđźđşđđžđ˝...đ¤

â  đ˛đžđşđđźđ đđđđđ đđđđđđž đđđ˝đž
đłđđđ đđžđđđđ˝ đđđđđ đđ đşđđ đźđđşđ, đŠđđđ đđđđž <b>Bot Username</b> đşđđ˝ đđđžđ đđžđşđđž đş đđđşđźđž đşđđ˝ đđžđşđđźđ đşđđ đđđđđž đđđ đđşđđ...

đđťââď¸ đłđđđđđđşđ đŚđđđ˝đž @piro_tuts

â đ đđşđđđşđťđđž đ˘đđđđşđđ˝đ
     
 /start - Check I'm Alive..
 /status - Bot Status
 /info - User info
 /alive - To check you are alive
 /ping - To get your ping
 /id - User id
 /stats - Db status  
 /broadcast - Broadcast (đŽđđđžđ đŽđđđ)

â đ­đđđđźđž đ:-

âđŁđđđ đ˛đđşđ đŹđž...đ¤

đ đŻđđđžđđžđ˝ đťđ @rai_info17
"""
    ABOUT_TXT = """
â đ˘đđžđşđđđ : <a href='https://t.me/rithesh_rkrm_17'>đłđđđ đŻđžđđđđ</a>
â đŤđşđđđđşđđž : đŻđđđđđ đĽ 
â đŤđđťđđşđđ : đŻđđđđđđşđ đşđđđđźđđ đ˘.đŁđŠ.đŁ 
â đ˛đžđđđžđ : Contabo
â đŁđşđđşđťđşđđž : <a href='https://www.mongodb.com'>đŹđđđđđŁđĄ đĽđđžđž đłđđžđ</a>
â đĄđđđđ˝ đ˛đđşđđđ : v1.0.1 [BeTa]
â đ˛đđđđđđ đŚđđđđ : <a href='https://t.me/raixchat'>đłđşđ đ§đžđđž</a>"""
    SOURCE_TXT = """<b>NOTE:</b>
Special Thanks to EvaMaria and Professor-Bot for the codes 
<b>DEV:</b>

- <a href=https://t.me/rithesh_rkrm_17>ăá´ÉŞĘá´ă</a>
- Source - https://github.com/ritheshrkrm/PiroAutoFilterBot """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and PiroAutoFilterBot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â˘ /filter - <code>add a filter in chat</code>
â˘ /filters - <code>list all the filters of a chat</code>
â˘ /del - <code>delete a specific filter in chat</code>
â˘ /delall - <code>delete the whole filters in a chat (chat owner only)</code>

<b>Adv Global Filter </b>
â˘ /gfilter - <code>á´á´ á´á´á´ É˘Ęá´Ęá´Ę ŇÉŞĘá´á´Ęs</code>
â˘ /gfilters - <code>á´á´ á´ ÉŞá´á´Ą ĘÉŞsá´ á´Ň á´ĘĘ É˘Ęá´Ęá´Ę ŇÉŞĘá´á´Ęs<code>
â˘ /delg - <code>á´á´ á´á´Ęá´á´á´ á´ sá´á´á´ÉŞŇÉŞá´ É˘Ęá´Ęá´Ę ŇÉŞĘá´á´Ę</code>
â˘ /delallg - <code>á´á´ á´á´Ęá´á´á´ á´ĘĘ É˘Ęá´Ęá´Ę ę°ÉŞĘá´á´Ęęą</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/PiroAutoFilterBot)</code>

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
â˘ /connect  - <code>connect a particular chat to your PM</code>
â˘ /disconnect  - <code>disconnect from a chat</code>
â˘ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
â˘ /id - <code>get id of a specified user.</code>
â˘ /info  - <code>get information about a user.</code>
â˘ /imdb  - <code>get the film information from IMDb source.</code>
â˘ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â˘ /logs - <code>to get the rescent errors</code>
â˘ /stats - <code>to get status of files in db.</code>
â˘ /delete - <code>to delete a specific file from db.</code>
â˘ /users - <code>to get list of my users and ids.</code>
â˘ /chats - <code>to get list of the my chats and ids </code>
â˘ /leave  - <code>to leave from a chat.</code>
â˘ /disable  -  <code>do disable a chat.</code>
â˘ /ban  - <code>to ban a user.</code>
â˘ /unban  - <code>to unban a user.</code>
â˘ /channel - <code>to get list of total connected channels</code>
â˘ /broadcast - <code>to broadcast a message to all users</code>
â˘ /inkick - <code>command with required arguments and i will kick members from group.</code>
â˘ /instatus - <code>to check current status of chat member from group.</code>
â˘ /inkick within_month long_time_ago - <code>to kick users who are offline for more than 6-7 days.</code>
â˘ /inkick long_time_ago - <code>to kick members who are offline for more than a month and Deleted Accounts.</code>
â˘ /dkick - <code>to kick deleted accounts."""
    STATUS_TXT = """đłđđđşđ đĽđđđžđ: <code>{}</code>
đłđđđşđ đŹđžđđťđžđđ: <code>{}</code>
đłđđđşđ đ˘đđşđđ: <code>{}</code>
đ´đđžđ˝ đ˛đđđđşđđž: <code>{}</code>
 """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
