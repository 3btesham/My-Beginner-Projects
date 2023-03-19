game_on = True

class Player:
    def __init__(self, name):
        self.name = name
        self.grid = ["-"] * 100
        self.grid_pos = [f"{chr(65 + i // 10)}{i % 10 + 1}" for i in range(100)]
        
    def __repr__(self):
        letters = "ABCDEFGHIJ"
        battlefield = "  "
        for i in range(11):
            if i == 0:
                for num in range(1, 11):
                    if num == 10:
                        battlefield += str(num) + "\n"
                    else:
                        battlefield += str(num) + " "
            else:
                for row in range(11):
                    if row == 0:
                        battlefield += f"{letters[i - 1]} "
                    elif row == 10:
                        battlefield += self.grid[(i - 1) * 10 + (row - 1)] + "\n"
                    else:
                        battlefield += self.grid[(i - 1) * 10 + (row - 1)] + " "
    
        return battlefield
    
    def grid_pos_to_num(self, pos):
        return self.grid_pos.index(pos)
    
    def check_pos(self, pos):
        pos = self.grid_pos_to_num(pos)
        if self.grid[pos] == "-":
            return True
        else:
            return False
    
    def place(self, ship, pos1, pos2):
        pos1 = self.grid_pos_to_num(pos1)
        pos2 = self.grid_pos_to_num(pos2)
        ship_len = len(ship)
        
        if abs(pos2 - pos1) != ship_len - 1 and abs(pos2//10 - pos1//10) != ship_len - 1:
            return "ERROR: Position is too long or short"
        
        if abs(pos2 - pos1) == ship_len - 1:
            placer = min(pos1, pos2)
            for i in range(len(ship)):
                if self.grid[placer] == "-":
                    self.grid[placer] = ship[i]
                    placer += 1
                else:
                    placer = min(pos1, pos2)
                    for i in range(len(ship)):
                        if self.grid[placer] == ship[i]:
                            self.grid[placer] = "-"
                            placer += 1
                    return "ERROR: Position overlaps with another ship"
            
            confirm = ""
            while confirm == "":
                print(self)
                confirm = input("Input 'Y' to confirm or 'N' to choose a different position: ")
                if confirm == "N":
                    placer = min(pos1, pos2)
                    for i in range(len(ship)):
                        if self.grid[placer] != "-":
                            self.grid[placer] = "-"
                            placer += 1
                    return "N"
                elif confirm == "Y":
                    return ""
                else:
                    print("ERROR: Enter a valid input")
                    input("Press enter to continue: ")
                
        elif abs(pos2//10 - pos1//10) == ship_len - 1:
            placer = min(pos1, pos2)
            for i in range(len(ship)):
                if self.grid[placer] == "-":
                    self.grid[placer] = ship[i]
                    placer += 10
                else:
                    placer = min(pos1, pos2)
                    for i in range(len(ship)):
                        if self.grid[placer] == ship[i]:
                            self.grid[placer] = "-"
                            placer += 10
                    return "ERROR: Position overlaps with another ship"
                
            confirm = ""
            while confirm == "":
                print(self)
                confirm = input("Input 'Y' to confirm or 'N' to choose a different position: ")
                if confirm == "N":
                    placer = min(pos1, pos2)
                    for i in range(len(ship)):
                        if self.grid[placer] != "-":
                            self.grid[placer] = "-"
                            placer += 10
                    return "N"
                elif confirm == "Y":
                    return ""
                else:
                    print("ERROR: Enter a valid input")
                    input("Press enter to continue: ")
                
def setup():
    p1Name = input("What is the name of Player 1? ")
    p1 = Player(p1Name)
    grid_setup(p1)
    
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
        print("Here are your remaining ships: \n")
        for i in battleships:
            print(f"The {i} fills up {len(battleships[i])} spots\n")
        input("Press enter to continue: ")
        
        ship_chosen = ""
        while ship_chosen == "":
            print(player)
            ship_chosen = input("Choose a ship to place on your grid: ")
            if ship_chosen not in battleships:
                print("ERROR: Ship non-existent or already placed!")
                ship_chosen = ""
                input("Press enter to continue: ")
        
        rules = "These are the rules for ship placement:\nShips can only be placed vertically and horizontally!\nShips cannot overlap!\nShips cannot be placed off the board!\nIf you forget any of the placement rules, input 'RULES'"
        print(rules)
        input("Press enter to continue: ")
        
        pos1 = ""
        while pos1 == "":
            print(player)
            pos1 = input("Choose the first position of your ship: ")
            if pos1 == "RULES":
                print(rules)
                pos1 = ""
                input("Press enter to continue")
            elif pos1 not in player.grid_pos:
                print("ERROR: That is not a valid position!")
                pos1 = ""
                input("Press enter to continue: ")
            
            check_pos1 = player.check_pos(pos1)
            if check_pos1 == False:
                print("ERROR: Position overlaps with another ship!")
                pos1 = ""
                input("Press enter to continue: ")
        
        pos2 = ""
        while pos2 == "":
            print(player)
            pos2 = input("Choose the second position of your ship: ")
            if pos2 == "RULES":
                print(rules)
                pos2 = ""
                input("Press enter to continue")
            elif pos2 not in player.grid_pos:
                print("ERROR: That is not a valid position!")
                pos2 = ""
                input("Press enter to continue: ")
                
            place_prev = player.place(battleships[ship_chosen], pos1, pos2)
            
            if place_prev == "N":
                pos2 = ""
            elif place_prev != "":
                print(place_prev)
                input("Press enter to continue: ")
                pos2 = ""
        
        battleships.pop(ship_chosen)
                    
def game_play(p1, p2):
    global game_on
    while game_on == True:
        pass
        
def battleship():
    p1, p2 = setup()
    game_play(p1, p2)
    input()

battleship()

    