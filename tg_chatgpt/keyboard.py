from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_help = KeyboardButton(text='/help')
button_photo = KeyboardButton(text='/photo')
button_disable = KeyboardButton(text='/disable')

keyboard.add(button_help)
keyboard.add(button_photo)
keyboard.add(button_disable)