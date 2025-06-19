import pyinputplus as pyip

item = pyip.inputNum("Enter a number: ")
print(f"You entered: {item}")


itemValue = pyip.inputMenu(["apple", "peach", "orange"])
print(itemValue)