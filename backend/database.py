import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

DINING_HALL_IDS = ["RVC", "BMH", "NRH", "DH", "CS"]

def check_creds():
    if not firebase_admin._apps:
        cred = credentials.Certificate({
        "type": "service_account",
        "project_id": "mchacks-10",
        "private_key_id": "79e96426d0b88ce7bef47d9786eca188b631b4d8",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCqtKoMMavJAFdr\nqvwxjDdqnUkkmNYgAEhaxOsQsU7mTt5jYeRL77gAPvAiEMOIgD2qVZ9K6XRdaCo6\nTwEatfwzffIPJXP08hTeeYNmfF+XrJPN7trU7b3hiaJLt4wPI0tKC2z6s7MnsCSQ\nXQvJSIhfazV9H7Z6IALqtlj6YIO1m6AM/JSFFz3UfrBFWbPtPbctuCQ7BLwUvvfh\nD/dhKy8VRqPzT4YR3X6DoIrVCYjriTFbkocWqgP11VxLbGdY+ggEVHIhQLRul6Q4\nok1gVvkUldFTjMbex8GoeKqTzZaL2c0TBgwclrHWap79gsXAoDlP7hSSVH6cWYYf\njY1x+5s5AgMBAAECggEAFciw05YKHUAjJ8z92mfRkZQpR5eOaa6HjTfIZIyv7CF/\n7TBKlSst8LAXbk1z2mk9FU3QYluo2xumGeNHmYxENyD5IRgvNECpS5u3mj5AZ6dh\nBDxZJieBnfS1ppJxd+QR4UzUdyiz8dpfTCHnlWPhbUXN4V4I6AxKOwASmj7zR9sz\nEMqOk/KYjCj7nLctm8f5P4DSBeaF4o4Cc4F/B1gNuZPOsU8UbuJKzi5tPm5IEA03\nboesQqDtMr9jw4MCa1DSa497FpyjmICx3kp7y+KtUkV1ksmbYGhFXCxgBuLzalWl\nsPnQXYBXADAzzkKQ1HHl8BS6GkRkMJt5+MHfJEuOhQKBgQDdLvf35Lf93iUeeBeV\nY9Ao6WOz6WSaxGuBG0VHesvDF17Ns36LHPRUYzsf3FB5aE/AibfpxEmOEE0Fr15q\nHCj1cj+K7jTEh3PZwfsTdtTr6LGG0c9948hFAWbdgehmdutnHwJN/01Mtggh7ZgZ\n0Ex6nqd7dA7K9Bc8Y73jHw6n7QKBgQDFk5frWQ2HVlWojejP4LPX4oszDbklKR4i\nIKbdVIdCQDyadN7gpf20rxvTZv66ukqDlXb0Vkv81/ZCRa4LPz4o5YsLwqWhvFKa\n9vXE4tQC50Fbsci6bcIotrgrJF6AcpDOmvowgpG7+1kRhbk/tXEMzW6Zk9x3Leuo\ns7ZDFB1+/QKBgQCzN1F4rPxgWVUeQRRq2XtbCvDcYCpCNREehWg3KMpdg1wvtFa+\nhXF7xwOrJyqVlO26Blzcr00iLRcbmiMYO0T8y9usyKI887vtH34/ITQZCmx93xcO\n3DfzodUlehNCouzOm5OUe164323rf8aUc/DkEhWGtF0gGXOSXQcJNqr7aQKBgQCB\nnlGVaefxONeba/Ynor/5yrsNtFwZn/8P3qH6JEFUWnYn0rKBaQSnrBWyPCizchH+\nf2j55T+W0kvRsIr8//GUvPrarUkicT00Qv57u1/hw7tiH6GThPxS34S1cPe6hu6v\nTIcEmjRnwf7t+u/MdwmCn6eGg7WoTm0DUVsqaKDtNQKBgQCHs+7j1+Sz+e0qNl4c\nVO8LNnvbdz3C9LaMwgKKZFSV/OOHsKzf9P89byopfRAF3skJj2ySqzNsh1C14foS\nx/hCWuVzxDcAkyWuzDbBYiN43mDsC4sfPR4L1lkQGKBeUtK53LYj6QzhR9NtH8ry\ngB5zXMotoN9e63K61TuYHaGdug==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-pasvc@mchacks-10.iam.gserviceaccount.com",
        "client_id": "108911766112944071412",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-pasvc%40mchacks-10.iam.gserviceaccount.com"
        })
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
                    update_meal(meal_id.lower(), menu[day][day_meal][meal_id])


def get_dining_hall(dining_hall_code: str):
    db = check_creds()
    dining_hall_ref = db.collection("dining_halls").document(dining_hall_code)
    dining_hall = dining_hall_ref.get().to_dict()
    return dining_hall

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

def create_meal(meal):
    db = check_creds()
    meal["ratings"] = []
    meal_ref = db.collection("meals").document(meal["name"].lower()).set(meal)
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
    for rating in ratings:
        if rating["dining_hall_id"] == dining_hall_id :
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