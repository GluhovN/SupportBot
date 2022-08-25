from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

def mainkey():
    send_request = KeyboardButton('Задать вопрос')

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(send_request)
    return kb

def back():
    back = KeyboardButton('Назад')
    kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_back.add(back)
    return kb_back

def ans():
    ans = InlineKeyboardButton('Ответить', callback_data='ans')
    kb_ans = InlineKeyboardMarkup().add(ans)   
    return kb_ans