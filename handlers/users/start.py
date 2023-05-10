from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.telefonlar_uchun import telefonlar_buttons
from loader import dp,bot
from keyboards.inline.tillar_uchun import tillar_buttons
from filters import Shaxsiy
@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)


@dp.callback_query_handler(text="til1")
async def bot_start(xabar:CallbackQuery):
    await xabar.message.answer(text=f"Salom, O'zbek tilini tanladiz!",reply_markup=menu_buttons)

@dp.message_handler(text="Telefonlar")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=telefonlar_buttons)


@dp.message_handler(text="Sumsung")
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/UstozShogird/27266'
    await bot.send_photo(chat_id=user_id,photo=rasm,caption="Bu Sumsung telefoni \n"
                                                            "Narxi : 200$")

@dp.message_handler(commands="boshlash")
async def bot_start(message: types.Message):
    await message.answer(f"Salom,botga hush kelibsiz!")