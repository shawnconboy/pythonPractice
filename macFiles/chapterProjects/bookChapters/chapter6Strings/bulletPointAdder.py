import time, sys, os, pyperclip

os.system("clear")

randomList = ["animals",
              "aquarium life"
              "biologist by author abbreviation",
              "cultivars"]

for i in randomList:
    print(f"* List of {i.title()}")