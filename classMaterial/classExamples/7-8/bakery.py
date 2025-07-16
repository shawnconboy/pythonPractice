import time, os, sys

from bakeryMenu import Bakery_Dict
# *********************************************************************************************************

def clearScreen():
    os.system("clear")

def header():
    print("Leah's Bake Shop")
    print("-"*20)

def printMenu():
    print("Menu")
    print("-"*45)
    for i in Bakery_Dict:
        print(f"{i:<30}{Bakery_Dict[i]:>10.2f}")

def transition():
    clearScreen()
    header()
    printMenu()

# *********************************************************************************************************

# loop per customer
response = "y"
while response == "y":
    clearScreen()
    total = 0

    transition()
    name = input("\nHello. Please enter your name : ")

    addItem = "y"
    while addItem == "y":
        transition()
        customerChoice = input("\nPlease make a selection : ").title()

        if customerChoice in Bakery_Dict:
            transition()
            print()
            price = Bakery_Dict[customerChoice]
            total += price
            print(f"{customerChoice} added! Current total is ${total:.2f}")    
        else:
            print("Sorry. That's not on the menu.")
        
        addItem = input("\nWould you like to add another item to your order? (Y/N) : ").lower()
    
    os.chdir("/Users/shawnconboy/Desktop")

    reciept = open(f"store_reciept_{name}.txt" , "w")
    reciept.write("Welcome to Leah's Bake Shop!")
    reciept.write(f"\nHello {name}!")
    reciept.write(f"\nYour total today is {total:.2f}")
    reciept.write(f"\nThank you. Come again!")
    reciept.close()

    transition()
    response = input("\nWould you like to start another order? (Y/N) : ")

transition()
print("\nProgram ended. Thank you.")

time.sleep(1)
sys.exit()