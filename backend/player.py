from database import *

currentLocation = ""

planes = 1
boats = 5
bus = 10
turns = 16
money = 100


def spawnpoint(): ##Setting current location of player with the method getOneCountry()
    global currentLocation
    currentLocation = getOneCountry()
    print(f"You were spawned in: {currentLocation}")


def positionReveal(): ##It reveals Player location
    print("You are currently in " + currentLocation)
    return currentLocation


def checkbus(): ## Checks if bus can be used by checking if the neigh. countries list is empty or not.
    global currentLocation
    ncountrylist = neighbourcountries(currentLocation)  ##Saving in variable return value of neighbourcountries() function.
    if ncountrylist:
        return True
    else:
        return False

def checkboat(): ## Check if the boat can be used by checking if the country has shared sea with different countries.
    global currentLocation
    sharedsealist = countrysea(currentLocation)  ##Saves in variable the return value of countrysea() function.
    if sharedsealist:
        return True
    else:
        return False




## Player bus function.
def busmovement():
    global currentLocation
    ncountrylist = neighbourcountries(currentLocation) ##Saving in variable return value of neighbourcountries() function.
    destination = input("Which country would you like to travel to by bus? Type: 'Show Options' for help.\n")

    ## Sets as new location the destination player types in case it is one of the neigh. countries.
    if destination in ncountrylist:
        currentLocation = destination
    ## Prints all the possible options to travel by bus from current location
    elif destination == "Show Options":
        print("Options to travel by bus from " + currentLocation + ": " + str(ncountrylist))
        busmovement()
    else:
        ## Error message in case destination doesnt exists.
        print("Is not possible to travel to " + destination + " from " + currentLocation)
        busmovement()


## Player boat function.
def boatmovement():
    global currentLocation
    sharedsealist = countrysea(currentLocation) ##Saves in variable the return value of countrysea() function.
    destination = input("How far do you want to sail by boat? Type: 'Show Options' for help.\n")

    ## Sets as new location the destination player types in case the destination shares same sea.
    if destination in sharedsealist:
        currentLocation = destination
    ## Prints all the possible options to travel by boat from current location
    elif destination == "Show Options":
        print("Options to travel by boat from " + currentLocation + ": " + str(sharedsealist))
        boatmovement()
    else:
        ## Error message in case destination doesnt exists.
        print("You can't travel from " + currentLocation + " to " + destination + " by boat.")
        boatmovement()


## Player plane function
def planemovement():
    global currentLocation
    planedestinations = flydestination(currentLocation)
    destination = input("Where do you want to fly by plane? ")

    ## Sets as new location the destination player types in case the destination exists.
    if destination in planedestinations:
        currentLocation = destination
    else:
    ## Error message in case destination doesnt exists.
        print(destination + " doesn't exist. Try again!")
        planemovement()



## Player movement options
def moves():
    global bus, boats, planes, turns
    vehicle = input(f"What vehicle do you want to use? Tickets: Bus: {bus}, Boat: {boats}, Plane: {planes}.\n")

    ## In case player want to use bus
    if vehicle.lower() == "bus":
        ## Checks if players has enough tickets.
        if bus > 0:
           ## In case bus can be used, executes bus function and player loses one turn and one bus ticket.
           if checkbus():
              busmovement()
              bus = bus - 1
              turns = turns - 1
           ## Error message in case is not possible to use bus
           else:
              print("You can't use Bus from " + currentLocation)
              moves()
        ## Error msg in case player didn't have enough tickets
        else:
            print("You dont have anymore bus tickets!")
            moves()

    ## In case player want to use boat
    elif vehicle.lower() == "boat":
        ## Checks if players has enough tickets.
        if boats > 0:
           ## In case boat can be used, executes boat function and player loses one turn and one boat ticket.
           if checkboat():
              boatmovement()
              boats = boats - 1
              turns = turns - 1
           ## Error message in case is not possible to use boat.
           else:
              print("You can't travel by Boat from " + currentLocation)
              moves()
        ## Error msg in case player didn't have enough tickets
        else:
            print("You don't have anymore boat tickets! Try another vehicle!")
            moves()

    ## In case player want to use plane
    elif vehicle.lower() == "plane":
        ## Checks if players has enough tickets.
        if planes > 0:
           planemovement()
           planes = planes - 1
           turns = turns - 1
        ## Error msg in case player didn't have enough tickets
        else:
           print("You have 0 plane tickets left!")
           moves()
     ## Error message in case player types something different that Bus, Boat or Plane.
    else:
        print("Travel is ONLY possible by bus, boat or plane. Please try again!!")
        moves()


def getMoney():
    return money





