'''
TODO: Создать меню для tg-бота, обеспечить навигацию по меню (при нажатии кнопок будут открываться нужные ReplyKeyboardMarkup
Реализовать функицю, которая будет при нажатии кнопки считывать текст и его же выводить в консоль принтом
* Залочить (просто его не воспринимаешь и никак не обрабатываешь) обработку текста на некоторое время
* Добавить кнопку для генерации фотографии по запросу, при нажатии активировать считывание запроса
'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

import time

from config import TOKEN_API, HELP_INFO
from keyboard import *

bot = Bot(TOKEN_API)
dispatcher = Dispatcher(bot)


def on_startup():
    print('Bot has started')


@dispatcher.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Hello!')


@dispatcher.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await message.answer(text=HELP_INFO,
                         reply_markup=keyboard)


@dispatcher.message_handler(commands=['disable'])
async def start_command(message: types.Message):
    await message.answer(text='Keyboard is disabled',
                         reply_markup=ReplyKeyboardRemove())


@dispatcher.message_handler(commands=['photo'])
async def start_command(message: types.Message):
    url = 'https://cataas.com/cat/says/Hi!'
    unique_url = f"{url}?timestamp={int(time.time())}"

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=unique_url,
                         reply_markup=keyboard)


def main():
    executor.start_polling(dispatcher,
                           skip_updates=True,
                           on_startup=on_startup())


if __name__ == '__main__':
    main()
