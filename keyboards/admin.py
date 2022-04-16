from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_upload = KeyboardButton('Upload')   # создание объекта кнопки
button_contact = KeyboardButton('Send your contact', request_contact=True)
button_location = KeyboardButton('Send your location', request_location=True)
button_remove_kb = KeyboardButton('Remove keyboard')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)     # создание объектка клавиатуры
# kb_main.add(button_upload).add(button_test1).insert(button_test2)  # сборка клавиатуры
kb_main.add(button_upload).row(button_contact, button_location).add(button_remove_kb)

button_cancel = KeyboardButton('cancel')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)
