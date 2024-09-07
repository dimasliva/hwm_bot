from app.regionFuncs import getRegionById
from app.variables import user

def getRegionBetween(region_one, region_two):
    around_region_two = []

    if region_two["moveLeft"] != 0:
        around_region_two.append(region_two["moveLeft"])
    if region_two["moveRight"] != 0:
        around_region_two.append(region_two["moveRight"])
    if region_two["moveBottom"] != 0:
        around_region_two.append(region_two["moveBottom"])
    if region_two["moveTop"] != 0:
        around_region_two.append(region_two["moveTop"])
            
    around_region_one = []
    if region_one["moveLeft"] != 0 :
        around_region_one.append(region_one["moveLeft"])
    if region_one["moveRight"] != 0 :
        around_region_one.append(region_one["moveRight"])
    if region_one["moveTop"] != 0 :
        around_region_one.append(region_one["moveTop"])
    if region_one["moveBottom"] != 0 :
        around_region_one.append(region_one["moveBottom"])
    for sideID in around_region_one:
        break_side = False
        if sideID in around_region_two and sideID != 0:
            found_middle_region = getRegionById(sideID)
            break_side = True
            return found_middle_region
        if break_side: 
            break

def removeAdditionalRegions(search_region, regions):
    # Находим индекс элемента с именем "Dragons' Caves"
    index = next((i for i, item in enumerate(regions) if item['name'] == search_region), None)

    # Если элемент найден, обрезаем массив до этого индекса (включительно)
    if index is not None:
        regions = regions[:index + 1]
    print()
    unique_list = []
    for item in regions:
        if item not in unique_list:
            unique_list.append(item)

    return(unique_list)  
    
def getRegionSides(region, onlyID):
    sides_region = []
    if region["moveLeft"] != 0 :
        if onlyID:
            sides_region.append(region["moveLeft"])
        else:
            sides_region.append(getRegionById(region["moveLeft"]))
    if region["moveRight"] != 0 :
        if onlyID:
            sides_region.append(region["moveRight"])
        else:
            sides_region.append(getRegionById(region["moveRight"]))
    if region["moveTop"] != 0 :
        if onlyID:
            sides_region.append(region["moveTop"])
        else:
            sides_region.append(getRegionById(region["moveTop"]))
    if region["moveBottom"] != 0 :
        if onlyID:
            sides_region.append(region["moveBottom"])
        else:
            sides_region.append(getRegionById(region["moveBottom"]))
    return sides_region

def getRegionIDSides(region):
    return [region["moveTop"], region["moveLeft"], region["moveBottom"], region["moveRight"]]

def checkRegionIsAround(region, region_around):
    return (region["moveLeft"] in region_around) or (region["moveRight"] in region_around) or (region["moveTop"] in region_around) or (region["moveBottom"] in region_around)
     
def checkSideIDAroundRegion(sideID, region_around):
    return (sideID in region_around) and (sideID != 0)
     
def getMinMaxCxXy(coord_one, coord_two):
    if(coord_one > coord_two):
        start_cx = coord_one
        end_cx = coord_two
    else:
        start_cx = coord_two
        end_cx = coord_one
    print('coord_one', coord_one)
    print('coord_two', coord_two)
    print('[start_cx, end_cx]', [start_cx, end_cx])
    return [start_cx, end_cx]
