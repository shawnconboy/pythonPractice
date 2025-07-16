import pyinputplus as pyip, os, sys, time


def clearScreen():
    os.system("clear")

clearScreen()

item = pyip.inputNum("Enter a number: ")
print(f"You entered: {item}")

time.sleep(1)
clearScreen()


itemValue = pyip.inputMenu(["apple", "peach", "orange"])
print(itemValue)

testGrades = input("Enter grades : ")

grades = testGrades.split(",")

print(grades)