import json
import pathlib
import string
from aiogram import types, Dispatcher


async def bad_words(message: types.Message):
    bw = pathlib.Path("db/bw.json")
    if {i.lower().translate(str.maketrans('', '', string. \
       punctuation)) for i in message.text.split(' ')}. \
       intersection(set(json.load(open(bw)))) != set():
        await message.answer('Bad words!')
        await message.delete()


def register_handlers_censor(dp: Dispatcher):
    dp.register_message_handler(bad_words)
