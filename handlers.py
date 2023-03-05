import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from sql_db import BotDB

# инициализируем бота
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализация класса с подключениями к БД
db = BotDB('notify_livescore.db')


# Команда активации подписки
@dp.message_handler(commands=["subscribe"])
async def subscribe(message: types.Message):
    if not db.user_exists(message.from_user.id):
        # если юзер новый и его нет в бд, добавляем его
        db.add_user(message.from_user.id)
    else:
        # если он уже есть, то обновляем ему статус
        db.update_subcription(message.from_user.id, True)
    await message.answer("Замечательно! Вы успешно подписаны на рассылку")
    # await message.bot.send_message(message.from_user.id, "Добро пожаловать! ЙОУ")


# Команда отписки
@dp.message_handler(commands=["unsubscribe"])
async def unsubscribe(message: types.Message):
    if not db.user_exists(message.from_user.id):
        # если юзер новый и его нет в бд, добавляем его с неактивной подпиской
        db.add_user(message.from_user.id, False)
        await message.answer("Вы отписаны, для подписки используй команду subscribe")
    else:
        # если он уже есть, то отписываем его
        db.update_subcription(message.from_user.id, False)
        await message.answer("Вы отписаны, для подписки используй команду subscribe")


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
