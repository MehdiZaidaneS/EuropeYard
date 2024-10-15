import json

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mehdizaidane1",
    database="EuropeYard",
    autocommit=True
)

countriesName = []


def getCountries():

    cursor = connection.cursor()
    sql = f"SELECT * FROM country WHERE continent = 'EU'"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        countriesName.append(row[1])
        if row[1] == "Spain":
          ncountries = json.loads(row[4])
          for country in ncountries:
              print(country)
        print(row[4])





getCountries()
print(countriesName)