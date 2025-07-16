import time, os, sys
from smoothies import menu

os.chdir("/Users/shawnconboy/Desktop")

def clearScreen():
    os.system("clear")

def header():
    print("Welcome to Sunny Smoothies!")
    print()

def printMenu():
    for i in menu:
        print(f"{i:<20}{menu[i]:>20}")
    print()

def transition():
    clearScreen()
    header()
    printMenu()

# customer loop
counter = 0
response = "y"
while response == "y":
    clearScreen()
    header()
    printMenu()

    total = 0
    
    addItem = "y"
    while addItem == "y":
        customerChoice = input("Please make a selection: ").title()

        if customerChoice in menu:
            transition()
            price = menu[customerChoice]
            total += price
            print(f"{customerChoice} added! Current total is ${total:.2f}")
            print()
        else:
            print("Item not on menu.")
        counter = counter + 1
        addItem = input("Would you like to add another item? (Y/N): ").lower()

    transition()
    print("Thank you for ordering.")
    print()
    print(f"Your total is ${total:.2f}")
    print()

    # create receipt
    receipt = open(f"Sunny_Smoothies_reciept_{counter}.txt", "w")
    receipt.write(f"Welcome to Sunny Smoothies!")
    receipt.write(f"\nYour total today is {total:.2f}.")
    receipt.write(f"\nThank you. Come again.")
    receipt.close()

    response = input("Would you like to start another order? (Y/N): ").lower()

print("Program ended. Thank you.")

time.sleep(1)
sys.exit()
