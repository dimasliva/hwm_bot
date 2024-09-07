from app.variables import user
import re
import ast
import requests
from bs4 import BeautifulSoup

async def homeRequest(params=False):
    if params == False:
        response = requests.get('https://www.heroeswm.ru/home.php', cookies=user.cookies, headers=user.headers)
    else:
        response = requests.get('https://www.heroeswm.ru/home.php', params=params, cookies=user.cookies, headers=user.headers)
    return response
  
    
def setUser(text):
    # Регулярные выражения для поиска `cookies` и `headers`
    cookies_pattern = r"cookies\s*=\s*({.*?})"
    headers_pattern = r"headers\s*=\s*({.*?})"

    # Находим соответствия
    cookies_match = re.search(cookies_pattern, text, re.DOTALL)
    headers_match = re.search(headers_pattern, text, re.DOTALL)

    # Парсим найденные строки в словари
    if cookies_match:
        cookies = ast.literal_eval(cookies_match.group(1))
    else:
        cookies = {}

    if headers_match:
        headers = ast.literal_eval(headers_match.group(1))
    else:
        headers = {}

    if headers != {} and cookies != {}:
        user.headers = headers
        user.cookies = cookies
    else:
        return 500 
        # Выводим результаты
    
        
async def skipDay(params):
    response = await homeRequest(params)
    if response.status_code:
        return 200
    else:
        return 500
    
async def getHomeInfo():
    response = requests.get('https://www.heroeswm.ru/home.php?info', cookies=user.cookies, headers=user.headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        span_element = soup.find('span', string='Ознакомился')
        if span_element:
            params = {
                'skipn': '1',
            }
            resp = await homeRequest(params)
            return resp
        else:
            return 500
            
async def learnRules(response):
    soup = BeautifulSoup(response.text, 'lxml')
    span_element = soup.find('span', string='Ознакомился')
    if span_element:
        params = {
            'skipn_day': '1',
        }
        status = await skipDay(params)
        if status == 200: 
            resp = await getHomeInfo()
            return resp
        else:
            return 500
    else: 
        return response
    
async def getUser():
    res = await homeRequest()
    if res.status_code == 200:
        resp = await learnRules(res)
        if resp == 500:
            print('learnRules not working')
            return 500
        else:
            soup = BeautifulSoup(resp.text, 'lxml')
            a = soup.find_all("a", class_="pi", href=True)[0]
            user.href = a['href']
            user.id = a['href'].split('=')[1]
            return 200
    else:
        return 500