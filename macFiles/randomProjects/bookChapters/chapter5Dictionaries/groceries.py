import time, sys, os

os.system("clear")

# This defines the dictionary to hold all the items
groceryList = [{"Item" : "Shoes", "Price" : 60.00, "Quantity" : 1}]

while True:
    os.system("clear")
    print()
    print("Shopping List")
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

    try:
        selection = int(input("Make a selection : "))
    except ValueError:
        print("Invalid selection. Please enter a number from 1 to 3.")
        time.sleep(2)
        continue

    print()

    if selection == 1:
        name = input("Please enter item name : ")
        name = name.capitalize()
        price = float(input("Please enter price : "))
        quantity = int(input("Please enter quantity : "))

        item = {"Item" : name,
                "Price" : price,
                "Quantity" : quantity}
        
        groceryList.append(item)
        print(f"Item added!")
        time.sleep(1)

    elif selection == 2:
            name = input("Enter item name to remove : ")
            found = False
            for item in groceryList:
                if item["Item"].lower() == name.lower():
                    groceryList.remove(item)
                    print(f"{name} removed!")
                    time.sleep(1)
                    found = True
                    break
            if not found:
                print(f"{name} not found in the list.")

    elif selection == 3:
        print("Program ended.")
        time.sleep(3)
        sys.exit()

    else:
        selection = input("Invalid selection. Please choose a number from 1 - 3. : ")