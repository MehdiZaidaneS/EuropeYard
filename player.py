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
    print("You are currently in " + currentLocation)
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
    destination = input("Which country would you like to travel to by bus? ")
    if destination in ncountrylist:
        currentLocation = destination
    else:
        print("Is not possible to travel to " + destination + " from " + currentLocation)
        busmovement()



def boatmovement():
    global currentLocation
    sharedsealist = countrysea(currentLocation) ##Saves in variable the return value of countrysea() function.

    destination = input("How far do you want to sail by boat? ")
    if destination in sharedsealist:
        currentLocation = destination
    else:
        print("You can't travel from " + currentLocation + " to " + destination + " by boat.")
        boatmovement()


def planemovement():
    global currentLocation
    planedestinations = flydestination(currentLocation)
    destination = input("Where do you want to fly by plane? ")

    if destination in planedestinations:
        currentLocation = destination
    else:
        print(destination + " doesn't exist. Try again!")
        planemovement()




def moves():
    global bus, boats, planes, turns
    vehicle = input(f"What vehicle do you want to use? Tickets: Bus: {bus}, Boat: {boats}, Plane: {planes}.\n")
    if vehicle.lower() == "bus":
        if bus > 0:
           if checkbus():
              busmovement()
              bus = bus - 1
              turns = turns - 1
           else:
              print("You can't use Bus from " + currentLocation)
              moves()
        else:
            print("You dont have anymore bus tickets!")
            moves()

    elif vehicle.lower() == "boat":
        if boats > 0:
           if checkboat():
              boatmovement()
              boats = boats - 1
              turns = turns - 1
           else:
              print("You can't travel by Boat from " + currentLocation)
              moves()
        else:
            print("You don't have anymore boat tickets! Try another vehicle!")
            moves()

    elif vehicle.lower() == "plane":
        if planes > 0:
           planemovement()
           planes = planes - 1
           turns = turns - 1
        else:
           print("You have 0 plane tickets left!")
           moves()
    else:
        print("Travel is ONLY possible by bus, boat or plane. Please try again!!")
        moves()






