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

KannaDiga = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("", "https://t.me/NAAN_1_KANNADIGA")]]
    await tgbot.send_file(event.chat_id, KANNADIGA_IMG, caption=KannaDiga, buttons=GOOD)
