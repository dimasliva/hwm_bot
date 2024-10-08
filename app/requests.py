import requests
from app.variables import user

from app.functions import getRegionByName
from app.jobs import getJob, doJob
from app.regionFuncs import getRegionName
from bs4 import BeautifulSoup
import random
from decimal import Decimal, getcontext
import time
from datetime import datetime, timedelta
import asyncio


async def startJob():
    #Добыча 'mn',
    #Обработка 'fc',
    #Производство 'sh',
    print("startJob")

    status = await doJob('sh')
    print('startJob status', status)   
    if status == None:
        return 200  
        
async def toJob():
    status = await startJob()
    if status == None:
        delay = 1 * 60 * 60 + 10  # 1 час = 3600 секунд, 10 секунд = 10
        await asyncio.sleep(delay)
        await toJob()

def getJobTimer():
    # Получаем текущее время
    now = datetime.now()

    # Создаем временной интервал для добавления (1 час и 10 секунд)
    delta = timedelta(hours=1, seconds=10)

    # Добавляем интервал к текущему времени
    new_time = now + delta

    # Форматируем полученное время в HH:MM:SS
    formatted_time = new_time.strftime('%H:%M:%S')
    return formatted_time

async def moveToRegion(region_to_move, regions_for_move):
    for region in regions_for_move:
        if getRegionName(user.region) == region_to_move:
            break
        getcontext().prec = 20

        # Generate a random float and convert it to Decimal for higher precision
        random_float = Decimal(random.uniform(0.0, 1.0)).quantize(
            Decimal('0.00000000000000000000'))
        params = {
            'id': region["id"],
            'rand': random_float,
        }
        res = requests.get('https://www.heroeswm.ru/move_sector.php',
                           params=params, cookies=user.cookies, headers=user.headers)
        if res.status_code == 200:
            user.region = region
            time.sleep(40)
