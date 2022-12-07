from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.ru_dict import KEYS_DATA

kb_main = InlineKeyboardMarkup(row_width=2)
keys1 = [InlineKeyboardButton(text=KEYS_DATA["appointment"], callback_data="appointment"),
         InlineKeyboardButton(text=KEYS_DATA["about"], callback_data="about"),
         InlineKeyboardButton(text=KEYS_DATA["q_and_a"], callback_data="q_and_a"),
         InlineKeyboardButton(text=KEYS_DATA["guide"], callback_data="guide")
         ]
kb_main.add(*keys1)
