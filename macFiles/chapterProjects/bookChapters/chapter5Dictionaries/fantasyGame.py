import time, os, sys
def clearScreen():
    os.system("clear")
clearScreen()

# ***************************************************************
items = {"Arrow": 12,
         "Gold Coin": 42,
         "Dagger": 1,
         "Torch": 6,
         "Rope": 10}
itemCount = 0

print("Inventory : ")
for item in items:
    itemCount += items[item]
    print(f"{item} {items[item]}")

print(f"Total number of items : {str(itemCount)}")