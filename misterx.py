import random
from database import *

mxcurrentLocation = ""
turns = 1


def mxspawnpoint(): ##Setting current location of Mister X with the method getOneCountry()
    global mxcurrentLocation
    mxcurrentLocation = getOneCountry()


def mxpositionreveal(): ##It reveals Mister X position
    return mxcurrentLocation

## In case neighbour country list is not empty, Mister X travels randomly to one of the neigh.countries.
## In case it is empty, calls boatmovement() function.
def mxbusmovement():
    global mxcurrentLocation
    ncountrylist = neighbourcountries(mxcurrentLocation) ##Saving in variable return value of neighbourcountries() function.

    if ncountrylist:
        index = random.randint(0, len(ncountrylist) - 1)
        mxcurrentLocation = ncountrylist[index]
        print("- Mister X used: Bus")
    else:
        mxboatmovement()


## In case shared sea list is not empty, Mister X travels randomly to one of the shared sea countries.
## In case it is empty, calls busmovement() function.
def mxboatmovement():
    global mxcurrentLocation
    sharedsealist = countrysea(mxcurrentLocation) ##Saves in variable the return value of countrysea() function.

    if sharedsealist:
        index = random.randint(0, len(sharedsealist) - 1)
        mxcurrentLocation = sharedsealist[index]
        print("- Mister X used: Boat")
    else:
        mxbusmovement()


##Saves all the countries in a variable. Mister X flies then randomly to one of all those countries on the list.
def mxplanemovement():
    global mxcurrentLocation
    planedestinations = flydestination(mxcurrentLocation)

    index = random.randint(0, len(planedestinations) - 1)
    mxcurrentLocation = planedestinations[index]
    print("- Mister X used: Plane")



##Depends on the chances Mister X can go by planes, bus or boat.
def xrandommove():
    chance = random.randint(0, 10)
    global turns

    if turns % 3 == 0:
        print("- Mister X is in " + mxcurrentLocation)
    if chance > 2:
        mxbusmovement()
        turns = turns + 1
    elif chance == 0:
        mxplanemovement()
        turns = turns + 1
    else:
        mxboatmovement()
        turns = turns + 1


