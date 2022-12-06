from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from conf import bot
from db import db_menu_connect as db
from keys import kb_admin

ID = None


class FSMAdmin(StatesGroup):
    pic = State()
    title = State()
    description = State()
    price = State()


async def go_to_admin(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(ID, "Do admin!", reply_markup=kb_admin.keys_admin)
    await message.delete()


async def create_menu(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.pic.set()
        await message.answer('1. Download picture')
    else:
        await message.answer('Forbidden')


async def cancel_loading(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Canceled!!!")


async def load_pic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["pic"] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.delete()
        await message.answer('2. White the title')


async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["title"] = message.text
        await FSMAdmin.next()
        await message.delete()
        await message.answer('3. White the description')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
        await FSMAdmin.next()
        await message.delete()
        await message.answer('4. Set price')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = float(message.text)
        data["user"] = message.from_user.id
        await message.delete()
    await db.db_add(state)
    await state.finish()
