import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

mem_storage = MemoryStorage()

# webhook settings
WEBHOOK_HOST = 'https://skaman.v6.navy'
WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'skaman.v6.navy'  # or ip
WEBAPP_PORT = 3001

WEATHER_TOKEN = os.getenv("OW_TOKEN")
bot = Bot(str(os.getenv("BOT_TOKEN")))
dp = Dispatcher(bot, storage=mem_storage)
dp.middleware.setup(LoggingMiddleware())
