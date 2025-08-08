import time, sys, os

def clearScreen():
    os.system("clear")

clearScreen()

def header():
    print("Calculator")
    print("-"*45)
    print()

header()

print("What would you like to do?")

print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

userChoice = int(input("\nPlease make a selection : "))

if userChoice == 1:
    clearScreen()
    header()
    print("Addition")
    print("-"*22)
    num1 = int(input("\nEnter number : "))
    num2 = int(input("Enter number to add : "))

    total = num1+num2
    print(f"\n{num1} + {num2} = {total}")
elif userChoice == 2:
    clearScreen()
    header()
    print("Subtraction")
    print("-"*22)
    num1 = int(input("\nEnter number : "))
    num2 = int(input("Enter number to subtract : "))

    total = num1-num2
    print(f"\n{num1} - {num2} = {total}")
elif userChoice == 3:
    clearScreen()
    header()
    print("Multplication")
    print("-"*22)
    num1 = int(input("\nEnter number : "))
    num2 = int(input("Enter number to multiply : "))

    total = num1*num2
    print(f"\n{num1} * {num2} = {total}")
elif userChoice == 4:
    clearScreen()
    header()
    print("Divsion")
    print("-"*22)
    num1 = int(input("\nEnter number : "))
    num2 = int(input("Enter number to divide : "))

    total = num1/num2
    print(f"\n{num1} / {num2} = {total}")

