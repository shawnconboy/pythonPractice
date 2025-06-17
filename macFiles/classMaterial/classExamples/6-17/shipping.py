import time, sys, os

# clears screen for Windows or Mac/Linux
def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

# makes menu
def menu():
    print("Shipping Cost Calculator")
    print("-" * 40)
    print("Type\t\tCost")
    print()
    for i in shippingType:
        print(f"{i}\t\t${shippingType[i]:.2f}")

# dictionary for package types
shippingType = {
    5: 7.40,
    6: 7.70,
    7: 8.00,
    9: 13.75,
    10: 19.30
}

# main loop for purchases
response = "y"
while response.lower() == "y":
    subTotal = 0
    total = 0

    clearScreen()
    menu()

    try:
        userChoice = int(input("\nWhat shipping type do you need? : "))
    except ValueError:
        print("Please enter a number from 5 to 10.")
        time.sleep(2)
        continue

    if userChoice in shippingType:
        price = shippingType[userChoice]
        subTotal += price
        print(f"\nYou chose type {userChoice}.")
        print(f"Your balance is ${subTotal:.2f}")

        insurance = input("\nWould you like to add insurance? (Y/N) : ").lower()

        if insurance == "y":
            if subTotal <= 50:
                subTotal += 2.20
            elif subTotal <= 100:
                subTotal += 2.45
            else:
                subTotal += 3.00
            print("Insurance has been added!")

        total = subTotal
        print(f"\nYour final total is ${total:.2f}")
    else:
        print("Wrong choice. Try again.")
        time.sleep(2)
        continue

    response = input("\nWould you like to make another purchase? (Y/N) : ")
