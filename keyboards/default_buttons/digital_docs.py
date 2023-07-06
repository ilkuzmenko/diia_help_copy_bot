from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

digital_docs_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝Довідка ВПО"),
            KeyboardButton(text="🛻Посвідчення водія")
        ],
        [
            KeyboardButton(text="🚘Техпаспорт"),
            KeyboardButton(text="🎉ID-карта та закордонний паспорт")
        ],
        [
            KeyboardButton(text="🪖єДокумент"),
            KeyboardButton(text="🧪COVID-сертифікат")
        ],
        [
            KeyboardButton(text="💳Посвідка"),
            KeyboardButton(text="🔖Страховий поліс")
        ],
        [
            KeyboardButton(text="📃Свідоцтво про народження"),
            KeyboardButton(text="👨‍🦳Пенсійне посвідчення")
        ],
        [
            KeyboardButton(text="📈Картка платника податків"),
            KeyboardButton(text="🎫Студентський квиток")
        ],
        [
            KeyboardButton(text="🏛Нота"),
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
