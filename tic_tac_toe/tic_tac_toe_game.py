import os


game_state = None


def game_setup():
    player1, symbol1, player2, symbol2 = select_players()
    grid_size = input("Enter a grid size (determines the # of rows/columns): ")
    while grid_size.isnumeric() == False:
        print("ERROR: Enter an integer for the grid size")
        grid_size = input("Enter a grid size (determines the # of rows/columns): ")

    grid_size = int(grid_size)

    while grid_size % 1 != 0:
        print("ERROR: Enter an integer for the grid size")
        grid_size = input("Enter a grid size (determines the # of rows/columns): ")

    while grid_size < 3:
        os.system("cls")
        print("ERROR: Enter a grid size greater than 3")
        grid_size = input("Enter a grid size (determines the # of rows/columns): ")

    values = setup_values(grid_size)
    start_grid = create_grid(grid_size, values)
    os.system("cls")
    print(f"Player {symbol1} is {player1}\n"
          f"Player {symbol2} is {player2}")
    print(start_grid)
    return grid_size, player1, symbol1, player2, symbol2, values


def setup_values(number):
    num_of_rows = number
    values = []
    row = []
    for row_num in range(1, num_of_rows ** 2 + 1):
        if row_num == num_of_rows:
            row += ["-"]
            values += [row]
            row = []
            num_of_rows += number
        else:
            row += ["-"]
    return values


def select_players():
    player1 = input("What is the name of player 1? ")
    symbol1 = input("What symbol do you want to use? ")
    while len(symbol1) != 1:
        print("ERROR: The symbol must be a singular character")
        symbol1 = input("What symbol do you want to use? ")
    os.system("cls")

    player2 = input("What is the name of player 2? ")
    symbol2 = input("What symbol do you want to use? ")
    while symbol2 == symbol1:
        print("ERROR: You must use a different symbol from player 1")
        symbol2 = input("What symbol do you want to use? ")
    while len(symbol2) != 1:
        print("ERROR: The symbol must be a singular character")
        symbol2 = input("What symbol do you want to use? ")

    os.system('cls')
    return player1, symbol1, player2, symbol2


def create_grid(rows, ttc_values):
    grid = ""
    for row in range(rows):
        for box in range(rows):
            if box != rows - 1:
                grid += " " + ttc_values[row][box] + " |"
            else:
                grid += " " + ttc_values[row][box] + " "
        if row != rows - 1:
            grid += "\n" + "-" * (rows * 3 + rows - 1) + "\n"
    return grid


def tic_tac_toe(rows, player1, symbol1, player2, symbol2, values):
    global game_state
    grid = values
    used_values = []
    while game_state == None:
        player1_turn = input(f"{player1} enter a # from 1 to {rows ** 2}: ")
        while player1_turn.isnumeric() == False:
            print("ERROR: Enter an integer for the number!")
            player1_turn = input(f"{player1} enter a # from 1 to {rows ** 2}: ")

        player1_turn = int(player1_turn)

        while player1_turn % 1 != 0:
            print("ERROR: Enter an integer for the number!")
            player1_turn = input(f"{player1} enter a # from 1 to {rows ** 2}: ")

        while int(player1_turn) < 1 or int(player1_turn) > (rows ** 2):
            print("ERROR: Enter a number within the range!")
            player1_turn = input(f"{player1} enter a # from 1 to {rows ** 2}: ")

        while player1_turn in used_values:
            print("ERROR: That spot is already filled!")
            player1_turn = int(input(f"{player1} enter a # from 1 to {rows ** 2}: "))

        player1_turn = int(player1_turn)

        used_values += [player1_turn]
        pos = player1_turn - 1
        grid[pos // rows][pos % rows] = symbol1
        os.system("cls")
        print(create_grid(rows, grid))
        win_lose_tie(symbol1, rows, player1, grid)

        if game_state == None:
            player2_turn = input(f"{player2} enter a # from 1 to {rows ** 2}: ")

            while player2_turn.isnumeric() == False:
                print("ERROR: Enter an integer for the number!")
                player2_turn = input(f"{player2} enter a # from 1 to {rows ** 2}: ")

            player2_turn = int(player2_turn)

            while player2_turn % 1 != 0:
                print("ERROR: Enter an integer for the number!")
                player2_turn = input(f"{player2} enter a # from 1 to {rows ** 2}: ")

            while int(player2_turn) < 1 and int(player2_turn) > rows ** 2:
                os.system("cls")
                print("ERROR: Enter a number within the range!")
                player2_turn = input(f"{player2} enter a # from 1 to {rows ** 2}: ")

            while player2_turn in used_values:
                print("ERROR: That spot is already filled!")
                player2_turn = int(input(f"{player2} enter a # from 1 to {rows ** 2}: "))

            used_values += [player2_turn]
            pos = player2_turn - 1
            grid[pos // rows][pos % rows] = symbol2
            os.system("cls")
            print(create_grid(rows, grid))
            win_lose_tie(symbol2, rows, player2, grid)


def win_lose_tie(symb, rows, player, values):
    global game_state
    Ldiagonal = []
    Ldiagonal_pos = 0
    Rdiagonal = []
    Rdiagonal_pos = rows - 1
    full_rows = 0
    for row in values:
        if row.count(symb) == rows:
            game_state = True
            print(f"{player} has won the game!")

    for row in values:
        Ldiagonal += [row[Ldiagonal_pos]]
        if Ldiagonal.count(symb) == rows:
            game_state = True
            print(f"{player} has won the game!")
        elif Ldiagonal_pos < rows:
            Ldiagonal_pos += 1

    for row in values:
        Rdiagonal += [row[Rdiagonal_pos]]
        if Rdiagonal.count(symb) == rows:
            game_state = True
            print(f"{player} has won the game!")
        elif Rdiagonal_pos > 0:
            Rdiagonal_pos -= 1

    for vertical_pos in range(rows):
        vertical = []
        for row in values:
            vertical += row[vertical_pos]
        if vertical.count(symb) == rows:
            game_state = True
            print(f"{player} has won the game!")

    for row in values:
        if row.count("-") == 0:
            full_rows += 1

    if full_rows == rows and game_state == None:
        game_state = False
        print(f"The game is a tie!")


def main():
    rows, player1, symbol1, player2, symbol2, values = game_setup()
    tic_tac_toe(rows, player1, symbol1, player2, symbol2, values)
    input()


main()