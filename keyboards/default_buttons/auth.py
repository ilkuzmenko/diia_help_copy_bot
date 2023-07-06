from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

auth_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲Авторизація в застосунку"),
            KeyboardButton(text="💻Авторизація на порталі")
        ],
        [
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
