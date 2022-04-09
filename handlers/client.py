from aiogram import Dispatcher, types


async def send_welcome(message: types.Message):
    await message.reply("Hello!")


async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(echo)
