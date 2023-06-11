from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
import random

from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

force_channel = "crazy_cinemas_official"

PICS = [
 "https://telegra.ph/file/0a0a44828a9854bab75a7.jpg",
 "https://telegra.ph/file/00b81ceb39ff1e1128c34.jpg"
]

VID = [
 "https://telegra.ph/file/d5082ef18ad41aa35d074.mp4"
]

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, update.from_user.id)
            if user.status == "kicked out":
                await update.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await update.reply_text(
                text="🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭.\n\nനിങ്ങൾക്ക് മൂവീസ് വേണോ? എങ്കിൽ തായെ കാണുന്ന ഞങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യുക.😂\nഎന്നിട്ട് ഗ്രൂപ്പിൽ പോയി വീണ്ടും മൂവിയിൽ ക്ലിക് ചെയ്ത് start കൊടുത്തു നോക്കൂ..!😁",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
   
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type, file_size = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
     #CUSTOM FILE CAPTION   
        caption=f"""Hey {update.from_user.mention} 😍
        
<code>{file_name} </code>

⚠ ഈ ഫയൽ ശരിയായി പ്രവർത്തിക്കാൻ ഞങ്ങളുടെ ചാനലിലും ഗ്രൂപ്പിലും ചേരുക..!!

♻️ 𝙅𝙊𝙄𝙉 :- @crazy_cinemas_official
♻️ 𝙅𝙊𝙄𝙉 :- @crazy_cinemas_group"""
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                reply_markup=InlineKeyboardMarkup( [[
                    InlineKeyboardButton("🔰 SUPPORT GROUP 🔰", url="t.me/crazy_cinemas_group"),
                    ],[
                    InlineKeyboardButton("💠 SUPPORT CHANNEL 💠", url="https://t.me/crazy_cinemas_official")
                    ]]
                    )
                )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode=enums.ParseMode.HTML)
            LOGGER(__name__).error(e)
        return
#pmstart
    buttons = [[
                    InlineKeyboardButton("🔰 SUPPORT GROUP 🔰", url="t.me/crazy_cinemas_group")
                ],[
                    InlineKeyboardButton("💠 SUPPORT CHANNEL 💠", url="https://t.me/crazy_cinemas_official")
           ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=reply_markup,
        reply_to_message_id=update.id
    )
    await update.reply_video(
        video=random.choice(VID),
        caption=f"""Hey {update.from_user.mention},
        
Here is my kiss for my dear... 💋
Go to Group for Movies...!!

@crazy_cinemas_official"""
    )
     
     
     
