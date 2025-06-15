import time, sys, os

def clearScreen():
    os.system("clear")

shoes = {"AF1": 100,
         "Jordan 3": 200,
         "Adidas": 150}

def menu():
    # user display
    print("Sole Providers")
    print()
    print(f"{"Shoe":<30}{"Price":>20}")
    print("-"*50)
    for shoe in shoes:
        price = shoes[shoe]
        print(f"{shoe:<30}{"$"+str(price):>20}")

def transition():
    time.sleep(0.5)
    clearScreen()
    menu()
    print()


# shop loop

response = "y"
while response == "y":
    subTotal = 0
    total = 0
    clearScreen()
    menu()
    addAnotherItem = "y"
    while addAnotherItem == "y":
        itemChoice = input("\nWhat item would you like? : ")
        price = shoes[itemChoice]
        
        transition()

        if itemChoice in shoes:
            print(f"{itemChoice} cost ${price}")
            addToCart = input(f"Add item to cart? (Y/N) : ").lower()

            transition()

            if addToCart == "y":
                total += price
                print(f"{itemChoice} added to cart!")

            else:
                print("That's okay. We can cancel the transaction.")
        # would you like another item? add to bill if yes.
            addAnotherItem = input("Do you want to make another selection? (Y/N) : ").lower()
        transition()
        # all done? Print total details
        print(f"Your current total is ${total}.")

    response = input("\nMove to next customer? (Y/N) : ").lower()

print("\nThank you. Come again.")
time.sleep(1)
sys.exit()

