from aiogram import types
from conf import bot
from keys import kb_client, kb_inline
from db import db_menu_connect as db


async def process_start_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello! Click on action')
        await message.delete()
    except:
        await message.reply('Write personal message, please!')


async def menu_command(message):
    await db.db_read(message)


async def process_help_command(message: types.Message):
    await message.answer("Hello, <a href='google.com'>world</a>!", parse_mode=types.ParseMode.HTML)
    await message.delete()
