# program made to simulate checkout at tire shop.

# thanks for being a great professor. Truly, the best so far. -Shawn

# grabs menu from tires.py
from tires import tire_prices

import os, sys, time

# clears screen for cleanliness
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# simply print menu by using "printMenu()"
def printMenu():
    print("\nAmerican Tire Co.\n")

    for i in tire_prices:
        price = tire_prices[i]
        print(f"{i:<30}         ${price:.2f}")

# begin loop here per customer
response = "y"

while response == "y":
    clearScreen()
    # reset totals per customer
    total = 0
    tirePrice = 0
    totalDiscounts = 0
    discount = 0.00

    # grab user data
    name = input("Please enter your name : ").title()
    isVeteran = input("Are you a veteran? (Y/N) : ").lower()
    isMedical = input("Are you a first responder? (Y/N) : ").lower()
    isSenior = input("Are you a senior(over 65)? (Y/N) : ").lower()

    printMenu()

    # pull from menu
    tireChoice = input("\nWhich tire would you like to purchase? : ").title().strip()
    if tireChoice in tire_prices:
        tirePrice = tire_prices[tireChoice]
        print(f"{tireChoice} in cart. Current total is {tirePrice:.2f}")
    else:
        while tireChoice not in tire_prices:
            print(f"\n{tireChoice} is not on the menu.")
            tireChoice = input("Please enter a valid tire from the menu: ").title().strip()
        tirePrice = tire_prices[tireChoice]
        print(f"{tireChoice} in cart. Current total is {tirePrice:.2f}")

    quantity = int(input("How many would you like to purchase? : "))
    total = tirePrice * quantity
    print(f"{quantity} added to cart. Total is now {total:.2f}")

    if isSenior == "y":
        discount = 0.04

    if isMedical == "y":
        discount =  0.06

    if isVeteran == "y":
        discount = 0.07

    if totalDiscounts > 1:
        discount = 0.07

    total = total - (total * discount)

    addAlignment = input("Would you like to add an alignment(Y/N)? : ").lower()

    if addAlignment == "y":
        total += 150

    total = total * 1.07


    print(f"Your total today is {total:.2f}")

    response = input("Would you like to make another purchase? (Y/N) : ")

print("\nProgram ended. Thank you.")
time.sleep(1)
sys.exit()