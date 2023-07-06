from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

where_diia_accepted_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏛️Державні установи"),
            KeyboardButton(text="✈️Подорожі та туризм")
        ],
        [
            KeyboardButton(text="Магазини та супермаркети"),
            KeyboardButton(text="💳Фінансові установи")
        ],
        [
            KeyboardButton(text="Поштові компанії"),
            KeyboardButton(text="🗒Інше")
        ],
        [
            KeyboardButton(text="↩️Назад")
        ]
    ],
    resize_keyboard=True
)
