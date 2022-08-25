from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from sql_dump import *
import json
from json_dump import *
from peewee import *
from keyboards.user_keyboard import *
from keyboards.admin_keyboard import *
from keyboards.mainadmin_keyboard import *
from states.admin_state import *
from states.mainadmin_state import *
from states.user_state import *
from art import tprint


with open("config.txt") as file:
    for i in file:
        API_TOKEN = i
        break

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    with open('admins.json') as json_file:
        data = json.load(json_file)
    if message.from_user.id in data['main_admin']:
        await message.answer("Добро пожаловать!", reply_markup=main_a())
    elif message.from_user.id in data['admins']:
        await message.answer("Добро пожаловать!", reply_markup=main_kb())
    else:
        await message.answer(text=get_txt(), reply_markup=mainkey())

@dp.message_handler()
async def qvs(message: types.Message):
    with open('admins.json') as json_file:
        data = json.load(json_file)
    if message.from_user.id in data['main_admin']:
        if message.text.lower() == 'начать работу':
            if check_base() is not False:
                await message.answer('Пришел вопрос:\n'+str(check_base()[2]))
                work_in_porcess(message.from_user.id, get_number(), check_base()[1])
                change_number()
                delete_from_base()
                await main_ad.answer.set()
            else:
                await message.answer('На данный момент вопросов нету')
        elif message.text.lower() == 'назначить нового админа':
            await bot.send_message(message.from_user.id,
             'Введите telegram id нового админа\nПолучить telegram id можно с помощью: \n@get_id_tg_bot',
              reply_markup=main_a_back())
            await main_ad.new_admin.set()
        elif message.text.lower() == 'список администраторов':
            await message.answer(text=get_admins(), reply_markup=main_a())
        elif message.text.lower() == 'удалить админа':
            await message.answer(text='Введите telegram id админа, которого хотите удалить'
            '\nПолучить telegram id можно с помощью:'
            ' \n@get_id_tg_bot', reply_markup=main_a_back())
            await main_ad.delete_admin.set()
        elif message.text.lower() == 'изменить вступительный текст':
            await message.answer(f'Текущий текст:"{get_txt()}". Введите новый текст:', reply_markup=main_a_back())
            await main_ad.new_intro.set()
    elif message.from_user.id in data['admins']:
        if message.text.lower() == 'начать работу':
            if check_base() is not False:
                await message.answer('Пришел вопрос:\n'+str(check_base()[2]))
                work_in_porcess(message.from_user.id, get_number(), check_base()[1])
                change_number()
                delete_from_base()
                await main.answer.set()
            else:
                await message.answer('На данный момент вопросов нету')
    else:
        if message.text.lower() == 'задать вопрос':
            if checkusers(message.from_user.id) == False:
                await bot.send_message(message.from_user.id, 'Пожалуйста отправьте вопрос который хотите задать:', reply_markup=back())
                await q.qvs.set()
            else:
                await message.answer('Вы уже задали вопрос. Дождитесь ответа.')
        elif message.text.lower() == 'Назначить нового админа':
            await message.answer('Отказано в доступе')
        elif message.text.lower() == 'Список администраторов':
            await message.answer('Отказано в доступе')

@dp.message_handler(state=q.qvs)
async def send(message: types.Message, state: FSMContext):
    if message.text.lower() == 'назад':
        await state.finish()
        await message.answer("Вы отменили вопрос", reply_markup=mainkey())
    elif message.text.lower()[0] == '/':
        await state.finish()
        await message.answer("hi", reply_markup=mainkey())
    else:
        change_number()
        await state.finish()
        send_to_db(get_number(), message.from_user.id, message.text)
        await bot.send_message(message.from_user.id, 'Ваше сообщение было успешно доставлено администратором, ожидайте вам скоро ответят!', reply_markup=mainkey())

