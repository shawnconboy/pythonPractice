import tempMod, os, sys, time

os.system("clear")
value = float(input("Please enter temp to convert : "))

result = tempMod.convertToCelsius(value)

print(f"{result:.2f}")