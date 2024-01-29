import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import token
from db import open_pool

from handlers import basic


logging.basicConfig(level=logging.INFO)


async def main():
    try:
        await open_pool()
        bot = Bot(token=token)
        dp = Dispatcher()
        dp.include_router(basic.router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, polling_timeout=11)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """
    функция ниже set_event_loop_policy для решения проблем с windows!!! - для linux и unix не актуальна
    если что коментируй ее просто
    """
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
