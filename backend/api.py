from flask import Flask, Response
import json
import database
from flask_cors import CORS

from backend import player

app = Flask(__name__)
CORS(app)


@app.route('/getcountry/') ##End point to get ONE country.
def getcountry():
    try:
        response = { ##Save as response, returned value from the "get one country" function from database class.
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


@app.route('/getallcountries/') ##End point to get all countries of the game.
def getallcountries():
    try:
        response = database.getAllCountries() ##Save as response, returned value from the "get all countries" function from database class.
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route("/busdestinations/<location>") ##End point for bus destinations
def getneighbourcountries(location):
    try:
        response = database.neighbourcountries(location) ##Save as response, returned value from the "bus destinations" function from database class.
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route("/boatdestinations/<location>") ##End point for boat destinations
def getsamesea(location):
    try:
        response = database.countrysea(location) ##Save as response, returned value from the "boat destinations" function from database class.
        return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route("/planedestinations/<location>") ##End point for plane destinations.
def getplanedestinations(location):
    try:
        response = database.flydestination(location) ##Save as response, returned value from the "fly destination" function from database class.
        return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route("/money/")
def getmoney():
    try:
        money = player.getMoney()
        return {"money": money}
    except ValueError:
        return {"message": "Invalid number as addend", "status": 400}, 400



@app.errorhandler(404)  ## Error message in case of invalid endpoint
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
