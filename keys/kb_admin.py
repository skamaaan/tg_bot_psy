from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_add = KeyboardButton('/dlnew')
menu_del = KeyboardButton('/dlrem')

keys_admin = ReplyKeyboardMarkup(resize_keyboard=True).\
    add(menu_add).add(menu_del)
