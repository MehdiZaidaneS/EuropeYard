import json
import random
import requests
import mysql.connector
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()


connection = mysql.connector.connect(
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWD"),
    database=os.getenv("DATABASE"),
    autocommit=True
)

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

def getAllCountries():

    countriesName = []

    cursor = connection.cursor()
    sql = f"SELECT * FROM country WHERE continent = 'EU'"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
     countriesName.append(row[1])

    return countriesName


def neighbourcountries(location):

    cursor = connection.cursor()
    sql = f"SELECT * FROM country WHERE continent = 'EU' AND name = '{location}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    ncountries = json.loads(result[4])

    return ncountries


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


def flydestination(location):

    destinations = []
    cursor = connection.cursor()
    sql = f"SELECT name FROM country WHERE continent = 'EU'"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        if row[0] != location:
           destinations.append(row[0])

    return destinations


