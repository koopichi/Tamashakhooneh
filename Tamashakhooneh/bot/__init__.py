from ..config import Telegram
from pyrogram import Client

if Telegram.SECONDARY:
    plugins=None
    no_updates=True
else:    
    plugins={"root": "Tamashakhooneh/bot/plugins"}
    no_updates=None

Tamashakhooneh = Client(
    name="Tamashakhooneh",
    api_id=Telegram.API_ID,
    api_hash=Telegram.API_HASH,
    workdir="Tamashakhooneh",
    plugins=plugins,
    bot_token=Telegram.BOT_TOKEN,
    sleep_threshold=Telegram.SLEEP_THRESHOLD,
    workers=Telegram.WORKERS,
    no_updates=no_updates
)

multi_clients = {}
work_loads = {}

