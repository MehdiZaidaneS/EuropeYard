import json
import random
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mehdizaidane1",
    database="EuropeYard",
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

