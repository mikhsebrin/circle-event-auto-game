from pyrogram import idle

import handlers
from bot.bot import bot 


async def main():
    await bot.start()
    async for _ in bot.get_dialogs(): ...

    await idle()


if __name__ == "__main__": 
    bot.run(main())
