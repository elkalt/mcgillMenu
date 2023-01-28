from flask import Flask, make_response, request
# $ flask run --host=0.0.0.0
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



