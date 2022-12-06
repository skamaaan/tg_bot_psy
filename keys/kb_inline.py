from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ukb = InlineKeyboardMarkup(row_width=3)
uk1 = InlineKeyboardButton(text='link1', callback_data='dlnew')
uk2 = InlineKeyboardButton(text='link2', url='google.com')
keys1 = [InlineKeyboardButton(text='link1', url='ya.ru'),
         InlineKeyboardButton(text='link1', url='ya.ru'),
         InlineKeyboardButton(text='link1', url='ya.ru')]
ukb.add(uk1, uk2).row(*keys1)
