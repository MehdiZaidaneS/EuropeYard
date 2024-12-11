import json
import random
import mysql.connector

# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv()


## Setting connection with Mysql database
connection = mysql.connector.connect(
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWD"),
    database=os.getenv("DATABASE"),
    autocommit=True
)

## Returns randomly ONE country's name after fetching the query from db.
def getOneCountry():

    countriesName = []

    cursor = connection.cursor()
    sql = f"SELECT * FROM country WHERE continent = 'EU'"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
     countriesName.append(row[1])

    randomNumber = random.randint(0, len(countriesName)-1)

    return countriesName[randomNumber]


## Returns a LIST of all the countries names after fetching the query from db.
def getAllCountries():

    countriesName = []

    cursor = connection.cursor()
    sql = f"SELECT * FROM country WHERE continent = 'EU'"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
     countriesName.append(row[1])

    return countriesName


## Return a list of neighbour countries (you can travel by bus) from the location entered.
def neighbourcountries(location):

    cursor = connection.cursor()
    sql = f"SELECT * FROM country WHERE continent = 'EU' AND name = '{location}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    ncountries = json.loads(result[4])

    return ncountries

## Checks if the location has sea. If location has sea, will add to a list all the countries that shares same sea.
def countrysea(location):

    sameseacountries = []

    cursor = connection.cursor()
    sql = f"SELECT * FROM country WHERE name = '{location}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    sea = result[3]

    if sea != "No":
       cursor = connection.cursor()
       sameSea = f"SELECT name FROM country WHERE sea= '{sea}'"
       cursor.execute(sameSea)
       result = cursor.fetchall()
       for row in result:
          if row[0] != location:
             sameseacountries.append(row[0])

       return sameseacountries

    else:
       return sameseacountries

## Return a list of destinations you can fly (you can travel by plane) from the location entered.
def flydestination(location):

    destinations = []
    cursor = connection.cursor()
    sql = f"SELECT name FROM country WHERE continent = 'EU'"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        if row[0] != location: ## If the row has DIFFERENT name than location is added to list (Basically, not adding the location as possible destination)
           destinations.append(row[0])

    return destinations


