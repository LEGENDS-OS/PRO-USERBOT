from telethon import events

from userbot import *

from . import *

PM_IMG = "https://te.legra.ph/file/893de277a5c0e53cb7b44.jpg"
pm_caption = f"⚜『𝙺𝚊𝚗𝚗𝚊𝚍𝚒𝚐𝚊』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{KANNADIGA_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『𝙿𝚘𝚛𝚏𝚎𝚜𝚜𝚘𝚛 𝙰𝚐𝚘𝚛𝚊』~ `{KANNADIGAversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Kannadiga_bots)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/MR-KANNADIGA/KANNADIGA-BOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『𝙺𝚊𝚗𝚗𝚊𝚍𝚒𝚐𝚊𝚋𝚘𝚝』 ](https://t.me/NAAN_1_KANNADIGA)\n"
pm_caption += f"┣Assistant ~ By [『𝙿𝚛𝚘𝚏𝚎𝚜𝚜𝚘𝚛 𝙰𝚐𝚘𝚛𝚊』 ](https://t.me/Mr_Professor_Agora)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『𝙿𝚛𝚘𝚏𝚎𝚜𝚜𝚘𝚛 𝙰𝚐𝚘𝚛𝚊』](https://t.me/NAAN_1_KANNADIGA) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
