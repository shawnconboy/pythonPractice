#                                          ░▒▓██████▓▒░        ░▒▓██████▓▒░       ░▒▓███████▓▒░       ░▒▓███████▓▒░        ░▒▓██████▓▒░       ░▒▓█▓▒  ▒▓█▓▒░ 
#                                         ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░ 
#                                         ░▒▓█▓▒░             ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░ 
#                                         ░▒▓█▓▒░             ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓███████▓▒░       ░▒▓█▓▒  ▒▓█▓▒░       ░▒▓██████▓▒░  
#                                         ░▒▓█▓▒░             ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░         ░▒▓█▓▒░     
#                                         ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░         ░▒▓█▓▒░     
#                                          ░▒▓██████▓▒░        ░▒▓██████▓▒░       ░▒▓█▓▒  ▒▓█▓▒░      ░▒▓███████▓▒░        ░▒▓██████▓▒░          ░▒▓█▓▒░     
                                                                                                                   



# There's a lot to unpack here. it's mostly just styling.

# program will simulate hotel booking experience. have patience.

import time, os, sys, datetime, pyinputplus, pyautogui

# clear screen for different os(s)
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# transition to clean the console that i barely used.
def transition():
    clearScreen()
    print(f"The Grand Hotel Reservation System")
    print()




# Get today's date. Honestly. don't think i used this.
currentDate = datetime.date.today()

#print(currentDate)             tested to see if it worked



# ____________________________________________________________________________________________________________________________________

# main program begins here

# loops per "guest"
response = "y"

while response == "y":


    # some variable declarations because i was getting squigglies underneath without having them declared yet. 
    # this may very well be garbage code.
    # the total..... if you run multiple times, that may be good to reset at the start though......

    nightlyRate = 0
    totalNights = 0
    total = 0

    # get user information
    transition()
    time.sleep(0.1)
    name = input("Please enter your name : ")
    time.sleep(1)

    transition()
    print(f"Hello {name},")
    time.sleep(2)

    arrivalDate = pyinputplus.inputDate(
        "\nPlease enter your arrival date (yyyy-mm-dd) : ",
        formats=["%Y-%m-%d"]
    )

    time.sleep(1)
    clearScreen()

    print("The Grand Hotel Reservation System")

    print("\nThank you for that.")
    time.sleep(2)
    clearScreen()
    print("The Grand Hotel Reservation System")
    print(f"\nYour arrival date is {arrivalDate.strftime('%A, %B %d, %Y')}")
    time.sleep(2)
    departureDate = pyinputplus.inputDate(
        "\nPlease enter your departure date (yyyy-mm-dd) : ",
        formats=["%Y-%m-%d"]
    )
    time.sleep(1)
    clearScreen()
    print("The Grand Hotel Reservation System")
    print("\nThank you again,")
    time.sleep(2)

    clearScreen()
    print("The Grand Hotel Reservation System")

    print("\nHere's your summary for the days you've given.")
    time.sleep(1)
    print()

    # if/else to determine "peak" season

    if arrivalDate.month == 6:
        nightlyRate = 325
        print("\nPeak season rates apply!")
    else:
        nightlyRate = 250


    # calculate total due based on nights stayed
    totalNights = (departureDate - arrivalDate).days
    total = nightlyRate * totalNights

    print(f"Arrival Date                    {arrivalDate.strftime('%B %d, %Y')}")
    print(f"Departure Date                  {departureDate.strftime('%B %d, %Y')}")
    print(f"Nightly Rate                    ${nightlyRate:.2f}")
    print(f"Total Nights                    {totalNights}")
    print(f"Total Price                     ${total:.2f}")

    time.sleep(2)

    print()

    response = input("Can I help the next guest?? (Y/N) : ")


print("Program shutting down. Thank you.")
time.sleep(1)
sys.exit()