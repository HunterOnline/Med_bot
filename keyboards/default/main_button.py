from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Розрахунки при опіках 🔥")],
        [KeyboardButton(text="Розрахунки препаратів 💉")],
        [KeyboardButton(text="Шпаргалка 📋")],


    ], resize_keyboard=True, ) # [KeyboardButton(text="Тренуватися🏋️‍♀️")]
