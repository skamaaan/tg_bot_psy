from aiogram.utils.executor import start_webhook
from conf import dp, bot
from conf import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
from handlers import admin, client
from client import censor
from db import db_menu_connect as db


async def on_startup(_):
    await bot.set_webhook(WEBHOOK_URL)
    print("Bot connection OK")
    db.db_connect()


async def on_shutdown(dp):
    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
censor.register_handlers_censor(dp)


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
