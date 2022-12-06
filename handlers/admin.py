from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from admin.create_product import create_menu, load_pic, load_title, load_description
from admin.create_product import load_price, cancel_loading, FSMAdmin, go_to_admin


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(go_to_admin, commands=["admin"], is_chat_admin=True)
    dp.register_message_handler(create_menu, commands=["dlnew"], state=None)
    dp.register_message_handler(cancel_loading, commands=["cload"],  state="*")
    dp.register_message_handler(cancel_loading, Text(equals=["cload"], ignore_case=True), state="*")
    dp.register_message_handler(load_pic, content_types=[types.ContentType.PHOTO], state=FSMAdmin.pic)
    dp.register_message_handler(load_title, state=FSMAdmin.title)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, content_types=[types.ContentType.TEXT], state=FSMAdmin.price)
