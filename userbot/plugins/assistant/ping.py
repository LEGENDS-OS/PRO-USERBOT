import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

KANNADIGA_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/893de277a5c0e53cb7b44.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

KannaDiga = (
    f"**꧁•⊹٭𝙾𝚆𝙽𝙴𝚁 𝙿𝚁𝙾𝙵𝙴𝚂𝚂𝙾𝚁 𝙰𝙶𝙾𝚁𝙰٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"
)


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("OWNER STAY HERE", "https://t.me/MASTI_IN_DOSTI")]]
    await tgbot.send_file(event.chat_id, KANNADIGA_IMG, caption=KannaDiga, buttons=GOOD)
