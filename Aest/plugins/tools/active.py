from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from Aest import app
from Aest.misc import SUDOERS
from Aest.utils.inline import close_markup
from Aest.utils.decorators.language import language
from Aest.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "activevoice", "ac"]) & SUDOERS)
@language
async def activevc(client, message: Message,_):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_chats()
    video_chats = await get_active_video_chats()
    text = ""
    j = 0
    if "-list" in message.text:
        for x in served_chats:
            try:
                title = (await app.get_chat(x)).title
            except:
                await remove_active_chat(x)
                continue
            try:
                if (await app.get_chat(x)).username:
                    user = (await app.get_chat(x)).username
                    text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
                else:
                    text += (f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n")
                j += 1
            except:
                continue
        if len(served_chats)==0:
            await mystic.edit_text(text=f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ {app.mention}.",reply_markup=close_markup(_))
            
        return await mystic.edit_text(f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs :</b>\n\n{text}", disable_web_page_preview=True,reply_markup=close_markup(_))
    #   await mystic.edit_text(f"✫ <b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</b></u> : \n\n**ᴀᴜᴅɪᴏ** : {len(served_chats)} \n **ᴠɪᴅᴇᴏ**  : {len(video_chats)} ")
    if len(served_chats)==0:
        await mystic.edit_text(text=f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ {app.mention}.",reply_markup=close_markup(_),
)
    else:
        await mystic.edit_text(text=f"✫ <b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</b></u> : \n\n ᴀᴜᴅɪᴏ : {len(served_chats)} \n ᴠɪᴅᴇᴏ  : {len(video_chats)} ",reply_markup=close_markup(_))

@app.on_message(filters.command(["activev", "activevideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
