import os, sys, time

os.system("clear")

birthdays = {"Alice" : "Jan 1", "Bob": "Apr 7", "Carol": "Jun 29"}

while True:
    name = input(f"Enter a name. (Blank to quit) : ")

    if name == '':
        print("Program ended.")
        time.sleep(2)
        break
    
    if name.lower() == "print list":
        print(birthdays)

    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}.")
    else:
        print(f"I do not have birthday information for {name}.")
        bday = input("When is their birthday? : ")
        birthdays[name] = bday
        print("Birthday database updated.")
        print()