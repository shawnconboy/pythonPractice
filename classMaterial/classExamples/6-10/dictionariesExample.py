import time, os, sys
os.system("clear")

items = {"Apple" : 1.90,
         "Carrots(Bag)" : 2.22,
         "Banana" : 1.15,
         "Cucumber" : 1.59,
         "Lettuce" : 1.96,
         "Onion" : 1.5}

def printMenu():
    print("The Store")
    print("-"*40)
    print("Available Items:")
    print("-" * 25)
    for item, price in items.items():
        print(f"{item:15} ${price:.2f}")
    print("-" * 25)

# *********************************************************
response = "y"

while response == "y":
    os.system("clear")
    printMenu()
    new = input("Would you like to place an order?(Y/N) : ")
    totalOrder = []
    moreItems = "y"

    while moreItems == 'y':
        itemName = input ('Enter produce to order: ')
        
        if itemName.lower() in items:
            print (f'{itemName} will cost ${items[itemName.lower()]:.2f}')
            buy = int(input ('How many would you like to buy ?'))
            subtotal = items[itemName.lower()]*buy
            totalOrder.append(subtotal)

        else:
            print("I don't have that item.")
        
        moreItems = input("Do you wish to purchase another item?(Y/N) : ")

    total = sum(totalOrder)
    tax = total *  0.09
    total += tax

    print(f"Your total cost is ${total:,.2f}")

    response = input("Make another purchase?(Y/N) : ")






time.sleep(3)
sys.exit()