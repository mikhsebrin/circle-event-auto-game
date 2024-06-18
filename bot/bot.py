from pyrogram import Client

import configs

bot = Client(
    "session",
    api_id=configs.API_ID,
    api_hash=configs.API_HASH, 
)
