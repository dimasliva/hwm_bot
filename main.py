from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from app.handlers import router
from app.user import getUser
from app.variables import user
from app.database import db_start
from dotenv import load_dotenv
import os
import asyncio


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    print('Бот запущен')
    status = db_start(user)
    if status == 200:
        status_user = await getUser()
        if status_user == 500:
            print("user not authorization")
    else:
        print("user not authorization")

    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
