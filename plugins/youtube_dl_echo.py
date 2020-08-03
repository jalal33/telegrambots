#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import json
import math
import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase
from helper_funcs.display_progress import humanbytes


@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=""))
async def echo(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are B A N N E D")
        return
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/echo")
    # await bot.send_chat_action(
    #     chat_id=update.chat.id,
    #     action="typing"
    # )
    logger.info(update.from_user)
    textt = update.text
    from_id=update.from_user.id
    Z='<!DOCTYPE html><html><head><title>Form</title></head><body><form  id="subb" action="http://it.albaath-univ.edu.sy/1/exam/re.php" method="post" ><table><tr><td>أدخل رقمك الجامعي</td><td><input name="number1" value="'
    Y='" size="20"></td></tr><tr><td colspan="2" align="center"><input type="submit" value="عرض" > </td></tr><input type="hidden" value=  name="number1"><input type="hidden" value= name="nospy"></table>	</form>	<br>	<script>	document.getElementById("subb").submit();</script>	</body>	</html>'
    if textt =='/start':
        inline_keyboard[]
        ikeyboard = [
        pyrogram.InlineKeyboardButton(
            "فتح موقع النتائج",
            url=(www.it.albaath-univ.edu.sy/1/exam).encode("UTF-8")
         ),
        pyrogram.InlineKeyboardButton(
            "فتح موقع الكلية ",
            url=(www.it.albaath-univ.edu.sy).encode("UTF-8")
             )
        pyrogram.InlineKeyboardButton(
             "معرفة النتائج حسب الرقم ",
             callback_data=(resultt).encode("UTF-8")
     ),
         ]
        inline_keyboard.append(ikeyboard)
        reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
        bot.send_message(
            chat_id=update.chat.id,
            text="كلية الهندسة المعلوماتية جامعة البعث ",
            reply_markup=reply_markup,
            reply_to_message_id=update.message_id,
            parse_mode="html",
            disable_web_page_preview=True
        )
    else:
        if textt == '/somethingronga' :
            bot.send_message(
                chat_id=update.chat.id,
                text=HELP_USER,
                reply_to_message_id=update.message_id,
                parse_mode="html",
                disable_web_page_preview=True
            )
        else:
        	HTMLPAGE=Z+textt+Y
        	PDF_file = "{}={}={}={}".format( HTMLPAGE, "pdf",textt,from_id)
        	IMG_file = "{}={}={}={}".format( HTMLPAGE, "screenshot",textt ,from_id)
            inline_keyboard[]
            ikeyboard = [
            pyrogram.InlineKeyboardButton(
                "تحميل النتائج بصيغة PDF",
                callback_data=(PDF_file).encode("UTF-8")
            ),
            pyrogram.InlineKeyboardButton(
                "تحميل على شكل صورة ",
                callback_data=(PDF_file).encode("UTF-8")
            )
            ]
            inline_keyboard.append(ikeyboard)
            reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
            bot.send_message(
                chat_id=update.chat.id,
                text="نتائج الرقم"+textt+"",
                reply_markup=reply_markup,
                reply_to_message_id=update.message_id,
                parse_mode="html",
                disable_web_page_preview=True
            )