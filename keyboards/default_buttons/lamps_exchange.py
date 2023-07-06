from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lamps_exchange_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Фізичним особам"),
            KeyboardButton(text="🏥Юридичним особам")
        ],
        [
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
