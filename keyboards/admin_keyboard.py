from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

def main_kb():
    answer = KeyboardButton('Начать работу')
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(answer)
    return kb

def work():
    back = KeyboardButton('Назад')
    kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_back.add(back)
    return kb_back

def next_user1():
    next_user1 = InlineKeyboardButton('Следующий вопрос', callback_data='nxt1')
    kb_nxt1 = InlineKeyboardMarkup().add(next_user1)   
    return kb_nxt1

