print("Welcome to Tic-Tac-Toe!")
#Player_X_name = input("Player X what is your name?: ")
#Player_O_name = input("Player O what is your name?: ")
game = {"A1":"1", "A2":"2", "A3":"3","B1":"4", "B2":"5", "B3":"6","C1":"7", "C2":"8", "C3":"9"}
win = False

def win_checker(player):
    global win
    if game["A1"] == game["B1"] == game["C1"]:
        print(f"{player} wins!")
        win = True
    elif game["A2"] == game["B2"] == game["C2"]:
        print(f"{player} wins!")
        win = True
    elif game["A3"] == game["B3"] == game["C3"]:
        print(f"{player} wins!")
        win = True
    elif game["A1"] == game["A2"] == game["A3"]:
        print(f"{player} wins!")
        win = True
    elif game["B1"] == game["B2"] == game["B3"]:
        print(f"{player} wins!")
        win = True
    elif game["C1"] == game["C2"] == game["C3"]:
        print(f"{player} wins!")
        win = True
    elif game["A1"] == game["B2"] == game["C3"]:
        print(f"{player} wins!")
        win = True
    elif game["A3"] == game["B2"] == game["C1"]:
        print(f"{player} wins!")
        win = True

def body():
    global win
    while win != True:
            while win != True:
                playerX_play = input("Player X, please enter your move in co-ordinates: ")
                if game[playerX_play] in ("O","X"):
                    print("That square is filled :(")
                else:
                    game[playerX_play] = "X"
                    win_checker("Player X")
                    break
            while win != True:
                playerO_play = input("Player O, please enter your move in co-ordinates: ")
                if game[playerO_play] in ("O","X"):
                    print("That square is filled :(")
                else:
                    game[playerO_play] = "O"
                    win_checker("Player O")
                    break

body()