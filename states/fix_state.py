from aiogram.dispatcher.filters.state import StatesGroup, State


class FixMessage(StatesGroup):
    EnterBurns = State()
    EnterWeight = State()


class CalcMessage(StatesGroup):
    EnterPercent = State()
    EnterWight = State()


class PassTestMessage(StatesGroup):
    ListTest = State()
    UserPoints = State()
