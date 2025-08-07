import time, os, sys

os.system("clear")

print("Calculator\n")

def add(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

def subtract(num1,num2):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

def multiply(num1,num2):
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

multiply(2,5)
print()
add(3,397)


print()
print()
print()
print()
time.sleep(2)
sys.exit()