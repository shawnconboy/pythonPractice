# this is a program to simulate a breakfast kiosk
import time, os, sys

os.system("clear")

# dictionary with items and prices
itemList = {"Specialty Donut": 1.50,
            "Bagel": 3.15,
            "Croissant": 2.98,
            "English Muffin": 1.75,
            "Coffee": 2.99,
            "Juice": 1.99}

def menu():
    os.system("clear")
    print("SCC Student Hub")
    print("-"*50)
    print()
    print(f"{'Item':<25}{'Price':>20}")
    print("-"*50)
    for item in itemList:
        print(f"{item:<25}{itemList[item]:>20.2f}")

# main loop per order
response = "y".lower()

while response == "y":
    # show menu
    menu()

    # initialize order total
    total = 0.0

    # nested loop to add multiple items
    addItem = "y"
    while addItem == "y":
        userChoice = input("\n\tWhat would you like to purchase? : ").title()

        if userChoice in itemList:
            price = itemList[userChoice]
            total += price
            print(f"\tAdded {userChoice} (${price:.2f}) to your order.")
            print(f"\n\tCurrent sub-total is ${total:.2f}")
        else:
            print(f"\t'{userChoice}' is not on the menu.")

        addItem = input("\n\tWant to add another item? (Y/N) : ").lower()

    total *= 1.09
    
    print("-"*50)
    print(f"\n\tTotal is ${total:.2f}")
    print("\n\tThank you for your purchase!")
    print("-"*50)
    print()

    response = input("Would you like to make another order? (Y/N) : ").lower()

# exited loop, final output
menu()
print("\n\tThank you. Come again.")

time.sleep(2)
sys.exit()
