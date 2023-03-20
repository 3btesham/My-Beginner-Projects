import os
from battleship_game_setup import *
from battleship_player import *
from battleship_game_play import *

def battleship():
    p1, p2 = setup()
    os.system('cls')
    game_play(p1, p2)
    input()

battleship()