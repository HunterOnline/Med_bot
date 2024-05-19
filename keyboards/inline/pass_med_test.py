from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

pass_test_callback = CallbackData("start_test_mess", "action")

pass_test = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text="Почати", callback_data=pass_test_callback.new(action='start_test')),
         InlineKeyboardButton(text="Вийти", callback_data=pass_test_callback.new(action='cancel'))
         ]

    ]
)

options_keyboard_callback = CallbackData("options_test_mess", "action")


def options_keyboard(ls: list):
    options_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=chr(ord('a') + button - 1),
                              callback_data=options_keyboard_callback.new(action=chr(ord('a') + button - 1))) for button in
         range(1, len(ls)+1)]
    ])

    return options_keyboard
