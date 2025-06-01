import os, time, sys, random

os.system("clear")
print()

result = []

print("\nStart of List\n")
#creates random output of T and H
for i in range(100):
    randomChoice = random.choice("TH")
    result.append(randomChoice)

hCount = 0
for item in result:
    if item == "H":
        hCount += 1

tCount = 0
for item in result:
    if item == "T":
        tCount += 1


print(result)
print()
print(f"There are {hCount} H's in the list.")
print(f"There are {tCount} T's in the list.")

print()
print()
