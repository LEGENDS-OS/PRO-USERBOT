from telethon import version

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.utils import *

# -------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "KANNADIGA"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

KANNADIGA = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={KANNADIGA})"


PM_IMG = "https://te.legra.ph/file/c085085b63638ae1ba5cf.jpg"
pm_caption = "**𝙺𝚊𝙽𝚗𝚊𝙳𝚒𝙶𝚊 𝚋𝙾𝚝 𝙸𝚜 𝚘𝙽𝚕𝚒𝙽𝚎**\n\n"

pm_caption += f"**┏🔥𝐊𝐀𝐍𝐍𝐀𝐃𝐈𝐆𝐀 𝐁𝐎𝐓🔥┓**\n"
pm_caption += f"**┣😎 𝙼𝙰𝚂𝚃𝙴𝚁:{mention}**\n"
pm_caption += f"**┣⚡ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 : `{version.__version__}`**\n"
pm_caption += f"**┣🌍 𝙺𝙰𝙽𝙽𝙰𝙳𝙸𝙶𝙰𝙱𝙾𝚃 :{KANNADIGAversion}**\n"
pm_caption += f"**┣😈 𝚂𝚄𝙳𝙾     : `{sudou}`**\n"
pm_caption += f"**┣👨‍🏫 𝙾𝚆𝙽𝙴𝚁     : [𝙺𝙰𝙽𝙽𝙰𝙳𝙸𝙶𝙰](https://t.me/Mr_Professor_Agora)**\n"
pm_caption += f"**┗[💛𝙶𝚁𝙾𝚄𝙿❤️](https://t.me/NAAN_1_KANNADIGA)┛**\n"

pm_caption += "    [✨ 𝚁𝙴𝙿𝙾 ✨](https://github.com/MR-KANNADIGA/KANNADIGABOT) 🔹 [📜License📜](https://github.com/MR-KANNADIGA/KANNADIGABOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "bot",
    None,
    "Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg",
).add_warning(
    "Harmless Module"
).add_info(
    "Are u alive?"
).add_type(
    "Official"
).add()
