from bs4 import BeautifulSoup
from app.variables import user

from PIL import Image
from io import BytesIO
import pytesseract
import threading
import requests
import random

async def jobsRequests(work_type):
    integer_part = random.randint(0, 999999)
    fractional_part = random.randint(0, 9999999999)
    formatted_number = f"{integer_part:06}.{fractional_part:010}"
    
    #Добыча 'mn',
    #Обработка 'fc',
    #Производство 'sh',
    params = {
        'cx': user.region["coordinates"]["cx"],
        'cy': user.region["coordinates"]["cy"],
        'st': work_type,
        'action': 'get_objects',
        'js_output': '1',
        'rand': formatted_number,
    }
    
    response = requests.get('https://www.heroeswm.ru/map.php',
                            params=params, cookies=user.cookies, headers=user.headers)
    
    if response.status_code == 200:
        return response.text
    
            
async def jobDo(job_id):
    data = {
        'x': user.region["coordinates"]["cx"],
        'y': user.region["coordinates"]["cy"],
        'id': job_id,
        'id2': job_id,
        'idr': 'c1e4e918dcd3407b25713e65aa63ee0b',
        'num': '0',
        'work_code_data_element': '0',
        'id3': 'ba326e9c5810a7ed90141a7998ae8904',
    }
    response = requests.post('https://www.heroeswm.ru/object_do.php', cookies=user.cookies, headers=user.headers, data=data)
    if response.status_code == 200:
        return 200
    
async def getJobBtn(html, job_id):
    soup = BeautifulSoup(html, 'lxml')
    captcha_img_tag = soup.find('img', class_='getjob_capcha')
    if captcha_img_tag:
        # Step 1: Define URL and download CAPTCHA
        captcha_img_url = f"https://www.heroeswm.ru/{captcha_img_tag['src']}"
        captcha_response = requests.get(captcha_img_url)

        # Step 2: Process the image
        img = Image.open(BytesIO(captcha_response.content))
        img = img.convert('RGB')
        gray = img.convert('L')

        # Perform OCR
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update based on your installation path
        captcha_text = pytesseract.image_to_string(img)
        img.show()
        # Output results
        print("captcha_img_url:", captcha_img_url)
        print("captcha_text:", captcha_text)
        return 500
    else:
        print("captcha not found")
        soup = BeautifulSoup(html, 'lxml')
        job_button = soup.find('input', {
            'type': 'image',
            'src': 'https://dcdn.heroeswm.ru/i/getjob/btn_work.png',
            'class': 'getjob_submitBtn',
            'onclick': 'return obj_c(0);',
            'id': 'wbtn'
        })
        if job_button:
            status = await jobDo(job_id)
            return status

    
async def getJob(id):
    params = {
        'id': id,
    }
    response = requests.get('https://www.heroeswm.ru/object-info.php', params=params, cookies=user.cookies, headers=user.headers)
    if response.status_code == 200:
        status = await getJobBtn(response.text, id)
        return status
    else:
        return 500

    
async def getJobs(html): 
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html, 'lxml')
    # Method 1: Using find()
    tabs = soup.find_all('a', string=lambda text: text and text.strip() == '»»»')
    print("len(tabs)", len(tabs))
    if len(tabs) > 0: 
        href = tabs[0]['href']
        id_value = href.split('id=')[1]
        return await getJob(id_value)
    else: 
        return False
    
async def doJob(work_type): 
    html = await jobsRequests(work_type)
    status = await getJobs(html)
    if status == 200:
        return status
    elif status == 500:
        return 500
    else:
        if status == False:
            if work_type == 'sh':
                await doJob('fc')
            elif work_type == 'fc':
                await doJob('mn')
