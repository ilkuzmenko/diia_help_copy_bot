from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

e_repair_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Як подати заяву?"),
            KeyboardButton(text="🤔Даних про майно не знайдено")
        ],
        [
            KeyboardButton(text="Хто може отримати послугу?"),
            KeyboardButton(text="Умови послуги?")
        ],
        [
            KeyboardButton(text="Який термін розгляду заяви?"),
            KeyboardButton(text="Через який час я отримаю кошти?")
        ],
        [
            KeyboardButton(text="Які документи необхідні?"),
            KeyboardButton(text="Як співвласнику підтвердити заяву?")
        ],
        [
            KeyboardButton(text="На що можна витратити кошти?"),
            KeyboardButton(text="🤝Долучитись як бізнес")
        ],
        [
            KeyboardButton(text="Що робити після подачі?"),
            KeyboardButton(text="✍️Запитати менеджера")
        ],
        [
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
