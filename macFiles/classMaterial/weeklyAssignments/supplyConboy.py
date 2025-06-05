# This program is a basic kiosk that allows a user to buy kits needed for classes.
import time, sys, os

# Function declarations

# showMenu() prints output to the user so they can see a gui
def showMenu():
    print()
    print("SCC Book Inn")
    print("-"*30)
    print()

    print(f"1 -- Mechatronics Kit       {"$299"}")
    print(f"2 -- Nursing Kit            {"$99"}")
    print(f"3 -- Welding Kit            {"$699"}")
    print(f"4 -- Multimeter             {"$299"}")
    print(f"5 -- Culinary Kit           {"$250"}")

# getName is simple. Gets a name from user and returns name to the main program
def getName():
    print()
    name = input("Please enter name : ")
    return name

# getKit() is similar to getName() this one lets the user pick their selection
# and returns that to the main program.
def getKit():
    kitNeeded = int(input("Enter a selection to purchase(1-5) : "))
    return kitNeeded

# makeSelection() takes input from the console and assigns price based on that input
def makeSelection(kitNeeded):
    if kitNeeded == 1:
        price = 299
        return price
    elif kitNeeded == 2:
        price = 99
        return price
    elif kitNeeded == 3:
        price = 699
        return price
    elif kitNeeded == 4:
        price = 299
        return price
    elif kitNeeded == 5:
        price = 250
        return price
    else:
        print("Invalid choice.")

# giveTrioDiscount takes the price given and applies half of if you're a trio member
def giveTrioDiscount(price):
    print()
    inTrio = input("Are you in the TRIO program?(Y/N) : ")

    if inTrio.lower() == 'y':
        price = price * 0.5
    else:
        price = price

    return price

# chargeTax takes the current price after possible discounts and charges sales tax
def chargeTax(price):
    taxAmount = 0.07
    finalPrice = (price * taxAmount) + price

    return finalPrice

# prints output back to the user
def printOutput(name, price):
    print()
    print("*"*40)
    print()
    print(f"Hello {name}, your total is ${price:,.2f}.")
    print()

def getUserChoice():
    runAgain = input("Make another transaction?(Y/N) : ")

    if runAgain == "y":
        return runAgain
    else:
        print("Program has ended.")
        time.sleep(2)
        sys.exit()


# Main Program *****************************************************************

runAgain = 'y'

while runAgain.lower() == 'y':
    os.system("clear")
    showMenu()
    name = getName()

    total = 0
    userChoice = "y"

    while userChoice.lower() == "y":
        selection = getKit()
        price = makeSelection(selection)
        total += price
        print()
        userChoice = input("Would you like to add another item?(Y/N) : ")


    total = giveTrioDiscount(total)
    finalPrice = chargeTax(total)
    printOutput(name, finalPrice)
    runAgain = getUserChoice()

time.sleep(2)