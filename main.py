import logging
from aiogram import executor
from create_bot import dp
from handlers import client, admin


logging.basicConfig(level=logging.INFO)


admin.register_handlers(dp)
client.register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
