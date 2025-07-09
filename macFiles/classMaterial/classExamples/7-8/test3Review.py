# program to create tickets for sparkle and shine

import time, os, sys, shutil, datetime

def clearScreen():
    os.system("clear")

# import dictionary from sparkle_car_wash.py
from Sparkle_Car_Wash import Services_Dict

currentDay = datetime.datetime.now()
formattedDate = currentDay.strftime("%B %d, %Y")
# B - month
# d - day
# Y - year

def header():
    print("Welcome to Sparkle Car Wash!")
    print("-"*40)

def menu():
    for i in Services_Dict:
        print(f"{i:<20}{Services_Dict[i]:>20}")

clearScreen()

os.chdir("/Users/shawnconboy/Desktop")

# **********************************
# main loop per customer
response = "y"

while response == "y":

    # create text file for receipt
    total = 0
    clearScreen()
    header()
    print()

    clearScreen()
    header()
    name = input("Please enter your name : ")
    print(f"\nHello {name}")
    print()
    menu()

    addItem = "y"

    while addItem == "y":

        print()
        customerOrder = input("What would you like to purchase? : ").title()

        print()

        if customerOrder in Services_Dict:
            price = Services_Dict[customerOrder]
            total += price
            print(f"Added {customerOrder} (${price}) to your order")
        else:
            print(f"{customerOrder} is not on the menu.")

        addItem = input("Would you like to add another? (Y/N) : ")

    # receipt here
    clearScreen()
    header()

    print(f"\tTotal is ${total:.2f}")
    print("\n\tThank you for your purchase!")
    print("-"*40)
    print()


    bill = open(f"sparkle_and_shine_{name}.txt", "w")
    bill.write(f"Hello {name}")
    bill.write(f"\nThanks for visiting Sparkle and Shine Car Wash today!")
    bill.write(f"\nToday is {str(formattedDate)}")
    bill.write(f"\nTotal is ${total:.2f}")
    bill.close()

    response = input("Start another order? (Y/N) : ")

print("Program ended. Thank you.")
time.sleep(1)
sys.exit()