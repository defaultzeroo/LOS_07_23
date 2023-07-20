'''
TODO: Создать меню для tg-бота, обеспечить навигацию по меню (при нажатии кнопок будут открываться нужные ReplyKeyboardMarkup
Реализовать функицю, которая будет при нажатии кнопки считывать текст и его же выводить в консоль принтом
* Залочить (просто его не воспринимаешь и никак не обрабатываешь) обработку текста на некоторое время
* Добавить кнопку для генерации фотографии по запросу, при нажатии активировать считывание запроса
'''

import logging
logging.basicConfig(level=logging.DEBUG)

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery

import time

from config import TOKEN_API, HELP_INFO, likes_number, dislikes_number
from keyboard import *

bot = Bot(TOKEN_API)
dispatcher = Dispatcher(bot)


def on_startup():
    print('Bot has started')


@dispatcher.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Hello!',
                         reply_markup=keyboard_menu)


@dispatcher.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await message.answer(text=HELP_INFO,
                         reply_markup=keyboard_menu)


@dispatcher.message_handler(commands=['disable'])
async def start_command(message: types.Message):
    await message.answer(text='Keyboard is disabled',
                         reply_markup=ReplyKeyboardRemove())


@dispatcher.message_handler(commands=['photo'])
async def start_command(message: types.Message):
    keyboard_likes = InlineKeyboardMarkup(row_width=2)
    button_like = InlineKeyboardButton(text='❤️',
                                       callback_data='like')  # Обязательный параметр - url, callback_data
    button_dislike = InlineKeyboardButton(text='💩',
                                          callback_data='dislike')

    keyboard_likes.add(button_like)
    keyboard_likes.insert(button_dislike)

    url = 'https://cataas.com/cat/says/Hi!'
    unique_url = f"{url}?timestamp={int(time.time())}"

    await message.answer_photo(photo=unique_url,
                               reply_markup=keyboard_menu)

    await message.answer(text='Оцените фото',
                         reply_markup=keyboard_likes)


@dispatcher.callback_query_handler()
async def count_likes(callback: types.CallbackQuery):
    global likes_number, dislikes_number

    print(callback.message)

    if callback.data == 'like':
        likes_number += 1

    if callback.data == 'dislike':
        dislikes_number += 1


@dispatcher.message_handler(commands=['likes'])
async def start_command(message: types.Message):
    await message.answer(text=f'Likes:{likes_number}, Dislikes:{dislikes_number}',
                         reply_markup=keyboard_menu)

def main():
    executor.start_polling(dispatcher,
                           skip_updates=True,
                           on_startup=on_startup())


if __name__ == '__main__':
    main()
