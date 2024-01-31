import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import token
from db import open_pool

from routers import commands


async def main():
    try:
        await open_pool()
        bot = Bot(token=token)
        dp = Dispatcher()
        dp.include_router(router=commands.router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
        await open_pool()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
