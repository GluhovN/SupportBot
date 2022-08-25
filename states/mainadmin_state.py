from aiogram.dispatcher.filters.state import State, StatesGroup

class main_ad(StatesGroup):
    answer = State()
    new_admin = State()
    delete_admin = State()
    new_intro = State()
