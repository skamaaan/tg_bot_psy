from conf import dp, bot
from handlers import admin, client
from client import censor
from aiogram.utils import executor
from db import db_menu_connect as db
from db.ru_dict import PHRASES_DATA


async def start_message(_):
    print("Bot connection OK")
    db.db_connect()


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
censor.register_handlers_censor(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_message)
