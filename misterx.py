import random

planes = 1
boats = 5
busses = 10


def positionReveal():
    print("Mister X is in {country Name}")


def xRandomMove():
    chance = random.randint(0, 10)
    if chance > 2:
        print("Use bus")
    elif chance == 0:
        print("Use plane")
    else:
        print("Use boat")


xRandomMove()


