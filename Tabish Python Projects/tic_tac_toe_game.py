#! /usr/bin/python3

from time import sleep as s

board = {"tl": "tl", "tm": "tm", "tr": "tr",
         "ml": "ml", "mm": "mm", "mr": "mr",
         "bl": "bl", "bm": "bm", "br": "br"}

not_finished = True
turn = 1
lst = ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"]

def show_board():
    print()
    print("       " , board["tl"], "|", board["tm"], "|", board["tr"])
    print("       " , "-----------")
    print("       " , board["ml"], "|", board["mm"], "|", board["mr"])
    print("       " , "-----------")
    print("       " , board["bl"], "|", board["bm"], "|", board["br"])
    print()

def put_in_board(inpu):
    global turn
    if inpu in lst:
        if turn % 2 == 0:  # True for player2
            board[inpu] = "O"
            show_board()
            print()
            if turn >= 5 and turn <= 9:
                con_list_check()
        else:  # True for player1
            board[inpu] = "X"
            show_board()
            print()
            if turn >= 5 and turn <= 9:
                con_list_check()
        lst.remove(inpu)
        turn += 1
    else:
        print("Invalid Input Try Again")

def con_list_check():

    global not_finished
    
    cond_list_O = [((board["tl"] == "O") and (board["ml"] == "O") and (board["bl"] == "O")), ((board["bl"] == "O") and (board["bm"] == "O") and (board["br"] == "O")), ((board["tr"] == "O") and (board["mr"] == "O") and (board["br"] == "O")), ((board["tl"] == "O") and (board["tm"] == "O") and (board["tr"] == "O")), ((
        board["tl"] == "O") and (board["mm"] == "O") and (board["br"] == "O")), ((board["tr"] == "O") and (board["mm"] == "O") and (board["bl"] == "O")), ((board["ml"] == "O") and (board["mm"] == "O") and (board["mr"] == "O")), ((board["tm"] == "O") and (board["mm"] == "O") and (board["bm"] == "O"))]

    cond_list_X = [((board["tl"] == "X") and (board["ml"] == "X") and (board["bl"] == "X")), ((board["bl"] == "X") and (board["bm"] == "X") and (board["br"] == "X")), ((board["tr"] == "X") and (board["mr"] == "X") and (board["br"] == "X")), ((board["tl"] == "X") and (board["tm"] == "X") and (board["tr"] == "X")), ((
        board["tl"] == "X") and (board["mm"] == "X") and (board["br"] == "X")), ((board["tr"] == "X") and (board["mm"] == "X") and (board["bl"] == "X")), ((board["ml"] == "X") and (board["mm"] == "X") and (board["mr"] == "X")), ((board["tm"] == "X") and (board["mm"] == "X") and (board["bm"] == "X"))]

    if turn % 2 == 0:
        if any(cond_list_O):
            print("CONGRATS",p2,"WON THE GAME")
            not_finished = False
            return

    else:
        if any(cond_list_X):
            print("CONGRATS",p1,"WON THE GAME")
            not_finished = False
            return 

print()
print("INSTRUCTIONS:")
print()
print("Below is the TIC TAC TOE board")
show_board()
print("Player has to enter the Value at which he wants to place his Mark")
print("The Value will be replaced by his Mark in the Board")
print("First Player to make a Straight line will Win the Game")
print()
p1 = input("Enter player 1 Name and your mark is X ").upper()
p2 = input("Enter player 2 Name and your mark is O ").upper()
print()
print("GET")
s(1)
print("SET")
s(1)
print("GO")
s(1)
show_board()

while not_finished:
    if turn > 9:
        print("IT\'S A DRAW")
        not_finished = False
        break
    else:
        if not_finished:
            if turn % 2 == 0:  # True for player2
                print(p2, "turn: ")
            else:  # True for player1
                print(p1, "turn: ")
            inpu = input().lower()
            put_in_board(inpu)
        else:
            print("PROCESS FINISHED")

print()
print()
