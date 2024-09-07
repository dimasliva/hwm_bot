import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from app.handlers import router
from dotenv import load_dotenv
import os


async def main():
    load_dotenv()
    # session = AiohttpSession(proxy="http://proxy.server:3128")

    # bot = Bot(token=PROD_TOKEN, session=session)
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    print('Бот запущен')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
