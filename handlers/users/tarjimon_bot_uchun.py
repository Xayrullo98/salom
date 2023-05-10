from aiogram import types
from googletrans import Translator
from loader import dp

tarjimon = Translator()

# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):

    til = tarjimon.detect(text=message.text).lang
    if til=='uz':
        eng = tarjimon.translate(text=message.text,dest='en',src='uz').text
        await message.answer(text=eng)
