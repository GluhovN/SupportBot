from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

def main_a():
    answer = KeyboardButton('Начать работу')
    new_admin = KeyboardButton('Назначить нового админа')
    check_admins = KeyboardButton('Список администраторов')
    delete_admin = KeyboardButton('Удалить админа')
    change_intro = KeyboardButton('Изменить вступительный текст')
    kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_main.add(answer, new_admin, check_admins)
    kb_main.add(delete_admin)
    kb_main.add(change_intro)
    return kb_main

def main_a_back():
    back = KeyboardButton('Назад')
    back_main = ReplyKeyboardMarkup(resize_keyboard=True)
    back_main.add(back)
    return back_main

def next_user():
    next_user = InlineKeyboardButton('Следующий вопрос', callback_data='nxt')
    kb_nxt = InlineKeyboardMarkup().add(next_user)   
    return kb_nxt
