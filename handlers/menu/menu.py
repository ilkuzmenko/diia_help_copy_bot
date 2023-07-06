from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message

from handlers.menu.digital_docs import DigitalDocsState
from keyboards.default_buttons import *
from loader import dp


@dp.message_handler(Command("start"))
async def start(message: Message):
    await message.answer(
        "🕹Будь ласка, тепер оберіть кнопками, якого продукту стосується ваше запитання:\n"
        "– 📱цифрових документів\n"
        "– 🗃послуг"
        "\n\n"
        "Це необхідно для того, щоб ви отримали відповідь тільки стосовно обраного продукту або ж поставили запитання менеджеру, який спеціалізується на ньому.",
        reply_markup=menu_buttons
    )


@dp.message_handler(Text(equals=["↩️Назад"]))
async def back_to_start(message: Message):
    await message.answer(
        "🕹Будь ласка, тепер оберіть кнопками, якого продукту стосується ваше запитання:\n"
        "– 📱цифрових документів\n"
        "– 🗃послуг"
        "\n\n"
        "Це необхідно для того, щоб ви отримали відповідь тільки стосовно обраного продукту або ж поставили запитання менеджеру, який спеціалізується на ньому.",
        reply_markup=menu_buttons
    )


@dp.message_handler(Text(equals=["📱Цифрові документи"]))
async def digital_docs_command(message: Message):
    await message.answer(
        "Забуті вдома документи — це вже історія з бородою. Маємо всю важливу інформацію під рукою: від того, як користуватись кожним, їх юридичну силу до типових питань по кожному. Сам користуюсь і вам раджу."
        "\n\n"
        "🕹Обирайте кнопками документ, щоб потрапити на типові відповіді про нього або щоб отримати допомогу від менеджера",
        reply_markup=digital_docs_buttons
    )
    await DigitalDocsState.waiting_for_select.set()


@dp.message_handler(Text(equals=["🗃Послуги"]))
async def services_command(message: Message):
    await message.answer("🕹Обирайте кнопками блок питань, який вас цікавить", reply_markup=services_buttons)


@dp.message_handler(Text(equals=["📲Авторизація"]))
async def auth_command(message: Message):
    await message.answer(
        "Авторизуйтесь в застосунку або на порталі, щоб підтвердити, що ви – це дійсно ви, а також користуватися документами чи послугами.",
        reply_markup=auth_buttons
    )


@dp.message_handler(Text(equals=["✍️Дія.Підпис"]))
async def diia_signature_command(message: Message):
    await message.answer(
        "Дія.Підпис – це кваліфікований електронний підпис, який дає\n"
        "змогу підтвердити цілісність електронного документа та\n"
        "ідентифікувати підписувача. Це аналог власноручного підпису.\n\n"
        "Вибирайте відповідь кнопками 🕹або запитайте менеджера ✍️",
        reply_markup=diia_signature_buttons
    )


@dp.message_handler(Text(equals=["🏚єВідновлення"]))
async def e_repair_command(message: Message):
    await message.answer(
        "Подавайте заявку в застосунку Дія на компенсацію\n"
        "пошкодженого майна за допомогою послуги єВідновлення.\n\n"
        "Перший етап уже розпочали: якщо майно підлягає ремонту –\n"
        "заповніть і надішліть заяву на компенсацію.\n\n"
        "Згодом буде доступний другий етап – для осіб, майно яких\n"
        "знищено повністю.",
        reply_markup=e_repair_buttons
    )


@dp.message_handler(Text(equals=["💡Обмін лампочок"]))
async def lamps_exchange_command(message: Message):
    await message.answer(
        "Кожен українець зможе безкоштовно отримати\n"
        "енергозберігаючі LED-лампи. На заміну треба віддати старі\n"
        "лампи розжарювання. Лишайте заявку в застосунку Дія,\n"
        "приходьте в обране відділення Укрпошти та обмінюйте лампи.\n\n"
        "Зробіть свій внесок у балансування електросистеми України!",
        reply_markup=lamps_exchange_buttons
    )


@dp.message_handler(Text(equals=["😔Втратив телефон"]))
async def lost_phone_command(message: Message):
    await message.answer(
        "Нам прикро, що трапилася така ситуація! Для безпеки "
        "персональних даних радимо вам виконати наступні кроки:"
        "\n\n"
        "✔️авторизуватися в застосунку на іншому пристрої;\n"
        "✔️в меню обрати «Підключені пристрої»;\n"
        "✔️видалити всі пристрої."
        "\n\n"
        "❗️Пам'ятайте, що також слід оновити паролі у вашому банкінгу.",
        parse_mode="HTML"
    )


@dp.message_handler(Text(equals=["🚀Партнерам Дії"]))
async def diia_partners_command(message: Message):
    await message.answer(
        "Якщо ви бажаєте приймати у своємо бізнесі цифрові документи, то ми з радістю допоможемо вам в цьому."
        "\n\n"
        "🕹Обирайте кнопками блок питань, який вас цікавить або запитайте у менеджера",
        reply_markup=diia_partners_buttons
    )

@dp.message_handler(Text(equals=["😀Де приймають Дію?"]))
async def where_diia_accepted_command(message: Message):
    await message.answer(
        "Подорожуйте країною, отримуйте поштові відправлення та відкривайте рахунки в банках без паперових документів – https://paperless.diia.gov.ua/",
        reply_markup=where_diia_accepted_buttons
    )


@dp.message_handler(Text(equals=["🪖Повідом ЗСУ про ворога"]))
async def inform_about_enemy_command(message: Message):
    await message.answer(
        "❗️Побачили ворожу техніку чи солдатів?"
        "\n\n"
        "Фотографуйте, знімайте на відео, вказуйте їх геопозицію та діліться ними із ЗСУ через чатбот єВорог – https://t.me/evorog_bot"
        "\n\n"
        "Усі дані ми оперативно перевіряємо та передаємо в ЗСУ. Це допоможе відстежувати пересування окупанта та швидко дати гідну відсіч.",
        parse_mode="HTML"
    )


@dp.message_handler(Text(equals=["🔔Сповіщення"]))
async def notifications_command(message: Message):
    await message.answer(
        "З ними можна потурбуватися про свою фінансову та адміністративну безпеку"
        "\n\n"
        "Вибирайте кнопками блок питань, який вас цікавить 🕹або запитайте у менеджера ✍️",
        reply_markup=notifications_buttons
    )


@dp.message_handler(Text(equals=["🙎‍♂️Мій профіль"]))
async def my_profile_command(message: Message):
    await message.answer(
        f"👤Вказуйте в профілі ім’я, прізвище та номер телефону, щоб у подальшому команда підтримки одразу знала, як до вас звертатися"
        f"\n\n"
        f"ℹ️Номер телефону допоможе оперативно знайти та відслідковувати статус ваших тікетів"
        f"\n\n"
        f"▪️ Ім'я: {message.from_user.first_name}\n"
        f"▪️ Прізвище: {message.from_user.last_name}\n"
        f"▪️ Телефон: [Не вказано]\n"
        f"▪️ Email: [Не вказано]"
        f"\n\n"
        f"🕹Будь ласка, обирайте кнопками, що саме ви б хотіли зробити",
        reply_markup=my_profile_buttons
    )
