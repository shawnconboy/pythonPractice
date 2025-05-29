# This program acts as a kiosk to determine correct pricing for customers

# You are going to create a program to charge admission price to SCC sports events. Full admission price is $5. If a SCC student attends, their admission is free. If an alumni attends, admission price is reduced 50% and staff are reduced 80%. Others pay full price. Chaser shirts are also available for an additional $10.

# Write a program to display a small menu on a kiosk asking the user to choose #1 if a student, #2 if an alumni, #3 if SCC staff, and #4 if other. Then inquire if they would like to purchase a Chaser shirt. Tally total amount due and display back to him/her with a $ and 2 decimal positions. Include a loop to accommodate all event attendees until the person operating the kiosk chooses to end the loop.

import time, sys, os

os.system("clear")

ticketPrice = 0
fullPrice = 5
studentPrice = 0
alumniPrice = fullPrice * 0.5
staffPrice = fullPrice * 0.2

response = "y"

while response.lower() == "y":

    os.system("clear")

    print("-"*35)
    print("SCC Sporting")
    print()

    print("Hello. Choose your status.")
    print("-"*35)
    print()

    print(f"1 -- Guest      ${fullPrice:>15.2f}")
    # print(f"2 -- Alumni     ${alumniPrice:.2f}")
    # print(f"2 -- Alumni  ${alumniPrice:16.2f}".rjust(27))
    print(f"2 -- Alumni  {'$'+format(alumniPrice, '15.2f')}")
    print(f"3 -- Student    ${studentPrice:.2f}")
    print(f"4 -- Staff      ${staffPrice:.2f}")
    print()

    status = int(input())

    if status == 1:
        ticketPrice = fullPrice
    elif status == 2:
        ticketPrice = alumniPrice
    elif status == 3:
        ticketPrice = studentPrice
    elif status == 4:
        ticketPrice = staffPrice
    else:
        print("Invalid. Please select from 1 through 4.")
        time.sleep(3)
        continue

    print()
    tShirt = input("Would you like to purchase a T-Shirt for $10.00 as well? (Y/N) : ")

    if tShirt.lower() == "y":
        tShirtPrice = 10
    else:
        tShirtPrice = 0

    total = ticketPrice + tShirtPrice

    print(f"Your total is ${total:.2f}.")
    print(f"Thank you.")

    response = input("Would you like to order again? (Y/N) : ")
    time.sleep(2)

print("Program has ended.")
time.sleep(3)
sys.exit()