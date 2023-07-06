from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱Цифрові документи"),
            KeyboardButton(text="🗃Послуги")
        ],
        [
            KeyboardButton(text="📲Авторизація"),
            KeyboardButton(text="✍️Дія.Підпис")
        ],
        [
            KeyboardButton(text="🏚єВідновлення"),
            KeyboardButton(text="💡Обмін лампочок")
        ],
        [
            KeyboardButton(text="😔Втратив телефон"),
            KeyboardButton(text="🚀Партнерам Дії")
        ],
        [
            KeyboardButton(text="😀Де приймають Дію?"),
            KeyboardButton(text="🪖Повідом ЗСУ про ворога")
        ],
        [
            KeyboardButton(text="🔔Сповіщення"),
            KeyboardButton(text="🙎‍♂️Мій профіль")
        ],
    ],
    resize_keyboard=True
)
