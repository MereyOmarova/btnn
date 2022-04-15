from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fly me to the moon"),
            KeyboardButton(text="All of me"),
        ],
        [
            KeyboardButton(text="Wonderful"),
            KeyboardButton(text="Umbrella"),
        ],
        [
            KeyboardButton(text="Heat Weaves"),
            KeyboardButton(text="Dandelions"),
            KeyboardButton(text="Perfect"),
        ],
    ],
    resize_keyboard=True
)