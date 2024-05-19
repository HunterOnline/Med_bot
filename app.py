import json

from utils.db_api.quick_commands import add_question
from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()

    print("Готово")
    await on_startup_notify(dp)
    await set_default_commands(dp)
    # with open("data.json", "r") as json_file:
    #     # Прочитати вміст файлу
    #     json_content = json_file.read()
    #     # Десеріалізувати JSON-рядок у Python-об'єкт
    #     data = json.loads(json_content)
    #     # Ітерувати по кожному елементу
    #     for elm in data:
    #         print(elm)
    #         question = elm['question']
    #         options = json.dumps(elm['options'])
    #         points = int(elm['points'])
    #         await add_question(question=question, options=options, points=points)




if __name__ == '__main__':
    from aiogram import executor

    from handlers import dp

    executor.start_polling(dp,  on_startup=on_startup)
