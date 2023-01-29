import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

DINING_HALL_IDS = ["RVC", "BMH", "NRH", "DH", "CS"]

def check_creds():
    if not firebase_admin._apps:
        cred = credentials.Certificate("./token.json")
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

# GF, V, VE, DF, MSC, H
def update_dining_hall(
    dining_hall_code: str,
    dining_hall_name: str,
    location,
    hours,
    menu: dict
    # menu is of the same format as ./-/bmh.json
):
    db = check_creds()
    # ! verify
    menu_ref = db.collection("dining_halls").document(dining_hall_code)
    if not menu_ref.get().exists:
            menu_ref.set({
                "name": dining_hall_name,
                "location": location,
                "hours": hours,
                "menu": menu
            })
    else:
        menu_ref.update({
            "menu": menu
        })
        


    # update meals
    all_meals = get_all_meals()
    # check if meal exists
    days = menu.keys()
    for day in days:
        day_meals = menu[day].keys()
        for day_meal in day_meals:
            meals = menu[day][day_meal].keys()
            for meal_id in meals:
                meal_exists = False
                for all_meal_id in all_meals.keys():
                    if meal_id.lower() == all_meal_id.lower():
                        meal_exists = True
                        break
                if not meal_exists:
                    meal_id_escaped = meal_id.replace("w/", "with ").replace("/", " or")
                    print(meal_id_escaped)
                    create_meal(meal_id_escaped.lower(), menu[day][day_meal][meal_id])


def get_dining_hall(dining_hall_code: str):
    db = check_creds()
    dining_hall_ref = db.collection("dining_halls").document(dining_hall_code)
    dining_hall = dining_hall_ref.get().to_dict()
    return dining_hall

def get_all_dining_halls():
    db = check_creds()
    dining_halls_ref = db.collection("dining_halls")
    dining_halls = dining_halls_ref.stream()
    dining_halls_dict = {}
    for dining_hall in dining_halls:
        dining_halls_dict[dining_hall.id] = dining_hall.to_dict()

    return dining_halls_dict

# ! Meals
def get_all_meals():
    db = check_creds()
    meals_ref = db.collection("meals")
    meals = meals_ref.stream()
    meals_dict = {}
    for meal in meals:
        meals_dict[meal.id] = meal.to_dict()

    return meals_dict

def get_meal(meal_id):
    db = check_creds()
    meal_ref = db.collection("meals").document(meal_id)
    if not meal_ref.get().exists:
        return None
    meal = meal_ref.get().to_dict()
    return meal

def update_meal(meal_id, meal):
    db = check_creds()
    meal_ref = db.collection("meals").document(meal_id)
    meal_ref.set(meal)

def create_meal(meal_id, meal):
    db = check_creds()
    meal["ratings"] = []
    meal_ref = db.collection("meals").document(meal_id.lower()).set(meal)
    return meal_ref

# ! Ratings

def get_ratings(meal_id):
    db = check_creds()
    meal_ref = db.collection("meals").document(meal_id)
    if not meal_ref.get().exists:
        return None
    meal = meal_ref.get().to_dict()
    return meal["ratings"]

def get_ratings_by_dining_hall(meal_id, dining_hall_id):
    db = check_creds()
    meal_ref = db.collection("meals").document(meal_id)
    if not meal_ref.get().exists:
        return None
    meal = meal_ref.get().to_dict()
    ratings = meal["ratings"]
    ratings_by_dining_hall = []
    # print(ratings)
    for rating in ratings:
        if not type(rating) == dict or not rating["dining_hall_id"] or not rating["rating"]:
            continue
        elif rating["dining_hall_id"] == dining_hall_id:
            ratings_by_dining_hall.append(rating)

    return ratings_by_dining_hall

def set_rating(meal_id, rating, dining_hall_id):
    db = check_creds()
    # check if dining hall id exists
    if dining_hall_id not in DINING_HALL_IDS and dining_hall_id.upper() not in DINING_HALL_IDS:
        print("Invalid dining hall id")
        return None
    meal_ref = db.collection("meals").document(meal_id)
    if not meal_ref.get().exists:
        return None
    meal = meal_ref.get().to_dict()
    meal["ratings"].append({
        "rating": rating,
        "dining_hall_id": dining_hall_id
    })
    meal_ref.set(meal)

def get_dining_hall_ratings(dining_hall_id):
    db = check_creds()
    # check if dining hall id exists
    if dining_hall_id not in DINING_HALL_IDS and dining_hall_id.upper() not in DINING_HALL_IDS:
        print("Invalid dining hall id")
        return None
    meals = get_all_meals()
    ratings = []
    for meal_id in meals:
        ratings.append(get_ratings_by_dining_hall(meal_id, dining_hall_id))
    return ratings