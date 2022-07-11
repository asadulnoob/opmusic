# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "7f10cf5e8390a3ff33c7bbc581469984")
API_ID = int(getenv("API_ID", "9620148"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝘽𝙍𝙊𝙆𝙀𝙉 𝘼𝙎𝙎𝙄𝙎𝙏𝘼𝙉𝙏")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "brokenx_Assistant")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/e70f61a413b17c6add2a1.jpg")
BOT_NAME = getenv("BOT_NAME", "𝘽𝙍𝙊𝙆𝙀𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾")
BOT_TOKEN = getenv("BOT_TOKEN", "5552389598:AAEg1gXRcldx6dSjaKluOncqHqACgn5vnoY")
BOT_USERNAME = getenv("BOT_USERNAME", "broken_vccbot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "- ❛𝗠𝘁𝘀 ➻ 𝗕𝗿𝗼𝗸𝗲𝗻 𝗕𝗼𝘆 [🇮🇳]")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Broken_boyxd")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/BSDK/CHALHT")
STRING_SESSION = getenv("STRING_SESSION", "BQAr3m5vkTTVjP9IVI-8SbGQY4DM3crem27flOKsjxgOFJ5pRwjyyVvUEXBJCK5pw7aRGD_nzHJUV56sb_3jJmoZL-uXPxiMOOoY27Qnfc2DhmHDYrLypkPez_8mfNAgJaWhwlepDdgpBD2zAmBTEM_J57eiPbN6uTde1Xfw4I228IVJ_mAEJg2bqYl_1W7OcCHNtx9zG_p9QKUGN2JcUFdD04ZyKzx2kHNabwh-dz5ZCu4lLDlaylCwdoAc4IGFXwHdlhxvE0XorXpqyBDtwoZI5xa_kXKE7GdJ2GqKtsOmlGhw5OZDg09CEys0ADonJvrZmtF4HafYlXeQFijcRWTuAAAAAUBfQeEA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5374951905").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/MYSTERIOUS_CHATS")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/RTH_FIGHTERS")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐀𝐝𝐢𝐭𝐲𝐚 𝐇𝐚𝐥𝐝𝐞𝐫) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/kaalxd")
