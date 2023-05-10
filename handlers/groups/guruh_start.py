from aiogram import types
from aiogram.types import ContentTypes

from loader import dp
from filters import Guruh

# Echo bot
@dp.message_handler(Guruh(),commands="start")
async def bot_echo(message: types.Message):
    user = message.from_user.full_name
    await message.answer(text=f"guruhga hush kelibsiz {user}")

@dp.message_handler(Guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    user = message.new_chat_members[0].full_name
    await message.answer(text=f"Guruhga hush kelibsiz {user}")

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    user = message.left_chat_member.full_name
    await message.answer(text=f"Guruhni tark etdi {user}")

# Echo bot
@dp.message_handler(Guruh(),text="Salom")
async def bot_echo(message: types.Message):
    user = message.from_user.full_name
    await message.answer(text=f"Assalomu alaykum ☺️{user}")