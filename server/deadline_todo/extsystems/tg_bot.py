from deadline_todo.config import BOT_API_TOKEN

import asyncio
from aiogram import Bot, Dispatcher
from aiogram import types


bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        'Привет! Я бот, который поможет тебе не забывать дела запланированные на текущий день!\n'
        '  • Чтобы подписаться на рассылку, добавь свой Telegram UserID в профиль на нашем сайте DeadlineToDo!\n'
        '  • Для того чтобы узнать свой Telegram UserID можешь воспользоваться командой /id'
    )


@dp.message_handler(commands=['id'])
async def process_start_command(message: types.Message):
    await message.reply(
        f"""Твой уникальный идентификатор {message.from_user.id}!"""
    )


async def polling():
    try:
        await dp.start_polling()
    except asyncio.CancelledError:
        pass
    finally:
        dp.stop_polling()
        await dp.wait_closed()

        session = await dp.bot.get_session()
        await session.close()


async def bot_start(app):
    app['telegram_bot'] = asyncio.create_task(polling())


async def bot_shutdown(app):
    app['telegram_bot'].cancel()
    await app['telegram_bot']
