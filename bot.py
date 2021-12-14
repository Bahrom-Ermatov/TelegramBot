import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import TOKEN, PROXY
from fsm import States, PizzaOrder
from transitions import Machine

# Объект бота
bot = Bot(token=TOKEN, proxy=PROXY)

# Диспетчер для бота
dp = Dispatcher(bot)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

states = States()
users = {}

def get_answer_msg(message, pizza_size):
    if message in states.newOrder:
        return "Какую вы хотите пиццу? Большую или маленькую?"
    elif message in states.start:
        return "Какую вы хотите пиццу? Большую или маленькую?"
    elif message in states.pizzaSizes:
        return "Как вы будете платить?"
    elif message in states.payTypes:
        return "Вы хотите " + pizza_size + " пиццу, оплата - " + message + "?"
    elif message in states.orderStateYes:
        return "Спасибо за заказ"
    elif message in states.orderStateNo:
        return "Ок, заказ отменен"


# Хэндлер на Новый заказ
@dp.message_handler(commands=states.start)
@dp.message_handler(Text(equals=states.newOrder))
async def select_pizza_size(message: types.Message):
    users[message['from']['id']] = PizzaOrder(message['from']['id'])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = states.pizzaSizes
    keyboard.add(*buttons)
    resp_message=get_answer_msg(message.text, None)
    await message.answer(resp_message, reply_markup=keyboard)


# Хэндлер на выбор размера пиццы
@dp.message_handler(Text(equals=states.pizzaSizes))
async def select_pay_type(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    users[message['from']['id']].pizzaSize=message.text
    buttons = states.payTypes
    keyboard.add(*buttons)
    resp_message=get_answer_msg(message.text, None)
    await message.answer(resp_message, reply_markup=keyboard)

# Хэндлер на выбор способа оплаты
@dp.message_handler(Text(equals=states.payTypes))
async def order_confirm(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = states.orderStates
    keyboard.add(*buttons)
    users[message['from']['id']].payType=message.text
    resp_message=get_answer_msg(message.text, users[message['from']['id']].pizzaSize)
    await message.answer(resp_message, reply_markup=keyboard)


# Хэндлер на подтверждение заказа
@dp.message_handler(Text(equals=states.orderStateYes))
async def select_yes(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = states.newOrder
    keyboard.add(*buttons)
    resp_message=get_answer_msg(message.text, None)
    await message.answer(resp_message, reply_markup=keyboard)

# Хэндлер на отмену заказа
@dp.message_handler(Text(equals=states.orderStateNo))
async def select_no(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = states.newOrder
    keyboard.add(*buttons)
    resp_message=get_answer_msg(message.text, None)
    await message.answer(resp_message, reply_markup=keyboard)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)









