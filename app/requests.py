import requests
from app.variables import user
from app.functions import getRegionByName
from app.jobs import getJob, getSuccessJob
from app.regionFuncs import getRegionName
from bs4 import BeautifulSoup
import random
from decimal import Decimal, getcontext
import time


async def getCurrentRegion():
    params = {
        'id': f'{user.id}'
    }
    res = requests.get('https://www.heroeswm.ru/pl_info.php',
                       params=params, cookies=user.cookies, headers=user.headers)
    soup = BeautifulSoup(res.text, 'lxml')
    tds = soup.find_all('td', colspan="2")
    links = soup.find_all('a', href=True)
    region_name = ""
    for td in tds:
        links = td.find_all("a", href=True)
        for link in links:
            if link["href"].split('?')[0] == "map.php":
                region_name = link.text
                user.region = getRegionByName(region_name)
                break

    return region_name





        
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
