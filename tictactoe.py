# write your code here

# drawing the tic-tac-toe field filled with values
def draw_field(game_field):
    print("---------")

    for row in range(len(game_field)):
        print("| ", end="")

        for col in range(len(game_field[row])):
            if (col == len(game_field) - 1):
                print(f"{game_field[row][col]} |")
            else:
                print(f"{game_field[row][col]} ", end="")

    print("-------")


# filling tic-tac-toe field with values from the user input
def fill_field_with_values(game_field):
    count = 0

    for row in range(len(game_field)):
        for col in range(len(game_field[row])):
            game_field[row][col] = " "
            count += 1


def selecting_cells(game_field, count):
    mark = "X"
    if count % 2 == 0:
        mark = "O"

    while True:
        selection = str(input("Enter the coordinates: > "))
        selection = selection.split()
        if not selection[0].isnumeric() or (len(selection) > 1 and
                                            not selection[1].isnumeric()):
            print("You should enter numbers!")
            continue
        else:
            col = int(selection[0])
            row = int(selection[1])

        if col < 1 or row < 1 or col > 3 or row > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        col = col - 1
        row = 3 - row

        cell = game_field[row][col]
        if(cell != " "):
            print("This cell is occupied! Choose another one!")
            continue
        else:
            game_field[row][col] = mark
            draw_field(game_field)
            break


def check_results(game_field):
    for i in range(2):
        mark = "X"
        if i == 1:
            mark = "O"

        cells_rows = {'row1': [game_field[0][0], game_field[0][1], game_field[0][2]],
                 'row2': [game_field[1][0], game_field[1][1], game_field[1][2]],
                 'row3': [game_field[2][0], game_field[2][1], game_field[2][2]]}

        for row_name, rows in cells_rows.items():
            count = 0
            for cell in rows:
                if cell == mark:
                    count += 1
                    if count == 3:
                        result = f"{mark} wins"
                        print(result)
                        return result
                    continue

        cells_columns = {'col1': [game_field[0][0], game_field[1][0], game_field[2][0]],
                         'col2': [game_field[0][1], game_field[1][1], game_field[2][1]],
                         'col3': [game_field[0][2], game_field[1][2], game_field[2][2]]}

        for col_name, columns in cells_columns.items():
            count = 0
            for cell in columns:
                if cell == mark:
                    count += 1
                    if count == 3:
                        result = f"{mark} wins"
                        print(result)
                        return result
                    continue

        cells_diagonals = {'diag1': [game_field[0][0], game_field[1][1], game_field[2][2]],
                           'diag2': [game_field[2][0], game_field[1][1], game_field[0][2]]}

        for diag_name, diagonals in cells_diagonals.items():
            count = 0
            for cell in diagonals:
                if cell == mark:
                    count += 1
                    if count == 3:
                        result = f"{mark} wins"
                        print(result)
                        return result
                    continue
    return "undefined"


def start_game():
    field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    fill_field_with_values(field)
    draw_field(field)
    global result
    for i in range(1, 10):
        selecting_cells(field, i)
        result = check_results(field)
        if "wins" in result:
            break

    if result == "undefined":
        print("Draw")


start_game()
