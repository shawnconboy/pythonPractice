import re, time, os, sys, pyperclip

def clearScreen():
    os.system("clear")

clearScreen()

urlMatch = re.compile(r"https?\:\/\/(www\.[a-zA-Z0-9]+\.\w[a-z]+)")

userInput = input("Please enter your text here : ")

match = urlMatch.search(userInput)

if match:
    print()
    print(match.group(0))
    pyperclip.copy(match.group())
    print("✅ Match copied to clipboard!")
else:
    print("No matches.")