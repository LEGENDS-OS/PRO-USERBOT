from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.helpers.funct import deEmojify
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(KANNADIGA):
    KANNADIGA = KANNADIGA.pattern_match.group(1)
    if not KANNADIGA:
        if KANNADIGA.is_reply:
            (await KANNADIGA.get_reply_message()).message
        else:
            await edit_or_reply(
                KANNADIGA,
                "`Sir please give some query to search and download it for you..!`",
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(KANNADIGA))}")

    await troll[0].click(
        KANNADIGA.chat_id,
        reply_to=KANNADIGA.reply_to_msg_id,
        silent=True if KANNADIGA.is_reply else False,
        hide_via=True,
    )
    await KANNADIGA.delete()


CmdHelp("memevoice").add_command(
    "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()
