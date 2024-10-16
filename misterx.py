import random
from database import *

currentLocation = ""
turns = 0


def spawnpoint(): ##Setting current location of Mister X with the method getOneCountry()
    global currentLocation
    currentLocation = getOneCountry()


def positionReveal(): ##It reveals Mister X position
    print("Mister X is in " + currentLocation)


## In case neighbour country list is not empty, Mister X travels randomly to one of the neigh.countries.
## In case it is empty, calls boatmovement() function.
def busmovement():
    global currentLocation
    ncountrylist = neighbourcountries(currentLocation) ##Saving in variable return value of neighbourcountries() function.

    if ncountrylist:
        index = random.randint(0, len(ncountrylist) - 1)
        currentLocation = ncountrylist[index]
        print("Mister X used: Bus")
    else:
        boatmovement()


## In case shared sea list is not empty, Mister X travels randomly to one of the shared sea countries.
## In case it is empty, calls busmovement() function.
def boatmovement():
    global currentLocation
    sharedsealist = countrysea(currentLocation) ##Saves in variable the return value of countrysea() function.

    if sharedsealist:
        index = random.randint(0, len(sharedsealist) - 1)
        currentLocation = sharedsealist[index]
        print("Mister X used: Boat")
    else:
        busmovement()


##Saves all the countries in a variable. Mister X flies then randomly to one of all those countries on the list.
def planemovement():
    global currentLocation
    planedestinations = flydestination(currentLocation)

    index = random.randint(0, len(planedestinations) - 1)
    currentLocation = planedestinations[index]
    print("Mister X used: Plane")




##Depends on the chances Mister X can go by planes, bus or boat.
def xRandomMove():
    chance = random.randint(0, 10)
    global turns

    if turns % 3 == 0:
        positionReveal()

    if chance > 2:
        busmovement()
        turns = turns + 1
    elif chance == 0:
        planemovement()
        turns = turns + 1
    else:
        boatmovement()
        turns = turns + 1







spawnpoint()
xRandomMove()
xRandomMove()
xRandomMove()
xRandomMove()
xRandomMove()


