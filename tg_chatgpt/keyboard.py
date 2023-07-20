from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True)
button_help = KeyboardButton(text='/help')
button_photo = KeyboardButton(text='/photo')
button_disable = KeyboardButton(text='/disable')
button_likes = KeyboardButton(text='/likes')

keyboard_menu.add(button_help)
keyboard_menu.add(button_photo)
keyboard_menu.add(button_disable)
keyboard_menu.add(button_likes)

keyboard_photo = ReplyKeyboardMarkup(resize_keyboard=True)
button_photo = KeyboardButton(text='/photo')
button_back = KeyboardButton(text='/back')
