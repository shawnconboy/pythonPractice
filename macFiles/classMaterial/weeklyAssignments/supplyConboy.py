# This program is a basic kiosk that allows a user to buy kits needed for classes.
import time, sys, os

# Function declarations

# clears screen for either os. self explanatory
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# showMenu() prints output to the user so they can see a gui
def showMenu():
    print()
    print("SCC Book Inn")
    print("-"*30)
    print()

    print(f"1 -- Mechatronics Kit       $299")
    print(f"2 -- Nursing Kit            $99")
    print(f"3 -- Welding Kit            $699")
    print(f"4 -- Multimeter             $199")
    print(f"5 -- Culinary Kit           $250")

# getName is simple. Gets a name from user and returns name to the main program
def getName():
    print()
    name = input("Please enter your name : ")
    return name

# getKit() is similar to getName() this one lets the user pick their selection
# and returns that to the main program.
def getKit():
    while True:
        try:
            kitNeeded = int(input("\nEnter a selection to purchase (1-5): "))
            if kitNeeded >= 1 and kitNeeded <= 5:
                return kitNeeded
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")



# makeSelection() takes input from the console and assigns price based on that input
def makeSelection(kitNeeded):
    if kitNeeded == 1:
        price = 299
        print("Added Mechatronics Kit  $299")
        return price
    elif kitNeeded == 2:
        price = 99
        print("Added Nursing Kit       $99")
        return price
    elif kitNeeded == 3:
        price = 699
        print("Added Welding Kit       $699")
        return price
    elif kitNeeded == 4:
        price = 199
        print("Added Multimeter        $199")
        return price
    elif kitNeeded == 5:
        price = 250
        print("Added Culinary Kit      $250")
        return price
    else:
        print("Invalid choice.")
        return 0

# giveTrioDiscount takes the price given and applies half of if you're a trio member
def giveTrioDiscount(price):
    print()
    while True:
        inTrio = input("Are you in the TRIO program?(Y/N) : ")

        if inTrio.lower() == 'y' or inTrio.lower() == 'n':
            break
        else:
            print("Please enter Y or N.")
    
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
    while True:
        runAgain = input("Make another transaction? (Y/N): ")
        
        if runAgain.lower() == 'y':
            return runAgain  # Continue the main loop
        elif runAgain.lower() == 'n':
            print("\nProgram has ended.")
            time.sleep(2)
            sys.exit()
        else:
            print("Please enter Y or N.")



# Main Program *****************************************************************

# prime the loop
runAgain = 'y'

# begin the loop here, as long as runAgain equals 'y'
while runAgain.lower() == 'y':
    clearScreen()
    showMenu()
    name = getName()

    total = 0

    # nested loop to make multiple selections
    userChoice = "y"
    while userChoice.lower() == "y":
        selection = getKit()
        price = makeSelection(selection)
        total += price
        print()
        userChoice = input("Would you like to add another item?(Y/N) : ")

    #asks user for possible discounts, then continues to final price and output.
    total = giveTrioDiscount(total)
    finalPrice = chargeTax(total)
    printOutput(name, finalPrice)
    runAgain = getUserChoice()

time.sleep(2)