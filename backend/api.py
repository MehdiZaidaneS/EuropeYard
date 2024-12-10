from flask import Flask, Response
import json
import database
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/getcountry/')
def getcountry():
    try:
        response = {
            "country": database.getOneCountry()
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route('/getallcountries/')
def getallcountries():
    try:
        response = database.getAllCountries()
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route("/busdestinations/<location>")
def getneighbourcountries(location):
    try:
        response = database.neighbourcountries(location)
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route("/boatdestinations/<location>")
def getsamesea(location):
    try:
        response = database.countrysea(location)
        return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route("/planedestinations/<location>")
def getplanedestinations(location):
    try:
        response = database.flydestination(location)
        return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
