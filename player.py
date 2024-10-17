from database import *

currentLocation = ""


planes = 1
boats = 5
bus = 10
turns = 16

def spawnpoint(): ##Setting current location of player with the method getOneCountry()
    global currentLocation
    currentLocation = getOneCountry()
    print(f"You were spawned in: {currentLocation}")


def positionReveal(): ##It reveals Player position
    print("Your location now is " + currentLocation)
    return currentLocation


def checkbus():
    global currentLocation
    ncountrylist = neighbourcountries(currentLocation)  ##Saving in variable return value of neighbourcountries() function.
    if ncountrylist:
        return True
    else:
        return False

def checkboat():
    global currentLocation
    sharedsealist = countrysea(currentLocation)  ##Saves in variable the return value of countrysea() function.
    if sharedsealist:
        return True
    else:
        return False





def busmovement():
    global currentLocation
    ncountrylist = neighbourcountries(currentLocation) ##Saving in variable return value of neighbourcountries() function.
    destination = input("What country do you want to go by bus? ")
    if destination in ncountrylist:
        currentLocation = destination
    else:
        print("Is not possible to travel to " + destination)
        busmovement()



def boatmovement():
    global currentLocation
    sharedsealist = countrysea(currentLocation) ##Saves in variable the return value of countrysea() function.

    destination = input("What country do you want to go by boat? ")
    if destination in sharedsealist:
        currentLocation = destination
    else:
        print("You cant travel from " + currentLocation + " to " + destination + " by boat.")
        boatmovement()


def planemovement():
    global currentLocation
    planedestinations = flydestination(currentLocation)
    destination = input("What country do you want to go by plane? ")

    if destination in planedestinations:
        currentLocation = destination
    else:
        print(destination + " doesnt exists")
        planemovement()




def moves():
    global bus, boats, planes, turns
    vehicle = input("What vehicle do you want to use? ")
    if vehicle.lower() == "bus":
        if bus > 0:
           if checkbus():
              busmovement()
              bus = bus - 1
              turns = turns - 1
              print("You can use " + str(bus) + " more busses")
           else:
              print("You cant use Bus from " + currentLocation)
              moves()
        else:
            print("You cant use anymore busses")
            moves()

    elif vehicle.lower() == "boat":
        if boats > 0:
           if checkboat():
              boatmovement()
              boats = boats - 1
              turns = turns - 1
              print("You can use " + str(boats) + " more boats")
           else:
              print("You cant use Boat from " + currentLocation)
              moves()
        else:
            print("You cant use anymore boats")
            moves()

    elif vehicle.lower() == "plane":
        if planes > 0:
           planemovement()
           planes = planes - 1
           turns = turns - 1
           print("You cant use planes anymore")
        else:
           print("You cant use anymore planes")
           moves()
    else:
        print("Only bus, boat or plane are allowed!")
        moves()






