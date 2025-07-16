import time, sys, os

os.system("clear")

allGuest = {"Sydney": {"Apples": 21, "Pies": 3},
            "Carmen": {"JuiceBox": 9, "Chips": 15},
            "Joanne": {"Pizza": 5, "Pies": 19}}

def totalBought(guest, item):
    numBought = 0
    for k, v in guest.items():
        numBought += v.get(item, 0)
    return numBought

print("Number of things being brought: \n")
print(f"- Apples            {str(totalBought(allGuest, "Apples"))}")
print(f"- Pies              {str(totalBought(allGuest, "Pies"))}")
print(f"- Juice Boxes       {str(totalBought(allGuest, "JuiceBox"))}")
print(f"- Pizza             {str(totalBought(allGuest, "Pizza"))}")
