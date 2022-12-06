from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from client.services import process_start_command, process_help_command, menu_command


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_start_command, Text(equals=['В начало']))
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_help_command, Text(equals=['Помощь']))
    dp.register_message_handler(menu_command, Text(equals=['menu'], ignore_case=True))
