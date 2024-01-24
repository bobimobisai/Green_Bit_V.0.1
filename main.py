import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command

from handlers import basic
from config import *

logging.basicConfig(level=logging.INFO)          #Логирование
async def main():
    bot = Bot(token=token)          #Указываем токен бота
    dp = Dispatcher()               #Диспетчер
    dp.include_router(basic.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())

