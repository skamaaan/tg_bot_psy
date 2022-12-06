import calendar
from datetime import datetime, timedelta

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types import CallbackQuery

# setting callback_data prefix and parts
date_callback = CallbackData('simple_calendar', 'act', 'year', 'month', 'day')
time_callback = CallbackData('simple_time', 'act', 'time')


class SimpleDate:

    async def start_date(
            self,
            year: int = datetime.now().year,
            month: int = datetime.now().month
    ) -> InlineKeyboardMarkup:
        """
        Creates an inline keyboard with the provided year and month
        :param int year: Year to use in the calendar, if None the current year is used.
        :param int month: Month to use in the calendar, if None the current month is used.
        :return: Returns InlineKeyboardMarkup object with the calendar.
        """
        inline_kb = InlineKeyboardMarkup(row_width=7)
        ignore_callback = date_callback.new("IGNORE", year, month, 0)  # for buttons with no answer

        # Second row - Week Days
        inline_kb.row()
        for day in ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]:
            inline_kb.insert(InlineKeyboardButton(day, callback_data=ignore_callback))

        # Calendar rows - Days of month
        month_calendar = calendar.monthcalendar(year, month)
        for week in month_calendar:
            inline_kb.row()
            for day in week:
                if day == 0:
                    inline_kb.insert(InlineKeyboardButton(" ", callback_data=ignore_callback))
                    continue
                inline_kb.insert(InlineKeyboardButton(
                    str(day), callback_data=date_callback.new("DAY", year, month, day)
                ))

        # Last row - Buttons
        inline_kb.row()
        inline_kb.insert(InlineKeyboardButton(
            "< пред", callback_data=date_callback.new("PREV-MONTH", year, month, day)
        ))
        inline_kb.insert(InlineKeyboardButton(
            f'{calendar.month_name[month]} {str(year)}',
            callback_data=ignore_callback
        ))
        inline_kb.insert(InlineKeyboardButton(
            "след >", callback_data=date_callback.new("NEXT-MONTH", year, month, day)
        ))

        return inline_kb

    async def process_date_selection(self, query: CallbackQuery, data: CallbackData) -> tuple:
        """
        Process the callback_query. This method generates a new calendar if forward or
        backward is pressed. This method should be called inside a CallbackQueryHandler.
        :param query: callback_query, as provided by the CallbackQueryHandler
        :param data: callback_data, dictionary, set by date_callback
        :return: Returns a tuple (Boolean,datetime), indicating if a date is selected
                    and returning the date if so.
        """
        return_data = (False, None)
        temp_date = datetime(int(data['year']), int(data['month']), 1)
        # processing empty buttons, answering with no action
        if data['act'] == "IGNORE":
            await query.answer(cache_time=60)
        # user picked a day button, return date
        if data['act'] == "DAY":
            await query.message.delete_reply_markup()  # removing inline keyboard
            return_data = True, datetime(int(data['year']), int(data['month']), int(data['day']))
        # user navigates to previous month, editing message with new calendar
        if data['act'] == "PREV-MONTH":
            prev_date = temp_date - timedelta(days=1)
            await query.message.edit_reply_markup(await self.start_calendar(int(prev_date.year), int(prev_date.month)))
        # user navigates to next month, editing message with new calendar
        if data['act'] == "NEXT-MONTH":
            next_date = temp_date + timedelta(days=31)
            await query.message.edit_reply_markup(await self.start_calendar(int(next_date.year), int(next_date.month)))
        # at some point user clicks DAY button, returning date
        return return_data


class SimpleTime:

    async def start_time(self) -> InlineKeyboardMarkup:
        """
        Creates an inline keyboard with the provided year and month
        :param hour_minute:
        :return: Returns InlineKeyboardMarkup object with the calendar.
        """
        inline_kb = InlineKeyboardMarkup(row_width=5)
        # for buttons with no answer
        ignore_callback = time_callback.new("IGNORE", 0)

        # Rows time
        inline_kb.row()
        for time_select in [["9", "00"], ["10", "30"], ["12", "00"], ["13", "30"], ["15", "00"]]:
            inline_kb.insert(InlineKeyboardButton(
                time_select[0]+":"+time_select[1],
                callback_data=time_callback.new("TIMEam", time_select[0]+time_select[1])
            ))

        # inline_kb.row()
        # for time_select in ["16.30", "18.00", "19.30", "21.00", "22.30"]:
        #     inline_kb.insert(InlineKeyboardButton(
        #         str(time_select), callback_data=time_callback.new("TIMEpm", time_select.split("."))
        #     ))

        return inline_kb

    async def process_time_selection(self, query: CallbackQuery, data: CallbackData) -> tuple:
        """
        Process the callback_query. This method generates a new calendar if forward or
        backward is pressed. This method should be called inside a CallbackQueryHandler.
        :param query: callback_query, as provided by the CallbackQueryHandler
        :param data: callback_data, dictionary, set by date_callback
        :return: Returns a tuple (Boolean,datetime), indicating if a date is selected
                    and returning the date if so.
        """
        return_data = (False, None)
        # processing empty buttons, answering with no action
        if data['act'] == "IGNORE":
            await query.answer(cache_time=60)
        # user picked a day button, return date
        if data['act'] == "TIMEam":
            await query.message.delete_reply_markup()   # removing inline keyboard
            return_data = True, datetime.strptime(data['time'], "%H%M")
        # user picked a day button, return date
        # if data['act'] == "TIMEpm":
        #     await query.message.delete_reply_markup()   # removing inline keyboard
        #     return_data = True, data['time']
        # at some point user clicks DAY button, returning date
        return return_data
