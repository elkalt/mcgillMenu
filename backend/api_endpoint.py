from flask import Flask, make_response, request


app = Flask(__name__)


@app.route("/api/status")
def status():
    return make_response({"status": "ok"})


@app.route("/api/weekly/<int:week>")
def api():
    return make_response({"status": "ok"})
