# This program works as a bmi calculator.
# Shawn Conboy -- May 28, 2025
import time, sys, os, platform

# Here, is a function that clears the terminal screen, whether you're using windows, or mac / linux
def clearScreen():
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')

clearScreen()

# priming read
response = 'y'

while response.lower() == 'y':

    print()
    print("BMI Calculator")
    print("-"*15)
    print()

    # get data from user
    name = input("Please enter your name : ")
    weight = float(input("Please enter your weight in lbs : "))
    height = float(input("Please enter your height : "))

    # calculate BMI here
    bmi = (weight / (height * height)) * 703

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    # print results back to the console for user to see
    print(f"Hello, {name}.  Your BMI is {bmi:.2f}.  Status = {status}.")

    print()

    time.sleep(2)
    
    # update read
    response = input("Would you like to try again? (Y/N) : ")
    print()

    if response != 'y':
        # exit the program
        print("Program has ended.")
        time.sleep(5)
        sys.exit()

    clearScreen()

