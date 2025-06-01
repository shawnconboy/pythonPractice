import time, sys, os

showList = ["The Office", "All American", "Mr.Robot", "Orange Is The New Black", "SWAT"]

while True:
    os.system("clear")

    print()
    print("Shows To Watch")
    print("-"*40)
    print()

    print(f"{"Title":<20}")
    print("-"*40)
    print()

    for i in showList:
        print(i)

    print()
    print("1 -- Add a show")
    print("2 -- Exit")
    print()

    choice = int(input("Choose an option : "))

    print()
    if choice == 1:
        newShow = input("Enter show name : ")
        showList.append(newShow)
    elif choice == 2:
        print("Program ended.")
        break

print()
time.sleep(5)