from app.regionFuncs import getRegionByName
from app.autowalker import findRegionToMove 
from datetime import datetime, timedelta

def getTimeMoveToRegion(count_region):
    # Получаем текущую дату и время
    current_time = datetime.now()
    # Количество секунд, которое нужно добавить
    seconds_to_add = count_region * 40
    # Добавление секунд
    new_time = current_time + timedelta(seconds=seconds_to_add)

    # Форматирование времени в HH:MM:SS
    formatted_time = new_time.strftime('%H:%M:%S')
    return formatted_time
    
def getRegionsToMove(from_region, region_to_move_name):
    region_to_move = getRegionByName(region_to_move_name)
    founded_regions = findRegionToMove(region_to_move, from_region)
        
    print('founded regions: ')
    for region in founded_regions:
        print('region', region)
    
    return founded_regions
    
