from player import *
from misterx import *
from instructions import *



## Logic of the game
def game():
    mxspawnpoint() ## MisterX spawns randomly.
    spawnpoint() ## Player spawns randomly.
    ## While player has turns, Mister X and the player move, until player location is the same as Mister X.
    while player.turns > 0:
        xrandommove()
        moves()
        if mxpositionreveal() == player.currentLocation:
            print("Congratulations, you caught Mister X!")
            break
        positionReveal()


def start():

    print("Welcome to European Yard!")
    option = "".lower()

    ## While player doesn't game will show the initial menu.
    while option != "play":
      option = input("Choose one to continue: ['Play', 'Instructions', 'Exit']\n").lower()

      ## Prints the text about game and the rules
      if option == 'instructions':
        aboutgame()
        rules()
      ## Game starts
      elif option == 'play':
          game()
          break
      ## Game ends
      elif option == 'exit':
        print("Thank you for playing!")
        break
      ## Error message in case the input doesn't exist
      else:
        print("Invalid input!")






start()