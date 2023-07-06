from aiogram.types import Message, ContentTypes

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.default_buttons import menu_buttons
from loader import dp

""" [INFO] This is an example of using FCM to implement a menu with more than 2 attachments """

class DigitalDocsState(StatesGroup):
    waiting_for_select = State()


@dp.message_handler(state=DigitalDocsState.waiting_for_select, content_types=ContentTypes.TEXT)
async def digital_docs_state(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['doc'] = message.text

    if data['doc'] == "↩️Назад":
        await state.finish()
        await message.answer(
            "🕹Будь ласка, тепер оберіть кнопками, якого продукту стосується ваше запитання:\n"
            "– 📱цифрових документів\n"
            "– 🗃послуг\n\n"
            "Це необхідно для того, щоб ви отримали відповідь тільки стосовно обраного продукту або ж поставили запитання менеджеру, який спеціалізується на ньому.",
            reply_markup=menu_buttons
        )
        return
