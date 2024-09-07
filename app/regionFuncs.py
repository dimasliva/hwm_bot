from app.variables import regions

def getRegionByName(target_name):
    for item in regions:
        if item['name'] == target_name:
            found_object = item
            return found_object

def getRegionById(target_id):
    for item in regions:
        if item['id'] == target_id:
            found_object = item
            return found_object
        
def getRegionName(target_region):
    if target_region:
        return target_region['name']
    else:
        return ''
    
def getRegionByCoords(coord):
    print("coord", coord)