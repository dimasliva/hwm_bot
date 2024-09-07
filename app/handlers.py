from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from app.keyboards import main, regions_keyboard, user_keyboard
from app.user import setUser
from app.variables import user, regions_btns
from app.requests import getCurrentRegion, moveToRegion, toJob
from app.user import getUser

from app.functions import getRegionsToMove, getTimeMoveToRegion

router = Router()

@router.message(CommandStart())
async def send_welcome(message: Message):
    print(message.from_user)
    await message.answer("Чтобы начать нажмите на кнопку 'Играть'", reply_markup=main)

@router.message(F.photo)
async def photo_handler(message: Message):
    photo_data= message.photo[-1]
    await message.answer(f"{photo_data}")
    
@router.message(lambda message: message.text == "👨‍💻 Как войти?")
async def on_how_to_join(message: Message):
    await message.answer(f"1. Зайдите в https://www.heroeswm.ru/map.php\n2.Нажмите на ПКМ и нажмите на 'Просмотреть код'")
    await message.answer_photo(photo=FSInputFile(path='./app/images/Guide_1.png'))
    await message.answer(f"3. Перейдите в открывшейся консоли, на вкладку Сеть/Network.\n4. Найдите запрос с названием 'map.php'\n5. Нажмите ПКМ по запросу\n6. Навидитесь на 'копировать/copy'\n7. Нажмите на 'Копировать как cURL (bash)/Copy as cURL (bash)'")
    await message.answer_photo(photo=FSInputFile(path='./app/images/Guide_2.png'))
    await message.answer(f"8. Зайдите в https://curlconverter.com/python/\n9. Вставьте скопированное в поле 'curl command'\n10. Скопируйте текст начиная с 'cookes=...' и до конца скобок headers")
    await message.answer_photo(photo=FSInputFile(path='./app/images/Guide_3.png'))
    await message.answer(f"11. Введите в боте команду /auth 'вствьте копированные данные'")
    await message.answer_photo(photo=FSInputFile(path='./app/images/Guide_4.png'))
    
@router.message(lambda message: message.text == "⛏️ Работать")
async def on_job(message: Message):
    await toJob()
    await message.answer(f"Вы строились на работу!")

@router.message(lambda message: message.text == "🚗 Сменить регион")
async def on_how_to_join(message: Message):
    await message.answer(f"Выберите регион", reply_markup=regions_keyboard)

@router.message(Command('auth'))
async def auth_handler(message: Message):
    status = setUser(message.text)
    if status == 500:
        await message.answer(f"Неверные данные.")
    else:
        await getUser()
        await getCurrentRegion()
        await message.answer(f"Вход успешен!", reply_markup=user_keyboard)


@router.callback_query(lambda callback: callback.data in regions_btns)
async def on_regions_to_move(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Герой отправился в {callback.data}")
    regions_for_move = getRegionsToMove(callback.data)
    total_time = getTimeMoveToRegion(len(regions_for_move))
    user.rest_move_time = total_time
    await callback.message.answer(f"Время прибытия: {user.rest_move_time}")
    await moveToRegion(callback.data, regions_for_move)
    await callback.message.answer(f"Герой прибыл!")


# @router.callback_query(F.data == 'AuthNo')
# async def onAuthNo(callback: CallbackQuery):
#     await callback.answer()
#     await on_auth(callback.message)


@router.message(Command('location'))
async def location(message: Message):
    region = await getCurrentRegion()
    await message.answer(region)
