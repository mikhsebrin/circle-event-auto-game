from pyrogram import filters

from bot.bot import bot

@bot.on_message(
    filters.me & filters.command("work_check")

)
async def _(client, message):
    await message.reply("Работаю!")
