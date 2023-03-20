import os
from battleship_player import Player

def setup():
    os.system('cls')
    p1Name = input("What is the name of Player 1? ")
    p1 = Player(p1Name)
    grid_setup(p1)
    
    os.system('cls')
    p2Name = input("What is the name of Player 2? ")
    p2 = Player(p2Name)
    grid_setup(p2)
    
    return p1, p2

def grid_setup(player):
    battleships = {
        "Aircraft": ["A"] * 5,
        "Battleship": ["B"] * 4,
        "Cruiser": ["C"] * 3,
        "Submarine": ["S"] * 3,
        "Destroyer": ["D"] * 2
    }
    
    while len(battleships) > 0:
        os.system('cls')
        ship_chosen = ""
        while ship_chosen == "":
            print("Here are your remaining ships: \n")
            for i in battleships:
                print(f"{i}: {len(battleships[i])} spots\n")
            ship_chosen = input("Choose a ship to place on your grid: ")
            if ship_chosen not in battleships:
                os.system('cls')
                print("ERROR: Ship non-existent or already placed!")
                ship_chosen = ""
                input("Press enter to continue: ")
                os.system('cls')
        
        os.system('cls')
        rules = "These are the rules for ship placement:\n1. Ships can only be placed vertically and horizontally\n2. Ships cannot overlap\n3. Ships cannot be placed off the board\nIf you forget any of the placement rules, input 'RULES'"
        print(rules)
        input("Press enter to continue: ")
        os.system('cls')
        
        pos1 = ""
        while pos1 == "":
            print(player)
            pos1 = input(f"Choose the first position of your {ship_chosen} ({len(battleships[ship_chosen])} spots): ")
            if pos1 == "RULES":
                os.system('cls')
                print(rules)
                pos1 = ""
                input("Press enter to continue")
                os.system('cls')
            elif pos1 not in player.grid_pos:
                os.system('cls')
                print("ERROR: That is not a valid position!")
                pos1 = ""
                input("Press enter to continue: ")
                os.system('cls')
            
            if pos1 != "":
                check_pos1 = player.check_pos(pos1)
                if check_pos1 == False:
                    os.system('cls')
                    print("ERROR: Position overlaps with another ship!")
                    pos1 = ""
                    input("Press enter to continue: ")
                    os.system('cls')
            
            confirm_pos1 = ""
            while confirm_pos1 == "":
                os.system('cls')
                print(player)
                confirm_pos1 = input(f"First Position of {ship_chosen}: {pos1}\nInput 'Y' to confirm or 'N' to choose a different position: ")
                if confirm_pos1 == "N":
                    pos1 = ""
                elif confirm_pos1 != "Y":
                    os.system('cls')
                    print("ERROR: Enter a valid input")
                    confirm_pos1 = ""
                    input("Press enter to continue")
                
        os.system('cls')
        pos2 = ""
        while pos2 == "":
            print(player)
            pos2 = input(f"First Position of {ship_chosen}: {pos1}\nChoose the second position of your {ship_chosen} ({len(battleships[ship_chosen])} spots): ")
            if pos2 == "RULES":
                os.system('cls')
                print(rules)
                pos2 = ""
                input("Press enter to continue")
                os.system('cls')
            elif pos2 not in player.grid_pos:
                os.system('cls')
                print("ERROR: That is not a valid position!")
                pos2 = ""
                input("Press enter to continue: ")
                os.system('cls')
            
            if pos2 != "":
                place_prev = player.place(battleships[ship_chosen], ship_chosen, pos1, pos2)
                
                if place_prev == "N":
                    pos2 = ""
                elif place_prev != "":
                    os.system('cls')
                    print(place_prev)
                    input("Press enter to continue: ")
                    os.system('cls')
                    pos2 = ""
        
        battleships.pop(ship_chosen)
                


    