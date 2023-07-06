from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

services_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔄Внутрішньо переміщеним особам"),
            KeyboardButton(text="📜Військові облігації")
        ],
        [
            KeyboardButton(text="🏠єОселя"),
            KeyboardButton(text="⚖️Виконавчі провадження")
        ],
        [
            KeyboardButton(text="💸Податки ФОП"),
            KeyboardButton(text="🙌Пільги та допомога")
        ],
        [
            KeyboardButton(text="👥Cім'я та міграція"),
            KeyboardButton(text="🏗Будівництво та нерухомість")
        ],
        [
            KeyboardButton(text="🚗Автомобільні послуги"),
            KeyboardButton(text="💶Бізнес")
        ],
        [
            KeyboardButton(text="👨‍🦳Пенсійні послуги"),
            KeyboardButton(text="📄Дублікати, довідки та витяги")
        ],
        [
            KeyboardButton(text="📄Реєстрація нерухомого майна"),
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
