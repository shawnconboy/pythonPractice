import time, sys, os

# clears screen
def clearScreen():
    os.system("clear")

# makes menu
def menu():
    print("Shipping Cost Calculator")
    print("-" * 40)
    print("Type\t\tCost")
    print()
    for i in shippingType:
        cost = shippingType[i]
        print(f"{i}\t\t${cost}")

# dictionary for package types
shippingType = {5:7.40,
                6:7.70,
                7:8,
                9:13.75,
                10:19.30}


# ***********************************************************
# ***********************************************************
# main section


subTotal = 0
total = 0

# prime loop for purchases
response = "y".lower()
while response == "y":
    clearScreen()
    menu()

    # if user choice is not an integer value, program does not
    # move forward
    try:
        userChoice = int(input("What shipping type do you need? : "))
    except ValueError:
        print("Please enter a number from 5 to 10.")
        continue

    if userChoice in shippingType:
        price = shippingType[userChoice]
        subTotal += price
        print(f"\nYou chose {userChoice}.")
        print(f"Your balance is {subTotal}")
        insurance = input("\nWould you like to add insurance? (Y/N) : ").lower()

        if insurance == "y":
            if subTotal <= 50:
                subTotal += 2.20
            elif subTotal <= 100:
                subTotal = 2.45
            else:
                subTotal = 3

        total = subTotal

        print(f"\nYour final total is ${total}")

        response = input("\nWould you like to make another purchase? (Y/N) : ")
    else:
        print("Wrong choice. Try again.")
        continue