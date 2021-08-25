import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config


# =
usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()
caption_text = """
〰️〰️〰️〰️〰️〰️〰️〰️〰️

<b>╭─🔅 ᴜᴘʟᴏᴀᴅ ʙʏ 🔅 ─╮</b>

<b>├•</b> <i>@AnimeHubFlix</i>

<b>├•</b> <i>@AniMoviesFlix</i>

<b>╰─────────────╯</b>

〰️〰️〰️〰️〰️〰️〰️〰️〰️
"""


@autocaption.on_message(filters.channel & (filters.document | filters.video | filters.audio ) & ~filters.edited, group=-1)
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = """〰️〰️〰️〰️〰️〰️〰️〰️〰️
<b>╭─🔅 ᴜᴘʟᴏᴀᴅ ʙʏ 🔅 ─╮</b>
<b>├•</b> <i>@AnimeHubFlix</i>
<b>├•</b> <i>@AniMoviesFlix</i>
<b>╰─────────────╯</b>
〰️〰️〰️〰️〰️〰️〰️〰️〰️
"""
      except:
         caption_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"<b>{message.caption}</b>"                
          else:
             fname = media.file_name
             filename = fname.replace("_", ".")
             file_caption = f"<code>{filename}</code>"  
              
      try:
          if caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = caption_text + file_caption,
                 parse_mode = "html"
             )
          elif caption_position == "bottom":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = file_caption + "\n" + caption_text,
                 parse_mode = "html"
             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.message_id,
                 caption = caption_text, 
                 parse_mode = "html"
             ) 
      except:
          pass
              
                   
      
