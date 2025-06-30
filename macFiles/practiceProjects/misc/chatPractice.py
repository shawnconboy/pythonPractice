import time, os, sys

def clearScreen():
    os.system("clear")

clearScreen()

name = input("Please enter your name: ")

oddCounter = 0
evenCounter = 0

for i in range(5):
    number = int(input("Enter a number : "))

    if number % 2 == 0:
        evenCounter = evenCounter + 1
    else:
        oddCounter = oddCounter + 1

clearScreen()

print(f"Hello {name}. You entered {evenCounter} even numbers and {oddCounter} odd numbers.")

time.sleep(2)
sys.exit()
