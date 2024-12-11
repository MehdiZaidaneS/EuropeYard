from database import *
import player

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
        ## Removes current player country location as possible option to travel.
        if player.currentLocation in ncountrylist:
           ncountrylist.remove(player.currentLocation)

        index = random.randint(0, len(ncountrylist) - 1)
        mxcurrentLocation = ncountrylist[index]
        print("- Mister X used: Bus")
    else:
        mxboatmovement()


## In case shared sea list has values, Mister X travels randomly to one of the shared sea countries.
## In case list is empty, calls busmovement() function.
def mxboatmovement():
    global mxcurrentLocation
    sharedsealist = countrysea(mxcurrentLocation) ##Saves in variable the return value of countrysea() function.

    if sharedsealist:
        ## Removes current player country location as possible option to travel.
        if player.currentLocation in sharedsealist:
           sharedsealist.remove(player.currentLocation)

        index = random.randint(0, len(sharedsealist) - 1)
        mxcurrentLocation = sharedsealist[index]
        print("- Mister X used: Boat")
    else:
        mxbusmovement()


##Saves all the countries in a variable. Mister X flies then randomly to one of those countries on the list.
def mxplanemovement():
    global mxcurrentLocation
    planedestinations = flydestination(mxcurrentLocation)

    ## Removes current player country location as possible option to fly
    if player.currentLocation in planedestinations:
       planedestinations.remove(player.currentLocation)

    index = random.randint(0, len(planedestinations) - 1)
    mxcurrentLocation = planedestinations[index]
    print("- Mister X used: Plane")



def xrandommove():
    chance = random.randint(0, 10)
    global turns

    ## Every 3 rounds Mister X location is revealed.
    if turns % 3 == 0:
        print("- Mister X is in " + mxcurrentLocation)

    ##Depends on the chances Mister X can go by planes, bus or boat.
    if chance > 2:
        mxbusmovement()
        turns = turns + 1
    elif chance == 0:
        mxplanemovement()
        turns = turns + 1
    else:
        mxboatmovement()
        turns = turns + 1


