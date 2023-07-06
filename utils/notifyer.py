import logging
import time

from config import ADMINS
from loader import bot


logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO
)


async def message_to_admins(message_text) -> None:
    if message_text:
        start_time = time.time()
        admins_list = ADMINS.split(", ")
        if admins_list[0]:
            for admin in range(len(admins_list)):
                await bot.send_message(admins_list[admin], message_text, parse_mode='HTML')

            logging.info("Messages to admins sent --- %s seconds ---" % (time.time() - start_time))
