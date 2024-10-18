from player import *
from misterx import *
from instructions import *




def start():

    print("Welcome to European Yard! Choose one to continue:\n"
          "['Play', 'Instructions', 'Exit']")

    option = input()
    if option == 'Play':
        mxspawnpoint()
        spawnpoint()
        while turns > 0:
            xrandommove()
            moves()
            if mxpositionreveal() == positionReveal():
                print("Congratulations, you caught Mister X")
                break

    elif option == 'Instructions':
        aboutgame()
        rules()

    elif option == 'Exit':
        print("Thank you for playing!")





start()