import time, sys, os

os.system("clear")

fruitList = ["Apples", "Bananas", "Cantelope", "Dragon Fruit"]

def printList(listName):
    for i in fruitList:
        if i == fruitList[-1]:
            print(f"and {i}")
        else:
            print(f"{i}, ", end = "")

printList(fruitList)