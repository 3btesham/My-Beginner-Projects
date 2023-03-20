import os

class Player:
    def __init__(self, name):
        self.name = name
        self.grid = ["-"] * 100
        self.attack_grid = ["-"] * 100
        self.grid_pos = [f"{chr(65 + i // 10)}{i % 10 + 1}" for i in range(100)]
        self.cruiser = 1
        self.aircraft = 1
        self.battleship = 1
        self.destroyer = 1
        self.submarine = 1
        self.attacked_waters = []
        
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
    
    def display_attack_grid(self):
        letters = "ABCDEFGHIJ"
        enemy_waters = "  "
        for i in range(11):
            if i == 0:
                for num in range(1, 11):
                    if num == 10:
                        enemy_waters += str(num) + "\n"
                    else:
                        enemy_waters += str(num) + " "
            else:
                for row in range(11):
                    if row == 0:
                        enemy_waters += f"{letters[i - 1]} "
                    elif row == 10:
                        enemy_waters += self.attack_grid[(i - 1) * 10 + (row - 1)] + "\n"
                    else:
                        enemy_waters += self.attack_grid[(i - 1) * 10 + (row - 1)] + " "
    
        return enemy_waters
    
    def grid_pos_to_num(self, pos):
        return self.grid_pos.index(pos)
    
    def check_pos(self, pos):
        pos = self.grid_pos_to_num(pos)
        if self.grid[pos] == "-":
            return True
        else:
            return False
    
    def place(self, ship, ship_name, pos1, pos2):
        letterpos1 = pos1
        letterpos2 = pos2
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
            
            os.system('cls')
            confirm = ""
            while confirm == "":
                print(self)
                confirm = input(f"First Position of {ship_name}: {letterpos1}\nSecond Position of {ship_name}: {letterpos2}\nInput 'Y' to confirm or 'N' to choose a different position: ")
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
                
            os.system('cls')
            confirm = ""
            while confirm == "":
                print(self)
                confirm = input(f"First Position of {ship_name}: {letterpos1}\nSecond Position of {ship_name}: {letterpos2}\nInput 'Y' to confirm or 'N' to choose a different position: ")
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
        
    def attack_enemy(self, enemy, pos):
        enemy.attacked_waters += pos
        pos = self.grid_pos_to_num(pos)
        result = enemy.grid[pos]

        
        if result == "-":
            enemy.grid[pos] = "M"
            self.attack_grid[pos] = "M"
            return "miss"
        else:
            enemy.grid[pos] = "H"
            self.attack_grid[pos] = "H"
        
            if enemy.grid.count("D") == 0 and self.destroyer == 1:
                self.destroyer -= 1
                return "Destroyer"
            elif enemy.grid.count("C") == 0 and self.cruiser == 1:
                self.cruiser -= 1
                return "Cruiser"
            elif enemy.grid.count("A") == 0 and self.aircraft == 1:
                self.aircraft -= 1
                return "Aircraft"
            elif enemy.grid.count("B") == 0 and self.battleship == 1:
                self.battleship -= 1
                return "Battleship"
            elif enemy.grid.count("S") == 0 and self.submarine == 1:
                self.submarine -= 1
                return "Submarine"
            else:
                return "hit"
