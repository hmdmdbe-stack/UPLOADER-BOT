#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modifieded By : @DC4_WARRIOR

import os
import logging
import asyncio
from config import Config
from pyrogram import Client as Clinton

# إعداد السجلات
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

if __name__ == "__main__" :
    # إنشاء مجلد التحميل إذا لم يكن موجوداً
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    
    plugins = dict(root="plugins")
    
    # تعريف البوت مع إضافة خاصية مزامنة الوقت
    Warrior = Clinton(
        "WarriorBot", # يفضل استخدام اسم نصي بسيط هنا بدل المعرف
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        sleep_threshold=60 # يساعد في تجنب الحظر المؤقت عند كثرة الطلبات
    )
    
    # تشغيل البوت
    print("جاري تشغيل البوت...")
    Warrior.run()
