import logging
import os

from aiogram import executor
from handlers import dp
from utils.notifyer import message_to_admins

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO
)


async def on_startup(dp) -> None:
    await message_to_admins("I'm /start")


if __name__ == '__main__':

    path_log_file = os.path.dirname(os.path.abspath(__file__)) + '/launched_now'

    if not os.path.isfile(path_log_file):
        with open(path_log_file, 'w') as file:
            file.write('Bot launched!')
        try:
            executor.start_polling(dp, on_startup=on_startup)
        finally:
            os.remove(path_log_file)
    else:
        logging.info("Bot launched now. Finishing processes. Goodbye!")
