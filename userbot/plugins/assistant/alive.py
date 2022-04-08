from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/ccff0cc2752f1917eb08a.jpg"
pm_caption = f"⚜『𝙺𝚊𝚗𝚗𝚊𝚍𝚒𝚐𝚊』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{KANNADIGA_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Telethon ~ `1.15.0` \n"
pm_caption += f"┣『KING VERSION』~ `{KANNADIGAversion}` \n"
pm_caption += f"┣Channel ~ [Channel](https://t.me/Kannadiga_bots)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/MR-KANNADIGA/KANNADIGA-BOT/blob/master/LICENSE)\n"
pm_caption += (
    f"┣Copyright ~ By [『KANNADIGA BOT』 ](https://t.me/KARUNADA_KINGS_AND_QUEENS)\n"
)
pm_caption += f"┣Created ~ By [『KING OF KARNATAKA』 ](https://t.me/KARUNADA_KING)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『SPAM SUPPORT』](https://t.me/KARUNADA_FIGHTERS) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
