# TEST FOR DATABASE FILE, DO NOT CALL ON BACKEND

from database import *
from menu_parser import *
from random import randint

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
{
    "ratings": [
        {
            "dining_hall_id": "BMH",
            "rating": 3
        },
        {
            "dining_hall_id": "BMH",
            "rating": 1
        },
        {
            "dining_hall_id": "BMH",
            "rating": 5
        },
        {
            "dining_hall_id": "BMH",
            "rating": 2
        }
    ]
}


# ! for seeding db
# for file in [cs,bmh, nrh, rvc, dh]:
#     data = load_csv_file(os.path.join(os.path.dirname(__file__), "menus", file))

#     y = create_json_dict(data)

#     update_dining_hall(
#         file.split("_")[0].upper(), 
#         file.split("_")[0].upper(), [0,0], [0,0], y)

# data = load_csv_file("./menus/dh_week3_2022.csv")
# y = create_json_dict(data)
# print(y)

def random_ratings():
    all_meals = list(get_all_meals().keys())
    for meal in all_meals:
        for i in range(0, randint(0, 7)):
            set_rating(
                meal, 
                randint(1, 5),
                DINING_HALL_IDS[randint(0, len(DINING_HALL_IDS) - 1)])
random_ratings()