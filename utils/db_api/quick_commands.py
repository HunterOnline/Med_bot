import json

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.data_for_test import Data_Test
from utils.db_api.schemas.user import User


async def add_user(id: int, name: str, ):
    try:
        user = User(id=id, name=name,)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    # Перетворюємо список користувачів на список словників
    user_list = [user.to_dict() for user in users]

    return user_list


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_email(id, email):
    user = await User.get(id)
    await user.update(email=email).apply()


"""Data_Test Table DB"""

async def add_question(question:str, options:list, points:int):

    try:
        question = Data_Test(question=question, options=options, points=points)
        await question.create()

    except UniqueViolationError:
        pass


async def select_all_question_options():
    question = await Data_Test.query.gino.all()
    # Перетворюємо список користувачів на список словників
    question_list = [qsn.to_dict() for qsn in question]
    question_list =[{'question':qsn['question'],
                     'options':json.loads(qsn['options']),
                     'points':qsn['points']
                    }for qsn in question_list]

    return question_list
