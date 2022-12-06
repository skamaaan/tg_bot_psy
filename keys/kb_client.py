from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_key = KeyboardButton('В начало')
help_key = KeyboardButton('Помощь')

keys_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keys_main.row(start_key, help_key)
