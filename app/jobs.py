from bs4 import BeautifulSoup
import random
from app.variables import user
import requests
from PIL import Image
from io import BytesIO
import pytesseract

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
    
async def getJobBtn(html):
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
    else:
        soup = BeautifulSoup(html, 'lxml')
        job_button = soup.find('input', {
            'type': 'image',
            'src': 'https://dcdn.heroeswm.ru/i/getjob/btn_work.png',
            'class': 'getjob_submitBtn',
            'onclick': 'return obj_c(0);',
            'id': 'wbtn'
        })
        if job_button:
            print("job_button", job_button)

    
async def getJob(id):
    params = {
        'id': id,
    }
    response = requests.get('https://www.heroeswm.ru/object-info.php', params=params, cookies=user.cookies, headers=user.headers)
    if response.status_code == 200:
        await getJobBtn(response.text)

    
async def getJobs(html): 
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html, 'lxml')
    # Method 1: Using find()
    tabs = soup.find_all('a', string=lambda text: text and text.strip() == '»»»')
    print("len(tabs)", len(tabs))
    if len(tabs) > 0: 
        href = tabs[0]['href']
        id_value = href.split('id=')[1]
        await getJob(id_value)
    else: 
        return False
    
async def getSuccessJob(work_type): 
    print("work_type", work_type)
    html = await jobsRequests(work_type)
    res = await getJobs(html)
    if res == False:
        if work_type == 'sh':
            await getSuccessJob('fc')
        elif work_type == 'fc':
            await getSuccessJob('mn')
    return res