@dp.message_handler(state=main_ad.new_admin)
async def send(message: types.Message, state: FSMContext):
    if message.text.lower() == 'назад':
        await state.finish()
        await message.answer("Главное меню", reply_markup=main_a())
    elif message.text.lower()[0] == '/':
        await state.finish()
        await message.answer("Главное меню", reply_markup=main_a())
    else:
        await state.finish()
        if new_admin(int(message.text)) == False:
            await bot.send_message(message.from_user.id, 'Админ уже был добавлен',
         reply_markup=main_a())
        else:
            new_admin(int(message.text))
            await bot.send_message(message.from_user.id, 'Вы успешно добавили нового админа',
         reply_markup=main_a())


@dp.message_handler(state=main_ad.delete_admin)
async def send(message: types.Message, state: FSMContext):
    if message.text.lower() == 'назад':
        await state.finish()
        await message.answer("Главное меню", reply_markup=main_a())
    elif message.text.lower()[0] == '/':
        await state.finish()
        await message.answer("Главное меню", reply_markup=main_a())
    else:
        await state.finish()
        if delete_admin(int(message.text)) == False:
            await bot.send_message(message.from_user.id, 'Админа нет в списке',
         reply_markup=main_a())
        else:
            delete_admin(int(message.text))
            await bot.send_message(message.from_user.id, 'Вы успешно удалили админа',
         reply_markup=main_a())


@dp.message_handler(state=main_ad.new_intro)
async def send(message: types.Message, state: FSMContext):
    if message.text.lower() == 'назад':
        await state.finish()
        await message.answer("Главное меню", reply_markup=main_a())
    elif message.text.lower()[0] == '/':
        await state.finish()
        await message.answer("Главное меню", reply_markup=main_a())
    else:
        await state.finish()
        change_txt(message.text)
        await message.answer('Текст успешно изменен.', reply_markup=main_a())


@dp.message_handler(state=main_ad.answer)
async def send(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        await bot.send_message(qvs_id(str(message.from_user.id)), 'Ответ от Администрации:\n'+message.text, reply_markup=ans())
    except:
        pass
    await bot.send_message(message.from_user.id, 'Вы ответили на вопрос!', reply_markup=next_user())


@dp.message_handler(state=main.answer)
async def send(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        await bot.send_message(qvs_id(str(message.from_user.id)), 'Ответ от Администрации:\n'+message.text, reply_markup=ans())
    except:
        pass
    await bot.send_message(message.from_user.id, 'Вы ответили на вопрос', reply_markup=next_user1())


@dp.callback_query_handler()
async def process_callback_kb1btn1(call: types.CallbackQuery):
    with open('admins.json') as json_file:
        data = json.load(json_file)
    if call.data == 'ans':
        if call.message.chat.id in data['main_admin']:
            await call.answer('Сам с собой разговориваешь?')
        elif call.message.chat.id in data['admins']:
            await call.answer('Сам с собой разговориваешь?')
        else:
            if checkusers(call.from_user.id) == False:
                await bot.send_message(call.message.chat.id, 'Пожалуйста отправьте вопрос который хотите задать:', reply_markup=back())
                await q.qvs.set()
            else:
                await call.answer('Вы уже задали вопрос. Дождитесь ответа')
    elif call.data == 'nxt':
        if call.message.chat.id in data['main_admin']:
            if check_base() is not False:
                await bot.send_message(call.message.chat.id, 'Пришел вопрос:\n'+str(check_base()[2]))
                work_in_porcess(call.message.chat.id, get_number(), check_base()[1])
                change_number()
                delete_from_base()
                await main_ad.answer.set()
            else:
                await call.answer('На данный момент вопросов нету')
    elif call.data == 'nxt1':
        if call.message.chat.id in data['admins']:
            if check_base() is not False:
                await bot.send_message(call.message.chat.id, 'Пришел вопрос:\n'+str(check_base()[2]))
                work_in_porcess(call.message.chat.id, get_number(), check_base()[1])
                change_number()
                delete_from_base()
                await main_ad.answer.set()
            else:
                await call.answer('На данный момент вопросов нету')

if __name__ == '__main__':
    print('\n'*2)
    tprint('BOT>>START>>WORKING')
    executor.start_polling(dp, skip_updates=True)