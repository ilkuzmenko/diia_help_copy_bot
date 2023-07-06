from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

diia_partners_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✉️Дія.QR"),
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
