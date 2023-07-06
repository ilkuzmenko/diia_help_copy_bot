from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

diia_signature_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Як створити"),
            KeyboardButton(text="Не можу пройти перевірку PhotoID")
        ],
        [
            KeyboardButton(text="З чим порівнюється моє фото під час підтвердження?"),
            KeyboardButton(text="Немає паспортів, як створити?")
        ],
        [
            KeyboardButton(text="«Виникла проблема при роботі камери» на IOS"),
            KeyboardButton(text="Де зберігається?")
        ],
        [
            KeyboardButton(text="Де використовується?"),
            KeyboardButton(text="Термін дії")
        ],
        [
            KeyboardButton(text="Постанова"),
            KeyboardButton(text="Маю кілька пристроїв")
        ],
        [
            KeyboardButton(text="✍️Запитати менеджера"),
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
