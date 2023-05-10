from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

telefonlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sumsung"),
            KeyboardButton(text="Iphone")
        ],
        [
            KeyboardButton(text="Redmi")
        ]
    ],
    resize_keyboard=True
)

