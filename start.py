from player import *
from misterx import *




def start():

    print("Welcome to European Yard!")
    mxspawnpoint()
    spawnpoint()
    while turns > 0:
        xrandommove()
        moves()
        if mxpositionreveal() == positionReveal():
            print("You caught Mx")
            break

















start()