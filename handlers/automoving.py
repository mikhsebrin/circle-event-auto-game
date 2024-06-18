import datetime
import asyncio
import re
import random

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import configs
from configs.configs import StartingTypeMoving
from bot.bot import bot


# def shortest_path(current_x, current_y, target_x, target_y):
#     directions = {
#         (-1, 1): '↖️ СЗ',
#         (0, 1): '⬆️ Север',
#         (1, 1): '↗️ СВ',
#         (1, 0): '➡️ Восток',
#         (1, -1): '↘️ ЮВ',
#         (0, -1): '⬇️ Юг',
#         (-1, -1): '↙️ ЮЗ',
#         (-1, 0): '⬅️ Запад'
#     }

#     path = []
    
#     while (current_x, current_y) != (target_x, target_y):
#         dx = target_x - current_x
#         dy = target_y - current_y
        
#         if dx > 0:
#             step_x = 1
#         elif dx < 0:
#             step_x = -1
#         else:
#             step_x = 0
            
#         if dy > 0:
#             step_y = 1
#         elif dy < 0:
#             step_y = -1
#         else:
#             step_y = 0
            
#         step = (step_x, step_y)
#         path.append(directions[step])
        
#         current_x += step_x
#         current_y += step_y

#     return path


async def move_path_generator():
    messages = ["↗️ СВ", "↗️ СВ", "⬆️ Север", "⬆️ Север"]
    while True:
        for message in messages:
            yield message


async def get_message():
    async for message in bot.get_chat_history(configs.BOT_HYPERION_ID):
        text = message.text or message.caption
        if not re.search(r"Если ты не хочешь слышать других игроков - нажми|Ты снова можешь собрать ресурсы", text):
            return text


async def job_moving():
    if configs.TYPE_MOVING == StartingTypeMoving.TYPE_NONE:
        return
    
    elif configs.TYPE_MOVING == StartingTypeMoving.TYPE_TROLLEY:
        for text in ["/start", "🏋️‍♂️ Профиль", "🔙 Назад", "🛒 Телега", "🛒 к ⭕️  Кругу крови"]:
            await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text=text)
            await asyncio.sleep(random.uniform(1.5, 3.3))
        
        await asyncio.sleep(random.uniform(21, 26))
        await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="⭕️  Круг крови")
        await asyncio.sleep(random.uniform(1.5, 3.3))
        await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="🩸  Участвовать")

    elif configs.TYPE_MOVING == StartingTypeMoving.TYPE_WALKING:
        move_path = move_path_generator()
        
        for text in ["/start", "🏋️‍♂️ Профиль", "🔙 Назад", "🛒 Телега", "🛒 к городам...", "🛒 в 🏣 Китс"]:
            await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text=text)
            await asyncio.sleep(random.uniform(1.3, 3.3))

        await asyncio.sleep(random.uniform(21, 26))
        await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="👣 Перемещение")
        await asyncio.sleep(random.uniform(1.3, 3.3))
        await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="↗️ СВ")

        while True:
            await asyncio.sleep(random.uniform(61, 76))

            text = await get_message()

            if re.search(r"↕️:\s-?\d+\s\s↔️:\s-?\d+\s{3}🗺:\s⭕️\s\sКруг\sкрови\s\(Безопасные\sземли\)", text):
                await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="⭕️  Круг крови")
                await asyncio.sleep(random.uniform(1.3, 3.3))
                await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="🩸  Участвовать")
                break
            
            elif re.search(r"Перед тобой стоит", text):
                await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="♿️ Сбежать")
            
            elif re.search(r"Примешь бой или решишь пройти мимо\?", text):
                await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="♿️ Пройти мимо")
            
            elif re.search(r"Тебе удалось пройти мимо мобов|Тебе удалось сбежать от моба", text):
                
                await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text="👣 Перемещение")
                await asyncio.sleep(random.uniform(1.3, 3.3))
                await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text=await move_path.__anext__())
            
            elif re.search(r"^❤️:\s\d+/\d+\s{3}⚡️:\s\d+/\d+\s{3}🍖:\s\d+/\d+\n↕️:\s-?\d+\s{2}↔️:\s-?\d+\s{3}🗺:\sБезопасные\sземли$", text):
                await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text=await move_path.__anext__())
            
            elif re.search(r"^❤️:\s\d+/\d+\s{3}⚡️:\s\d+/\d+\s{3}🍖:\s\d+/\d+\n↕️:\s-?\d+\s{2}↔️:\s-?\d+\s{3}🗺:\sБезопасные\sземли\n\nБой\sс\s.+", text, re.DOTALL):
                await bot.send_message(chat_id=configs.BOT_HYPERION_ID, text=await move_path.__anext__())
            else:
                print(text)
                break

scheduler = AsyncIOScheduler()
moscow_tz = datetime.timezone(datetime.timedelta(hours=3))

scheduler.add_job(job_moving, "cron", hour=17, minute=6, timezone=moscow_tz, jitter=60 * 3)

scheduler.start()
