import time, sys, os

os.system("clear")

board = {"topLeft" : " ", "topMiddle" : " ", "topRight" : " ",
         "midLeft" : " ", "midMiddle" : " ", "midRight" : " ",
         "bottomLeft" : " ", "bottomMiddle" : " ", "bottomRight" : " "}

def printBoard(board):
    print(board["topLeft"] + "|" + board["topMiddle"] + "|" + board["topRight"])
    print("-+-+-")

    print(board["midLeft"] + "|" + board["midMiddle"] + "|" + board["midRight"])
    print("-+-+-")

    print(board["bottomLeft"] + "|" + board["bottomMiddle"] + "|" + board["bottomRight"])


turn = "x"

for i in range(9):
    printBoard(board)
    move = input(f"Turn for {turn}. Move on which space? : ")
    board[move] = turn
    if turn == "x":
        turn = "o"
    else:
        turn = "x"
    os.system("clear")

print()
print("Game ended.")
print()
printBoard(board)
