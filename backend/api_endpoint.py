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