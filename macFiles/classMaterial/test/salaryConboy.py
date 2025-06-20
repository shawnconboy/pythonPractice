#This is a program to determine salary increases per employee
import time, sys, os

# dictionary for percentages
increasePercentages = {
    12: 0.02,
    14: 0.035,
    16: 0.025,
    18: 0.03,
    20: 0.01
}

# recreation of the dictionary for percentages
def menu():
    for i in increasePercentages:
        percentage = increasePercentages[i]
        print(f"{i} \t\t {percentage}")

# this wipes the screen. you know?
def clearScreen():
    os.system("clear")


# here's the main program

# priming the loop with response variable
response = "y"
while response == "y":
    clearScreen()

    # display title
    print("Salary Manager")
    print("-" * 40)

    # get user data. ID can be whatever.
    employeeID = input("\nPlease enter your employee ID : ")

    # performance rating will determine raise eligibility.
    performanceRating = input("\nPlease enter performance rating :  ").lower()

    if performanceRating == "e" or performanceRating == "s" or performanceRating == "u":
        if performanceRating == "e" or performanceRating == "s":
            currentSalary = float(input("\nPlease enter current salary : "))
            classification = int(input("\nPlease enter employee classification : "))
            
            # this will check if the classification is in
            # the dictionary
            if classification in increasePercentages:
                percent = increasePercentages[classification]
                salaryIncrease = currentSalary * percent
                newSalary = salaryIncrease + currentSalary
        

            # display info back to user
            clearScreen()
            print("Loading .......")
            time.sleep(1)
            clearScreen()
            print("Salary Manager")
            print("-" * 40)
            print(f"\nEmployee ID\t\tCurrent Salary\t\tNew Salary")
            print("-"*60)
            print(f"{employeeID}\t\t\t${currentSalary:,.2f}\t\t${newSalary:,.2f}")
        elif performanceRating == "u":
            print("\nSorry. You are on probation for one year.")
    else:
        print("Invalid Entry. Please try again.")
        time.sleep(2)
        continue
    
    response = input("\nWould you like to enter another employee? (Y/N) : ").lower()

print("\nThank you. Program has ended.")

time.sleep(1)
sys.exit()