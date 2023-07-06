from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

notifications_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔔Сповіщення про кредити"),
            KeyboardButton(text="📖Судові сповіщення та справи")
        ],
        [
            KeyboardButton(text="🧒Про оздоровлення дитини"),
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
