import player
from player import *
from misterx import *
from instructions import *



def game():
    mxspawnpoint()
    spawnpoint()
    while player.turns > 0:
        xrandommove()
        moves()
        if mxpositionreveal() == positionReveal():
            print("Congratulations, you caught Mister X")
            break


def start():

    option = input("Welcome to European Yard! Choose one to continue: ['Play', 'Instructions', 'Exit']\n")

    if option == 'Play':
        game()

    elif option == 'Instructions':
        aboutgame()
        rules()

    elif option == 'Exit':
        print("Thank you for playing!")





start()