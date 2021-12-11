from deadline_todo.config import BOT_API_TOKEN
from deadline_todo.db.task import TaskDatabaseService

import logging
import asyncio
from aiogram import Bot, types
from aiogram.utils import exceptions


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')

bot = Bot(token=BOT_API_TOKEN, parse_mode=types.ParseMode.HTML)


async def get_data():
    data = await TaskDatabaseService().tg_today_tasks()

    return data


async def send_message(user_id: int, text: str, disable_notification: bool = True) -> bool:
    """
    Safe telegram bot messages sender
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_message(user_id, text, disable_notification=disable_notification)
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def broadcaster() -> int:
    """
    Broadcaster
    :return: Count of messages
    """
    count = 0
    try:
        data = await get_data()
        for user_id, tasks in data.items():
            message = 'Ваши задачи на сегодня:'
            for task in tasks:
                message += f'\n\n<b>{task.get("task_name")}</b>\n' \
                           f'{task.get("task_desc") if task.get("task_desc") else "Без описания"}'

            if await send_message(user_id, message):
                count += 1
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        session = await bot.get_session()
        await session.close()
        log.info(f"{count} messages successful sent.")

    return count
