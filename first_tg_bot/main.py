from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = ''

bot = Bot(TOKEN_API)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer('Hello, world!')


@dispatcher.message_handler(commands=['photo'])
async def command_photo(message: types.Message):
    await bot.send_photo(photo='https://cataas.com/cat/says/hello%20world!')

@dispatcher.message_handler()
async def msg(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dispatcher)
