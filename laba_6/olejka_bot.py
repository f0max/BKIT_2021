from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config import TOKEN
from utils import TestStates
from messages import MESSAGES
from answers import *


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await msg.reply(MESSAGES['start'])


@dp.message_handler(commands=['help'])
async def process_help_command(msg: types.Message):
    await msg.reply(MESSAGES['help'])


@dp.message_handler(state='*', commands=['setstate'])
async def process_setstate_command(msg: types.Message, state: FSMContext):
    arg = msg.get_args()
    curr_state = dp.current_state(user=msg.from_user.id)
    if not arg:
        await curr_state.reset_state()
        return await msg.reply(MESSAGES['state_reset'])

    if (not arg.isdigit()) or (not int(arg) < len(TestStates.all())):
        return await msg.reply(MESSAGES['invalid_key'].format(key=arg))

    if int(arg) != 0:
        await curr_state.set_state(TestStates.all()[int(arg)])
        return await msg.reply(MESSAGES[int(arg)])
    else:
        await curr_state.set_state(TestStates.all()[int(arg)])
        user_data = await state.get_data()
        if (user_data.get("chosen_location" == None)) or (user_data.get("chosen_backpack") == None) or (user_data.get("chosen_transport") == None):
            return await msg.reply("Заполните все данные", reply=False)
        await msg.reply(MESSAGES['camp'].format(loc=location[user_data.get("chosen_location")], 
                                            bp=backpack[user_data.get("chosen_backpack")],
                                            transp=transport[user_data.get("chosen_transport")]))


@dp.message_handler(state=TestStates.TEST_STATE_1)
async def first_test_state_choice(msg: types.Message, state: FSMContext):
    answer = msg.text
    if (not answer.isdigit()) or (not int(answer) < len(location)):
        return await msg.reply(MESSAGES['wrong_answer'], reply=False)

    await state.update_data(chosen_location=int(answer))
    await msg.reply(MESSAGES['success_answer'], reply=False)


@dp.message_handler(state=TestStates.TEST_STATE_2)
async def second_test_state_case_met(msg: types.Message, state: FSMContext):
    answer = msg.text
    if (not answer.isdigit()) or (not int(answer) < len(backpack)):
        return await msg.reply(MESSAGES['wrong_answer'], reply=False)
    
    await state.update_data(chosen_backpack=int(answer))
    await msg.reply(MESSAGES['success_answer'], reply=False)


@dp.message_handler(state=TestStates.TEST_STATE_3)
async def third_test_state_case_met(msg: types.Message, state: FSMContext):
    answer = msg.text
    if (not answer.isdigit()) or (not int(answer) < len(transport)):
        return await msg.reply(MESSAGES['wrong_answer'], reply=False)
    
    await state.update_data(chosen_transport=int(answer))
    await msg.reply(MESSAGES['success_answer'], reply=False)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)