# this is a program that simulates a checkout for customers and gives them a reciept in the form of a txt file
import time, os, sys

# import dictionary for menu
from techWave import current_inventory

def clearScreen():
    os.system("clear")

def header():
    print("Tech Wave Components! Wavey Bro.")
    print("-"*45)

def printMenu():
    print("Menu")
    print("-"*45)
    for i in current_inventory:
        print(f"{i:<30}{current_inventory[i]:>10.2f}")

# this is a combo of all of the above functions
# it will keep the console clean as users use it
def transition():
    clearScreen()
    header()
    printMenu()

# ****************************************************************************

# loop per customer
response = "y"
while response == "y":
    clearScreen()
    total = 0

    transition()
    name = input("\nHello. Please enter your name : ")

    # Move cart lists here so they persist for the whole order
    customerCartItem = []
    customerCartPrice = []

    addItem = "y"
    while addItem == "y":
        transition()
        customerChoice = input("\nPlease make a selection : ").title()

        # validate that input from customer is in dictionary
        if customerChoice in current_inventory:
            transition()
            print()
            price = current_inventory[customerChoice]
            total += price
            customerCartItem.append(customerChoice)
            customerCartPrice.append(price)
            print(f"{customerChoice} added! Current total is ${total:.2f}")    
        else:
            print("Sorry. That's not on the menu.")
        
        addItem = input("\nWould you like to add another item to your order? (Y/N) : ").lower()

    # calculate shipping
    shippingCost = 0.00

    if total < 50:
        shippingCost = 7.99
    elif total < 100:
        shippingCost = 4.99
    else:
        shippingCost = 0.00

    # add shipping cost to total
    total = total + shippingCost

    # calculate tax at 7%
    total = total * 1.07
# *****************************************************
# create reciept

    os.chdir("/Users/shawnconboy/Desktop")

    reciept = open(f"techWave_reciept_{name}.txt" , "w")
    reciept.write("Welcome to Tech Wave!")
    reciept.write(f"\nHello {name}!")
    reciept.write(f"\n\nItems Purchased\n")
    reciept.write(f"{'-'*45}\n")
    for i in range(len(customerCartItem)):
        reciept.write(f"{customerCartItem[i]:<30}{customerCartPrice[i]:>10.2f}\n")
    reciept.write(f"{'-'*45}\n")
    reciept.write(f"\nYour total shipping cost is ${shippingCost:.2f}")
    reciept.write(f"\nYour total today is ${total:.2f}\n")
    reciept.write(f"{'-'*45}\n")
    reciept.write(f"\nThank you. Come again!")
    reciept.close()

    transition()
    response = input("\nWould you like to start another order? (Y/N) : ")

transition()
print("\nProgram ended. Thank you.")

time.sleep(1)
sys.exit()