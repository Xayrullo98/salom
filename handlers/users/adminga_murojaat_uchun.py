from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states.holatlar import Murojaat
from loader import dp,bot
from keyboards.default.tasdiqlash import tasdiqlash_buttons
from keyboards.default.menu_uchun import menu_buttons
# Echo bot
@dp.message_handler(text="Adminga murojaat")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismni kiriting",reply_markup=ReplyKeyboardRemove())
    await Murojaat.ism_qabul_qilish.set()

@dp.message_handler(state=Murojaat.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"ism":matn})
    await message.answer(text="Familyani kiriting")
    await Murojaat.familya_qabul_qilish.set()

@dp.message_handler(state=Murojaat.familya_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"fam":matn})
    await message.answer(text="Yoshni kiriting")
    await Murojaat.yosh_qabul_qilish.set()

@dp.message_handler(state=Murojaat.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"yosh":matn})
    await message.answer(text="Tel kiriting")
    await Murojaat.tel_qabul_qilish.set()

@dp.message_handler(state=Murojaat.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"nomer":matn})
    await message.answer(text="Murojaat kiriting")
    await Murojaat.murojaat_qabul_qilish.set()

@dp.message_handler(state=Murojaat.murojaat_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"murojaat":matn})
    malumot = await state.get_data()
    ismi = malumot.get('ism')
    familya = malumot.get('fam')
    yosh = malumot.get('yosh')
    tel = malumot.get('nomer')
    murojaat = malumot.get('murojaat')

    textt= f"Ism : {ismi}\n" \
          f"Familya : {familya}\n" \
          f"Yosh : {yosh}\n" \
          f"Tel : {tel}\n"\
          f"Murojaat : {murojaat}\n"
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text=textt,reply_markup=tasdiqlash_buttons)
    await Murojaat.tasdiqlash_holati.set()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Bekor qilish")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="Bekor qilindi",reply_markup=menu_buttons)
    await state.finish()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Tasdiqlash")
async def bot_echo(message: types.Message,state:FSMContext):
    malumot = await state.get_data()
    ismi = malumot.get('ism')
    familya = malumot.get('fam')
    yosh = malumot.get('yosh')
    tel = malumot.get('nomer')
    murojaat = malumot.get('murojaat')

    textt = f"🙎‍♂️Ism : {ismi}\n" \
            f"🙎‍♂️Familya : {familya}\n" \
            f"Yosh : {yosh}\n" \
            f"Tel : {tel}\n" \
            f"Murojaat : {murojaat}\n"

    await bot.send_message(chat_id='5883029982',text=textt)
    await bot.send_message(chat_id=message.from_user.id,text="Adminga yuborildi",reply_markup=menu_buttons)
    await state.finish()


