import time

name = input("Please enter your name : ")
age = int(input("Please enter your age : "))

if age < 18:
    print("Sorry. You must be older than 18 to adopt.")
else:
    liveInApartment = input("Do you live in an apartment? (Yes or No) : ").lower()

    if liveInApartment == "yes":
        petsAllowed = input("Are pets allowed? (Yes or No?) : ").lower()
        if petsAllowed == "no":
            print("Sorry. Your apartments do not allow pets. You can not adopt today.")
        else:
            currentPets = int(input("How many pets do you currently have? : "))
            if currentPets >= 3:
                print("Sorry. You already own too many pets.")
            else:
                print("You're eligible to adopt a pet!")
    else:
        currentPets = int(input("How many pets do you currently have? : "))
        if currentPets >= 3:
            print("Sorry. You already own too many pets.")
        else:
            print("You're eligible to adopt a pet!")
