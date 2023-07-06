from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

my_profile_buttons = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="🔧Оновити дані"),
			KeyboardButton(text="💬Мої звернення")
		],
		[
			KeyboardButton(text="↩️Назад")
		]
	],
	resize_keyboard=True
)
