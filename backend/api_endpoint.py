from flask import Flask, make_response, request
from database import *

app = Flask(__name__)


@app.route("/api/status")
def status():
    return make_response({"status": "ok"})

# get all dining hall information
@app.route("/api/dining_halls")
def api_get_all_dining_halls():
    return {
        "status": "ok",
        "data": get_all_dining_halls()
    }
    
# get all dishes
@app.route("/api/dishes")
def api_get_all_dishes():
    return {
        "status": "ok",
        "data": get_all_meals()
    }