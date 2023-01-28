# TEST FOR DATABASE FILE, DO NOT CALL ON BACKEND

from database import *


# print(get_dining_hall("bmh"))

# print(get_all_meals())

# create_meal({
#     "name": "Poutine",
#     "options": [
#         "VF",
#         "VE"
#     ]
# })

# set_rating("poutine", 3, "bmh")
# print(get_ratings_by_dining_hall("poutine", "bmh"))

all_halls = [
 {
    "hall_id": "BMH",
    "name": "Bishop Mountain Hall",
    "location": [45.510631259110454, -73.58383411905979],
    "hours": {
        "Monday-Friday": [730,2130],
        "Weekends": [1030,2000],
        "Holidays": None
    },
    "menu": {}
 },
{
    "hall_id": "RVC",
    "name": "Royal Victoria College",
    "location": [45.505464957314736, -73.57361900678244],
    "hours": {
        "Monday-Friday": [730,2130],
        "Weekends": [1130,2000],
        "Holidays": None
    },
    "menu": {}
 },
 {
    "hall_id": "CS",
    "name": "Carrefour Sherbrooke",
    "location": [45.506693948116705, -73.57252871520632],
    "hours": {
        "Monday-Friday": [800,2030],
        "Weekends": [1030,2030],
        "Holidays": [1030,2030]
    },
    "menu": {}
 },
 {
    "hall_id": "NRH",
    "name": "New Residence Hall",
    "location": [45.51093394015983, -73.57596153832759],
    "hours": {
        "Monday-Friday": [800,2030],
        "Weekends": [1030,2030],
        "Holidays": [1030,2030]
    },
    "menu": {}
 },
 {
    "hall_id": "DH",
    "name": "Douglas Hall",
    "location": [45.50995021462863, -73.58246692277133],
    "hours": {
        "Monday-Friday": [1800,2000],
        "Weekends": None,
        "Holidays": None
    },
    "menu": {}
 },
]
# for hall in all_halls:
#     update_dining_hall(hall["hall_id"], hall["name"], hall["location"], hall["hours"], hall["menu"])

# print(get_all_dining_halls())


update_meal("poutine", {
    "name": "Poutine",
    "options": [
        "VF",
        "VE"
    ]
})

update_meal("porridge", {
    "name": "Porridge",
    "options": [
        "VE"
    ]
})