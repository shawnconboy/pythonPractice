import time, sys, os


def clearScreen():
    os.system("cls")

ticketPrices = {
    "child": 6.00,
    "teen": 8.00,
    "adult": 12.00,
    "senior": 7.00
}

theaterTypes = {
    "3d": 2.50,
    "imax": 4.00
}

def menu():
    print(f"Ticket Type\t\t\tPrice")
    print("-" * 40)
    for i in ticketPrices:
        print(f"{i}\t\t\t\t${ticketPrices[i]:.2f}")


response = "y"

while response == "y":
    subtotal = 0
    clearScreen()
    menu()
    
    userChoice = input("Please make a selection : ")

    if userChoice in ticketPrices:
        price = ticketPrices[userChoice]
        quantity = int(input(f"How many {userChoice} tickets would you like? : "))

        subtotal = price * quantity

        print(f"Your balance is {str(subtotal)}.")
    else:
        print("Did not find item.")

    response = input("\nWould you like to start another order? (Y/N) : ")

time.sleep(1)
sys.exit()