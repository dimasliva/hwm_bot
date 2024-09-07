class User:
    def __init__(self, id, region, rest_move_time, href, cookies, headers):
        self.id = id
        self.href = href
        self.region = region
        self.cookies = cookies
        self.headers = headers
        self.rest_move_time = rest_move_time


user = User('', '', '0', {}, {}, {})

regions = [
    {
        'name': 'Empire Capital', 'id': 1, 'moveRight': 2, 'moveTop': 3, 'moveBottom': 5, 'moveLeft': 8, 'coordinates': {'cx': 50, 'cy': 50},
    },
    {
        'name': 'East River', 'id': 2, 'moveRight': 14, 'moveBottom': 11, 'moveLeft': 1, 'moveTop': 4, 'coordinates': {'cx': 51, 'cy': 50},
    },
    {
        'name': 'Tiger Lake', 'id': 3, 'moveRight': 4, 'moveBottom': 1, 'moveLeft': 12, 'moveTop': 6, 'coordinates': {'cx': 50, 'cy': 49},
    },
    {
        'name': "Rogues' Wood", 'id': 4, 'moveRight': 15, 'moveBottom': 2, 'moveLeft': 3, 'moveTop': 24, 'coordinates': {'cx': 51, 'cy': 49},
    },
    {
        'name': 'Wolf Dale', 'id': 5, 'moveRight': 11, 'moveBottom': 10, 'moveLeft': 7, 'moveTop': 1, 'coordinates': {'cx': 50, 'cy': 51},
    },
    {
        'name': 'Peaceful Camp', 'id': 6, 'moveRight': 24, 'moveBottom': 3, 'moveLeft': 9, 'moveTop': 0, 'coordinates': {'cx': 50, 'cy': 48},
    },
    {
        'name': 'Lizard Lowland', 'id': 7, 'moveRight': 5, 'moveBottom': 26, 'moveLeft': 0, 'moveTop': 8, 'coordinates': {'cx': 49, 'cy': 51},
    },
    {
        'name': 'Green Wood', 'id': 8, 'moveRight': 1, 'moveBottom': 7, 'moveLeft': 27, 'moveTop': 12, 'coordinates': {'cx': 49, 'cy': 50},
    },
    {
        'name': 'Eagle Nest', 'id': 9, 'moveRight': 6, 'moveBottom': 12, 'moveLeft': 23, 'moveTop': 0, 'coordinates': {'cx': 49, 'cy': 48},
    },
    {
        'name': 'Portal Ruins', 'id': 10, 'moveRight': 19, 'moveBottom': 0, 'moveLeft': 26, 'moveTop': 5, 'coordinates': {'cx': 50, 'cy': 52},
    },
    {
        'name': "Dragons' Caves", 'id': 11, 'moveRight': 0, 'moveBottom': 19, 'moveLeft': 0, 'moveTop': 2, 'coordinates': {'cx': 51, 'cy': 51},
    },
    {
        'name': 'Shining Spring', 'id': 12, 'moveRight': 3, 'moveBottom': 8, 'moveLeft': 13, 'moveTop': 9, 'coordinates': {'cx': 49, 'cy': 49},
    },
    {
        'name': 'Sunny City', 'id': 13, 'moveRight': 12, 'moveBottom': 27, 'moveLeft': 0, 'moveTop': 23, 'coordinates': {'cx': 48, 'cy': 49},
    },
    {
        'name': 'Magma Mines', 'id': 14, 'moveRight': 17, 'moveBottom': 0, 'moveLeft': 2, 'moveTop': 15, 'coordinates': {'cx': 52, 'cy': 50},
    },
    {
        'name': 'Bear Mountain', 'id': 15, 'moveRight': 18, 'moveBottom': 14, 'moveLeft': 4, 'moveTop': 16, 'coordinates': {'cx': 52, 'cy': 49},
    },
    {
        'name': 'Fairy Trees', 'id': 16, 'moveRight': 0, 'moveBottom': 15, 'moveLeft': 0, 'moveTop': 0, 'coordinates': {'cx': 52, 'cy': 48},
    },
    {
        'name': 'Harbour City', 'id': 17, 'moveRight': 0, 'moveBottom': 0, 'moveLeft': 14, 'moveTop': 18, 'coordinates': {'cx': 53, 'cy': 50},
    },
    {
        'name': 'Mithril Coast', 'id': 18, 'moveRight': 0, 'moveBottom': 17, 'moveLeft': 15, 'moveTop': 0, 'coordinates': {'cx': 53, 'cy': 49},
    },
    {
        'name': 'The Great Wall', 'id': 19, 'moveRight': 0, 'moveBottom': 20, 'moveLeft': 10, 'moveTop': 11, 'coordinates': {'cx': 51, 'cy': 52},
    },
    {
        'name': "Titans's Valley", 'id': 20, 'moveRight': 21, 'moveBottom': 0, 'moveLeft': 0, 'moveTop': 19, 'coordinates': {'cx': 51, 'cy': 53},
    },
    {
        'name': 'Fishing village', 'id': 21, 'moveRight': 0, 'moveBottom': 22, 'moveLeft': 20, 'moveTop': 0, 'coordinates': {'cx': 52, 'cy': 53},
    },
    {
        'name': 'Kingdom Castle', 'id': 22, 'moveRight': 0, 'moveBottom': 0, 'moveLeft': 0, 'moveTop': 21, 'coordinates': {'cx': 52, 'cy': 54},
    },
    {
        'name': 'Ungovernable Steppe', 'id': 23, 'moveRight': 9, 'moveBottom': 13, 'moveLeft': 0, 'moveTop': 0, 'coordinates': {'cx': 48, 'cy': 48},
    },
    {
        'name': "Crystal Garden", 'id': 24, 'moveRight': 0, 'moveBottom': 4, 'moveLeft': 6, 'moveTop': 0, 'coordinates': {'cx': 51, 'cy': 48},
    },
    {
        'name': 'Sublime Arbor', 'id': 27, 'moveRight': 8, 'moveBottom': 0, 'moveLeft': 0, 'moveTop': 13, 'coordinates': {'cx': 48, 'cy': 50},
    },
    {
        'name': 'The Wilderness', 'id': 26, 'moveRight': 10, 'moveBottom': 0, 'moveLeft': 0, 'moveTop': 7, 'coordinates': {'cx': 49, 'cy': 52},
    }
]

regions_btns = [
    'Empire Capital',
    'East River',
    'Tiger Lake',
    "Rogues' Wood",
    'Wolf Dale',
    'Peaceful Camp',
    'Lizard Lowland',
    'Green Wood',
    'Eagle Nest',
    'Portal Ruins',
    "Dragons' Caves",
    'Shining Spring',
    'Sunny City',
    'Magma Mines',
    'Bear Mountain',
    'Fairy Trees',
    'Harbor City',
    'Mithril Coast',
    'The Great Wall',
    "Titans's Valley",
    'Fishing village',
    'Kingdom Castle',
    'Ungovernable Steppe',
    "Crystal Garden",
    'Sublime Arbor',
    'The Wilderness',
]
