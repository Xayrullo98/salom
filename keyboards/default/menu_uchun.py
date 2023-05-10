from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefonlar"),
            KeyboardButton(text="Kompyuterlar")
        ],
        [
            KeyboardButton(text="Maishiy texnika"),
            KeyboardButton(text="Aksesuarlar")
        ],
        [
            KeyboardButton(text="Adminga murojaat"),

        ]
    ],
    resize_keyboard=True
)
