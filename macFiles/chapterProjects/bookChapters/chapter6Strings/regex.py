import re, time, sys, os

os.system("clear")

phoneRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

userInput = input()

match = phoneRegex.search(userInput)

if match != None:
    print(f"Phone number found : {match.group(0)}")
    print(f"Area code is {match.group(1)}")
    print(f"Actual number is {match.group(2)}")
else:
    print("No matches found.")