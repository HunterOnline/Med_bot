import asyncio
import logging
import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.inline.pass_med_test import pass_test, pass_test_callback, options_keyboard, options_keyboard_callback
from loader import dp, bot
from states.fix_state import PassTestMessage
from utils.db_api.quick_commands import select_all_question_options
from aiogram.dispatcher.filters import Command
from utils.misc import rate_limit


@rate_limit(5, "Тренуватися🏋️‍♀️")
@dp.message_handler(Command("test"))
async def pass_med_test(message: types.Message, state: FSMContext):
    await PassTestMessage.ListTest.set()
    test_list = await select_all_question_options()
    user_points = 0
    await state.update_data(test_list=test_list, user_points=user_points)
    await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)
    # Чекаємо 1 секунди з використанням асинхронності
    await asyncio.sleep(0.5)
    await message.answer(f'Пропонуємо Вам перевірити свої знання (рівень CLS), корткий тест 30 запитань',
                         reply_markup=pass_test)
    logging.info(message.from_user.full_name + " -> pressed [Тренуватися🏋️‍♀]")


@dp.callback_query_handler(pass_test_callback.filter(action='cancel'))
async def cancel_state(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()


@dp.callback_query_handler(options_keyboard_callback.filter(), state=PassTestMessage.ListTest)
@dp.callback_query_handler(pass_test_callback.filter(action='start_test'), state=PassTestMessage.ListTest)
async def start_test(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    call_answer = call.data.split(':')[1]

    async with state.proxy() as data:

        test_list = data.get('test_list')
        answer = data.get('answer')
        user_points = data.get('user_points')
        answer_points = data.get('answer_points')

        if call_answer == answer:
            user_points += int(answer_points)

    try:
        aleatorius_index = random.randint(0, len(test_list) - 1)
        aleatorius_elementum = test_list.pop(aleatorius_index)
        answer_points = aleatorius_elementum['points']

        options_list = [chr(ord('a') + aleatorius_elementum['options'].index(i)) + ') ' + i for i in
                        aleatorius_elementum['options']]
        answer = [i[0] for i in options_list if '*' in i][0]

        options_list = [i.rstrip('*') for i in options_list]

        await state.update_data(test_list=test_list, answer=answer, answer_points=answer_points,
                                user_points=user_points)

        options = '\n\n'.join(options_list)
        await call.message.answer(f"{aleatorius_elementum['question']}\n\n{options}",
                                  reply_markup=options_keyboard(aleatorius_elementum['options']))
        logging.info(
            call.from_user.full_name + f"\nбал за запитання:{aleatorius_elementum['points']}\nНабрані бали:{user_points}")

    except ValueError:
        await state.finish()
        await call.message.answer(f"ВАШ РЕЗУЛЬТАТ: {user_points} з 40 можлих \n\nПРОХІДНИЙ бал: 34")
        await dp.bot.send_message(chat_id=ADMINS, text=f'{call.from_user.full_name}\nНабраних балів:{user_points} ', )