def findRegionToMove(search_region):
    condition_near_user = (search_region["moveLeft"] == user.region["id"]) or (search_region["moveRight"] == user.region["id"]) or (search_region["moveTop"] == user.region["id"]) or (search_region["moveBottom"] == user.region["id"])
    if condition_near_user: 
        found_region = search_region
        return removeAdditionalRegions(search_region["name"], [found_region])
        
    else:
        around_user = getRegionSides(user.region, True)
        condition_middle_region_around_user_search = checkRegionIsAround(search_region, around_user)
        
        if condition_middle_region_around_user_search:
            for sideID in getRegionIDSides(search_region) :
                if sideID in around_user and sideID != 0:
                    found_middle_region = getRegionById(sideID)
                    return removeAdditionalRegions(search_region["name"], [found_middle_region, search_region])
        else:
            for six_region_around_user in getRegionSides(search_region, False):
                break_for = False
                if checkRegionIsAround(six_region_around_user, around_user):
                    sidesID = getRegionIDSides(six_region_around_user) 
                    for sideID in sidesID:
                        if sideID in around_user and sideID != 0:
                            found_middle_region = getRegionById(sideID)
                            break_for = True
                            return removeAdditionalRegions(search_region["name"], [found_middle_region, six_region_around_user, search_region])
                            break
                else:
                    for region_around_five_region in getRegionSides(six_region_around_user, False):
                        break_for = False
                        if checkRegionIsAround(region_around_five_region, around_user):
                            for side_side_id in getRegionIDSides(region_around_five_region):
                                if checkSideIDAroundRegion(side_side_id, around_user):
                                    break_for = True
                                    found_middle_side_region = getRegionById(side_side_id)
                                    between_region = getRegionBetween(found_middle_side_region, six_region_around_user)
                                    return removeAdditionalRegions(search_region["name"], [found_middle_side_region, between_region, six_region_around_user, search_region])
                                    break
                        if break_for:
                            break 
                        else:
                            for four_region_around_user in getRegionSides(region_around_five_region, False):
                                five_break = False
                                if checkRegionIsAround(four_region_around_user, around_user):
                                    for side_id_third_region in getRegionIDSides(four_region_around_user):
                                        if checkSideIDAroundRegion(side_id_third_region, around_user):
                                            break_for = True
                                            found_middle_side_side_region = getRegionById(side_id_third_region)
                                            between_between_region = getRegionBetween(found_middle_side_side_region, region_around_five_region)
                                            five_region_around_user = getRegionBetween(between_between_region, six_region_around_user)
                                            return removeAdditionalRegions(search_region["name"], [found_middle_side_side_region, between_between_region, five_region_around_user, six_region_around_user, search_region])
                                            break
                                if five_break:
                                    break
                                else:
                                    for region_around_third_region in getRegionSides(four_region_around_user, False):
                                        six_break = False
                                        if checkRegionIsAround(region_around_third_region, around_user):
                                            for side_id_third_region in getRegionIDSides(region_around_third_region):
                                                six_break = False
                                                if checkSideIDAroundRegion(side_id_third_region, around_user):
                                                    six_break = True
                                                    region_around_user = getRegionById(side_id_third_region)
                                                    second_region_around_user = getRegionBetween(region_around_user, four_region_around_user)
                                                    five_region_around_user = getRegionBetween(four_region_around_user, six_region_around_user)
                                                    return removeAdditionalRegions(search_region["name"], [region_around_user, second_region_around_user, four_region_around_user, five_region_around_user, six_region_around_user, search_region])
                                                    break
                                        if six_break:
                                            break
                                        else:
                                            for second_region in getRegionSides(region_around_third_region, False):
                                                seven_break = False
                                                if checkRegionIsAround(second_region, around_user):
                                                    for side_id_third_around_region in getRegionIDSides(second_region):
                                                        if checkSideIDAroundRegion(side_id_third_around_region, around_user):
                                                            seven_break = True
                                                            region_around_user = getRegionById(side_id_third_around_region)
                                                            five_region_around_user = getRegionBetween(four_region_around_user, six_region_around_user)
                                                            third_region_around_user = getRegionBetween(second_region, four_region_around_user)
                                                            return removeAdditionalRegions(search_region["name"], [region_around_user, second_region, third_region_around_user, four_region_around_user, five_region_around_user, six_region_around_user, search_region])
                                                            break
                                                if seven_break:
                                                    break
                                                else:
                                                    for second_region_around_user in getRegionSides(second_region, False):
                                                        eight_break = False
                                                        if checkRegionIsAround(second_region_around_user, around_user):
                                                            for side_id_third_around_region in getRegionIDSides(second_region_around_user):
                                                                if checkSideIDAroundRegion(side_id_third_around_region, around_user):
                                                                    eight_break = True
                                                                    region_around_user = getRegionById(side_id_third_around_region)
                                                                    third_region_around_user = getRegionBetween(second_region_around_user, region_around_third_region)
                                                                    five_region_around_user = getRegionBetween(four_region_around_user, six_region_around_user)
                                                                    seven_region_around_user = getRegionBetween(region_around_third_region, five_region_around_user)
                                                                 
                                                                    return removeAdditionalRegions(search_region["name"], [region_around_user, second_region_around_user, third_region_around_user, region_around_third_region, seven_region_around_user, five_region_around_user, six_region_around_user, search_region])
                                                                    break
                                                        if eight_break:
                                                            break
                                                        else:
                                                            for nine_region_around_search in getRegionSides(second_region_around_user, False):
                                                                pre_last_break = False
                                                                if checkRegionIsAround(nine_region_around_search, around_user):
                                                                    for side_id_third_around_region in getRegionIDSides(nine_region_around_search):
                                                                        if checkSideIDAroundRegion(side_id_third_around_region, around_user):
                                                                            pre_last_break = True
                                                                            break_for = True
                                                                            region_around_user = getRegionById(side_id_third_around_region)
                                                                            third_region_around_user = getRegionBetween(nine_region_around_search, second_region)
                                                                            if third_region_around_user["id"] == search_region["id"]:
                                                                                return [region_around_user, nine_region_around_search, search_region]
                                                                            region_four_around_five = getRegionBetween(third_region_around_user, region_around_third_region)
                                                                            five_region_around_user = getRegionBetween(four_region_around_user, six_region_around_user)
                                                                            if five_region_around_user["id"] == search_region["id"]:
                                                                                return [region_around_user, nine_region_around_search, search_region]
                                                                            seven_region_around_user = getRegionBetween(region_around_third_region, five_region_around_user)
                                                                            return removeAdditionalRegions(search_region["name"], [region_around_user, nine_region_around_search, third_region_around_user, region_four_around_five, region_around_third_region, seven_region_around_user, five_region_around_user, six_region_around_user, search_region])
                                                                            break
                                                                if pre_last_break:
                                                                    break
                                                                else:
                                                                    for last_region_around_search in getRegionSides(nine_region_around_search, False):
                                                                        if checkRegionIsAround(last_region_around_search, around_user):
                                                                            for side_id_third_around_region in getRegionIDSides(last_region_around_search):
                                                                                last_break = False
                                                                                if checkSideIDAroundRegion(side_id_third_around_region, around_user):
                                                                                    break_for = True
                                                                                    region_around_user = getRegionById(side_id_third_around_region)
                                                                                    third_region_around_user = getRegionBetween(last_region_around_search, second_region_around_user)
                                                                                    region_four_around_five = getRegionBetween(second_region_around_user, region_around_third_region)
                                                                                    five_region_around_user = getRegionBetween(four_region_around_user, six_region_around_user)
                                                                                    seven_region_around_user = getRegionBetween(region_around_third_region, five_region_around_user)
                                                                                    return removeAdditionalRegions(search_region["name"], [region_around_user, last_region_around_search, third_region_around_user, second_region_around_user, region_four_around_five, region_around_third_region, seven_region_around_user, five_region_around_user, six_region_around_user, search_region])
                                                                                    break
                                                                                if last_break:
                                                                                    break

                    

            

 

