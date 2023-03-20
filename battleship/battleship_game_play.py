import os
from battleship_player import *

game_on = True

def game_play(p1, p2):
    global game_on
    while game_on == True:
        os.system('cls')
        print(f"It is now {p1.name}'s turn!")
        input("Press enter to continue: ")
        
        turn(p1, p2)
        
        if p1.attack_grid.count("H") == 17:
            os.system('cls')
            print(f"{p1.name} has won the game!")
            game_on = False
            break

        os.system('cls')
        print(f"It is now {p2.name}'s turn!")
        input("Press enter to continue: ")
        
        turn(p2, p1)

        if p2.attack_grid.count("H") == 17:
            os.system('cls')
            print(f"{p2.name} has won the game!")
            game_on = False
            break

def turn(player, enemy):
    attack_pos = ""
    while attack_pos == "":
        os.system('cls')
        print(player.display_attack_grid())
        attack_pos = input(f"{player.name}, choose a position to attack or view your own board by inputting 'my board': ")
        if attack_pos == "my board":
            os.system('cls')
            print(player)
            attack_pos = ""
            input("Press enter to continue: ")
            os.system('cls')
        elif attack_pos not in player.grid_pos:
            os.system('cls')
            print(player.display_attack_grid())
            print("ERROR: This is not a valid position!")
            attack_pos = ""
            input("Press enter to continue: ")
            os.system('cls')
        elif attack_pos in enemy.attacked_waters:
            os.system('cls')
            print(player.display_attack_grid())
            print("ERROR: These waters have already been attacked!")
            attack_pos = ""
            input("Press enter to continue: ")
    
    player_attack = player.attack_enemy(enemy, attack_pos)
    
    if player_attack == "hit":
        os.system('cls')
        print(player.display_attack_grid())
        print("It was a hit!")
        input("Press enter to continue: ")
    elif player_attack == "miss":
        os.system('cls')
        print(player.display_attack_grid())
        print("It was a miss!")
        input("Press enter to continue: ")
    else:
        os.system('cls')
        print(player.display_attack_grid())
        print(f"You sunk their {player_attack}!!") 
        input("Press enter to continue: ")