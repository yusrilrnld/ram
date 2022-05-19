from time import sleep
from userbot.utils import edit_or_reply, ram_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd, owner
eor = edit_or_reply

@ram_cmd(pattern='pay(?: |$)(.*)')
async def _(event):
    await eor(event, f"`Sedang Menulis Payment {owner}`")
    sleep(2)
    await eor(event, "`Mohon Tunggu.....`")
    sleep(1)
    await eor(event, "` **PAYMENT ACENG • STOREE \n\n DANA = 0895611203477 \n\nㅤPAYMENT ACENG • STOREE \n\nㅤGOPAY = 081270603368 \n\nㅤ★@ACENG_STOREE★**`")
    # Create by myself @YUSRIL4YOU


@ram_cmd(pattern='pay2(?: |$)(.*)')
async def _(event):
    await eor(event, "`Sabar Ya Kak`")
    sleep(3)
    await eor(event, "`Mohon Tunggu Beberapa Detik....`")
    sleep(3)
    await eor(event, "`Yah Kosong Kak Maaf🥺`")
# Create by myself @yusril4you


@ram_cmd(pattern='pay3(?: |$)(.*)')
async def _(event):
    await eor(event, "`Sedang Mengetik....`")
    sleep(2)
    await eor(event, "`Mohon Bersabar....`")
    sleep(3)
    await eor(event, "`\n\nㅤPAYMENT ACENG • STOREE \n\n DANA = 0895611203477 \n\n\n\nㅤ ACENG • STOREE \n\nㅤGOPAY = 081270603368  \n\n\n\nㅤㅤ★@ACENG_STOREE★`")
# Create by myself @yusril4you

CMD_HELP.update(
    {
       "payments": f"**Plugin :** payments.\
       \n\n    • Syntax : `{cmd}pay`\
       \n     • **Function: **Untuk Menulis Payments.\
       \n\n    •  Syntax : `{cmd}pay2`\
       \n     • **Function: **Untuk Menulis Payments.\
       \n\n    •  Syntax : `{cmd}pay3`\
       \n     • **Function: **Untuk Menulis Payments.\
    "
    }
)
