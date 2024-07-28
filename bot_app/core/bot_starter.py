import logging

from aiogram import Bot, Dispatcher

from core.config import BOT_TOKEN
from routers import router as main_router

bot = Bot(token=BOT_TOKEN)


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)
