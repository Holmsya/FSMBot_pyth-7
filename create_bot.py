from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage    # позволяет хранить данные в ОЗУ

API_TOKEN = ''

storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)
