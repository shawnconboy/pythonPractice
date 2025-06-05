# this is a program to calculate a salary increase based on certain specifications
import time, os, sys

response = "y"
response.lower()

# While wraps code in body to be used for multiple teachers
while response == 'y':
    os.system("clear")
    # simple ui formatting
    print()
    print("Wayne County Board Certification")
    print("-"*40)

    # getting user data
    experienceInYears = int(input("Please enter years of experience : "))
    currentSalary = float(input("Please enter your current salary  : "))
    isCertified = input("Are you board certified? (Y/N) : ")
    isCertified.strip().lower()
    print()

    # determine increase percentage
    if experienceInYears <= 2:
        increase = 0.02
    elif experienceInYears <= 5:
        increase = 0.04
    elif experienceInYears <=10:
        increase = 0.06
    else:
        increase = 0.1

    # calculations to determine increase

    salaryIncrease = currentSalary * increase
    newSalary = currentSalary + salaryIncrease

    if isCertified == 'y':
        newSalary += 5000


    # output to the user
    print(f"Your new salary is {newSalary:,.2f}")
    print()

    response = input("Would you like to calculate another teacher?(Y/N) : ")
    response.strip().lower()

    if response == "n":
        print("Program ended.")
        time.sleep(3)
        sys.exit()
