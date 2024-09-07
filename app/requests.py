import requests
from app.variables import user

from app.functions import getRegionByName
from app.jobs import getJob, getSuccessJob
from app.regionFuncs import getRegionName
from bs4 import BeautifulSoup
import random
from decimal import Decimal, getcontext
import time




        
async def toJob():
    #Добыча 'mn',
    #Обработка 'fc',
    #Производство 'sh',

    res = await getSuccessJob('sh')
    print('res', res)     



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
