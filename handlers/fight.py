import asyncio
import re
import random

from pyrogram import filters

import configs
from bot.bot import bot

check = None
users_in_circle = None

@bot.on_message(
    filters.chat(configs.BOT_HYPERION_FIGHT_ID) &
    filters.regex("Бой в 🩸  круге крови начался!")

)
async def _(client, message):
    global users_in_circle, check
    check = True
    
    users_in_circle = set(re.findall(r"🕳 ([а-яёa-z]+) ", message.text, re.I))
    
    await asyncio.sleep(random.uniform(3, 6))
    await message.reply("🔪 Ударить...")


@bot.on_message(
    filters.create(lambda _, __, ___: check) &
    filters.user(configs.BOT_HYPERION_FIGHT_ID) & filters.regex("^Ударить$")
)
async def _(client, message):
    global check
    check = False

    users_keyboard = set([name[0].split()[3] for name in message.reply_markup.keyboard[:-1]])
    my_name = list(users_in_circle - users_keyboard)[0]
    
    await bot.send_message(configs.BOT_CIRCLE_ID, f"Твои статы:\n🕳 {my_name} - 1000/1000❤️ 1000/1000🔮")


@bot.on_message(
    filters.private &
    filters.user(configs.BOT_CIRCLE_ID) &
    filters.regex(re.compile(r"🔪 ➡️ 🕳 [а-яёa-z]+", re.I))
)
async def _(client, message):
    name = message.matches[0].group(0)
    await asyncio.sleep(random.uniform(3, 6))
    
    await bot.send_message(chat_id=configs.BOT_HYPERION_FIGHT_ID ,text=name)
