from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "СТАРТ"),
        types.BotCommand("help", "Допомога"),
        types.BotCommand("arr_user", "Користувачі(Admin)"),
        types.BotCommand("count_user", "Кількість користувачів (Admin)"),

    ])
