import time, os, sys

def printMenu():
    os.system("clear")
    print("\nWelcome To The Smoothie Shack!")
    print("-"*40)
    print("1 -- Tropical Blast              $4.99")
    print("2 -- Pineapple Oasis             $4.99")
    print("3 -- Orange Passion              $4.99")
    print("4 -- Guava Surprise              $4.99")
    print("5 -- Chocolate Freeze            $4.99")
    print()

def getName():
    userName = input("Please enter your name : ")
    return userName

def takeOrder():
    userChoice = "y"
    subTotal = 0
    total = 0
    while userChoice.lower() == "y":
        selection = int(input("Enter your order number : "))
        if selection == 1:
            subTotal = 4.99
            total += subTotal
        elif selection == 2:
            subTotal = 4.99
            total += subTotal
        elif selection == 3:
            subTotal = 4.99 
            total += subTotal
        elif selection == 4:
            subTotal = 4.99
            total += subTotal
        elif selection == 5:
            subTotal = 4.99
            total += subTotal
        else:
            print("Invalid selection. Choose from 1 - 5 please.")
            continue
        userChoice = input("Would you like to add another item? (Y/N) : ")
        
    return total

def printTotal(userName,total):
    print(f"Hello {userName}, your total today is ${total:.2f}")






# ********************************************************************

printMenu()
userName = getName()
total = takeOrder()
printTotal(userName,total)
