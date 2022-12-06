import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

mem_storage = MemoryStorage()
WEATHER_TOKEN = os.getenv("OW_TOKEN")
bot = Bot(str(os.getenv("BOT_TOKEN")))
dp = Dispatcher(bot, storage=mem_storage)
