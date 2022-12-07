from aiogram import types

from client import Date, date_callback, Time
from client.appo import appo
from conf import bot
from keys import kb_client
from db import db_menu_connect as db, ru_dict
from weather.weather import get_weather


async def process_start_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               ru_dict.PHRASES_DATA["start_action"],
                               reply_markup=kb_client.kb_main)
        await message.delete()
    except:
        await message.reply('Write personal message, please!')


async def appointment_message(message: types.Message):
    await message.answer(ru_dict.PHRASES_DATA["appointment"])
    await message.delete()


async def appointment_callback(callback: types.CallbackQuery):
    await callback.message.answer(ru_dict.PHRASES_DATA["appointment"])


async def about_message(message: types.Message):
    await message.answer(ru_dict.PHRASES_DATA["about"])
    await message.delete()


async def about_callback(callback: types.CallbackQuery):
    await callback.message.answer(ru_dict.PHRASES_DATA["about"])


async def q_and_a_callback(callback: types.CallbackQuery):
    await callback.message.answer(ru_dict.PHRASES_DATA["q_and_a"])


async def guide_callback(callback: types.CallbackQuery):
    await callback.message.answer(ru_dict.PHRASES_DATA["guide"])


async def menu_command(message):
    await db.db_read(message)


async def weather(callback: types.CallbackQuery):
    await callback.message.answer("В каком городе спросить про погоду?"
                                  "Напишите 'погода в...'")


async def weather_message(message: types.Message):
    city = message.text.split()
    await message.answer(get_weather(city[-1]))


async def appointment_button(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите дату: ",
                                  reply_markup=await Date().start_date())


async def date_selector(callback: types.CallbackQuery, callback_data: dict):
    selected, date = await Date().process_date_selection(callback, callback_data)
    if selected:
        appo.clear()
        await callback.message.edit_text(
            f'Время:',
            reply_markup=await Time().start_time())
        appo.append([date.strftime("%Y"), (date.strftime("%m")), (date.strftime("%d"))])
        print(f'1 ---- {appo}')


async def time_selector(callback: types.CallbackQuery, callback_data: list):
    selected, time = await Time().process_time_selection(callback, callback_data)
    if selected:
        appo.append([time.strftime("%H"), time.strftime("%M")])
        await callback.message.edit_text(
            f'Выбрана дата: {appo[0][2]}.{appo[0][1]}.{appo[0][0]}г.\n'
            f'Время: {appo[1][0]}:{appo[1][1]}',

            reply_markup=None
        )
        print(f'2 ---- {appo}')


async def process_help_command(message: types.Message):
    await message.answer("Hello, <a href='google.com'>world</a>!", parse_mode=types.ParseMode.HTML)
    await message.delete()
