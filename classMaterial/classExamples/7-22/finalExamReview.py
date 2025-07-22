# Import a dictionary called current_prices from the module softbank.py into your program. 
# Prompt the customer as to which robot they would like to purchase. 
# If they wish to acquire a 2-year warranty, add $500 to the price. 
# If they wish to acquire a lifetime warranty, add $1000 to the price. 
# In addition, ask the customer if they would like to purchase an online training package. If so, add $250 to the price. 
# If the customer is a healthcare professional, they receive a 20% discount. 
# Lastly, calculate 7% tax on the total amount (including the protection plan).

# Display to the user the price of their robot purchase. Include at least one type of input validation.

# Variation would be to create a text file for the invoice instead of displaying the total price on the console.

from softbank import current_prices

import time, os, sys

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printMenu():
    print("Menu")

    for i in current_prices:
        price = current_prices[i]
        print(f"{i:<15}                 ${price:.2f}")

response = 'y'

while response == 'y':
    total = 0

    clearScreen()
    name = input("Hello. What's your name? : ")

    isDoctor = input(f"Thank you. {name}, are you a health care professional? (Y/N) : ")


    print()
    print("Robot Sales LLC.")

    printMenu()

    addItem = "y"
    while addItem == "y":
        customerOrder = input("Which item would you like? : ")

        if customerOrder in current_prices:
            price = current_prices[customerOrder]
            total += price
            print(f"{customerOrder} added! Current total is ${total:.2f}")
            
            if isDoctor == 'y':
                total = total * 0.8

            insurance = input("\nWould you like to add insurance to your item? (Y/N) : ").lower()
            if insurance == "y":
                insurancePlan = input("Would you like a 2 year plan or lifetime? : ")
                if insurancePlan == "2 year":
                    insuranceCost = 500
                else:
                    insuranceCost = 1000
            else:
                print("\nOkay. If it breaks, I don't want to hear any excuses.")
        else:
            print("Item not found.")

        addItem = input("\nWould you like to add another item? (Y/N) : ")

        onlineTraining = input("\nHow about an online training package for $250? (Y/N) : ")

        if onlineTraining == 'y':
            total += 250
            print("\nOkay. We'll add that on.")
        else:
            print("\nYou're ballsy, huh?")

        total = total * 1.07

        print(f"\n{name}, your total today is going to be ${total:.2f}.")

    response = input("\nAnother Order? (Y/N) : ")
    
print("Program has ended.")
time.sleep(1)
sys.exit()