import time, os, sys

os.system("clear")

def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        print(num)

while True:
    try:
        num = int(input("Please enter a number : "))
        break
    except ValueError:
        print("Type in a number, foo.")

collatz(num)