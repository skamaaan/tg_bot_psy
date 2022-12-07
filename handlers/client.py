from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from client import services, date_callback, time_callback


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(services.process_start_command, commands=['start'])
    dp.register_message_handler(services.process_help_command, commands=['help'])
    dp.register_message_handler(services.appointment_message, commands=['appointment'])
    dp.register_message_handler(services.about_message, commands=['about'])
    dp.register_callback_query_handler(services.about_callback, text="about")
    dp.register_callback_query_handler(services.q_and_a_callback, text="q_and_a")
    dp.register_callback_query_handler(services.guide_callback, text="guide")
    dp.register_callback_query_handler(services.appointment_button, text="appointment")
    dp.register_callback_query_handler(services.date_selector, date_callback.filter())
    dp.register_callback_query_handler(services.time_selector, time_callback.filter())
    dp.register_callback_query_handler(services.weather, text="weather")
    dp.register_message_handler(services.weather_message, Text(startswith=['погода'], ignore_case=True))
    dp.register_message_handler(services.menu_command, Text(equals=['menu'], ignore_case=True))
