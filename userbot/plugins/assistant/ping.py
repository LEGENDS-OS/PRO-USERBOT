import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

KANNADIGA_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/e5b07c5154727e350b1ae.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

KannaDiga = f"**꧁•⊹٭KARUNADA KING٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("OWNER STAY HERE", "https://t.me/Karunada_Kings_and_Queens")]]
    await tgbot.send_file(event.chat_id, KANNADIGA_IMG, caption=KannaDiga, buttons=GOOD)
