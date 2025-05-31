import time, sys, os

os.system("clear")

# This defines the dictionary to hold all the items
groceryList = []

while True:
    os.system("clear")
    print()
    print("Grocery List")
    print("-"*35)
    print()

    print(f"{"Item":<10}{"Price":>10}{"Quantity":>15}")
    print()
    for i in groceryList:
        print(f"{i["Item"]:<10}{i["Price"]:>10.2f} {i["Quantity"]:>14}")
    
    print()
    print()


    print("1 -- Add Item")
    print("2 -- Remove Item")
    print("3 -- Quit")
    print()

    selection = int(input("Make a selection : "))
    print()

    if selection == 1:
        name = input("Please enter item name : ")
        price = float(input("Please enter price : "))
        quantity = int(input("Please enter quantity : "))

        item = {"Item" : name,
                "Price" : price,
                "Quantity" : quantity}
        
        groceryList.append(item)
        print(f"Item added!")
        time.sleep(1)

    elif selection == 2:
        print("Please enter item to be deleted : ")

    elif selection == 3:
        print("Program ended.")
        time.sleep(3)
        sys.exit()

    else:
        selection = input("Invalid selection. Please choose a number from 1 - 3. : ")