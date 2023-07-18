from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API, HELP_INFO

# Для клавиатуры нам понадобится объект, который будет отвечать за клавиатуру
# Также понадобится объект, который отвечает за кнопку
# Понадобится функция, которая будет вызывать создание клавиатуры при исполнении какой-то команды


bot = Bot(TOKEN_API)
dispatcher = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True)  # resize_keyboard - будет отвечать за изменение размеров клавы, чтобы она была удобна для отображения
button_help = KeyboardButton('/help')
button_start = KeyboardButton('/start')
button_photo = KeyboardButton('/photo')
button_delete = KeyboardButton('/delete')

keyboard.add(button_help)
keyboard.add(button_start)
keyboard.add(button_photo)
keyboard.add(button_delete)


@dispatcher.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text='Hello, world!')


@dispatcher.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer(text=HELP_INFO,
                         reply_markup=keyboard)

    await message.delete()

@dispatcher.message_handler(commands=['delete'])
async def command_start(message: types.Message):
    await message.answer(text='Hello, world!',
                         reply_markup=ReplyKeyboardRemove())

    await message.delete()

@dispatcher.message_handler(commands=['photo'])
async def command_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://cataas.com/cat/says/hello%20world!')  # Обязтельно указывать с расширением файла

    await message.delete()

@dispatcher.message_handler()
async def msg(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
