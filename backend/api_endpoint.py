from flask import Flask, make_response, request
from flask_cors import CORS, cross_origin

from database import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/status")
@cross_origin()
def status():
    return make_response({"status": "ok"})

# get all dining hall information
@app.route("/api/dining_halls")
@cross_origin()
def api_get_all_dining_halls():
    return {
        "status": "ok",
        "data": get_all_dining_halls()
    }

# get all dishes
@app.route("/api/dishes")
@cross_origin()
def api_get_all_dishes():
    return {
        "status": "ok",
        "data": get_all_meals()
    }

# get single dish
@app.route("/api/dishes/<dish_id>")
@cross_origin()
def api_get_dish_by_id(dish_id):
    dish = get_meal(dish_id)
    if dish is None:
        return {
            "status": "error",
            "message": "Dish not found"
        }, 404
    return {
        "status": "ok",
        "data": dish
    }

# get single dining hall
@app.route("/api/dining_halls/<dining_hall_id>")
@cross_origin()
def api_get_dining_hall_by_id(dining_hall_id):
    dining_hall = get_dining_hall(dining_hall_id.upper())
    if dining_hall is None:
        return {
            "status": "error",
            "message": "Dining hall not found"
        }, 404
    return {
        "status": "ok",
        "data": dining_hall
    }

# get all ratings for a dish
@app.route("/api/dishes/<dish_id>/ratings")
@cross_origin()
def api_get_ratings_by_dish_id(dish_id):
    ratings = get_ratings(dish_id)
    if ratings is None:
        return {
            "status": "error",
            "message": "Dish not found"
        }, 404
    return {
        "status": "ok",
        "data": ratings
    }

# get all ratings for a dish at a dining hall
@app.route("/api/dishes/<dish_id>/ratings/<dining_hall_id>")
@cross_origin()
def api_get_ratings_by_dish_id_and_dining_hall_id(dish_id, dining_hall_id):
    ratings = get_ratings_by_dining_hall(dish_id, dining_hall_id)
    if ratings is None:
        return {
            "status": "error",
            "message": "Ratings not found"
        }, 404
    return {
        "status": "ok",
        "data": ratings
    }

# get all ratings for a dining hall
@app.route("/api/dining_halls/<dining_hall_id>/ratings")
@cross_origin()
def api_get_ratings_by_dining_hall_id(dining_hall_id):
    ratings = get_dining_hall_ratings(dining_hall_id)
    if ratings is None:
        return {
            "status": "error",
            "message": "Ratings not found"
        }, 404
    return {
        "status": "ok",
        "data": ratings
    }