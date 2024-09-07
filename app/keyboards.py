from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from app.variables import regions_btns
from app.regionFuncs import getRegionName
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup
from app.variables import user

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🕹️ Играть', web_app=WebAppInfo(url='https://www.heroeswm.ru/map.php'))],
    [KeyboardButton(text='👨‍💻 Как войти?')],
], resize_keyboard=False, input_field_placeholder='Выберите пункт меню...')

user_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='⛏️ Работать'), KeyboardButton(text='🚗 Сменить регион')],
    [KeyboardButton(text='📈 Статистика'), KeyboardButton(text='⚔️ Гильдия Наемников')],
], resize_keyboard=False, input_field_placeholder='Выберите пункт меню...')

def create_dynamic_keyboard(buttons):
    builder = InlineKeyboardBuilder()

    for key in buttons:
        builder.button(text=key, callback_data=key)
    builder.adjust(3)
    return builder.as_markup()

regions_keyboard = create_dynamic_keyboard(regions_btns)
def getCurrentRegionKeyboard(): 
    return create_dynamic_keyboard([f"Текущий регион: {getRegionName(user.region)}"])