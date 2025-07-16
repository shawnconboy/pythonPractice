import time, sys, os, datetime

def clearScreen():
    os.system("clear")

def header():
    print("Daily Mood Logger!")
    print("-"*40)
    print(f"Today is {str(formattedDate)}")
    print()

desktop = os.chdir("/Users/shawnconboy/Desktop")

moodFile = open("/Users/shawnconboy/Desktop/moodFile.txt", "a")

currentDay = datetime.datetime.now()
formattedDate = currentDay.strftime("%B %d, %Y")
clearScreen()

# **************************************************************************
header()


name = input("Please enter your name : ")

print(f"\nHello {name}, how are you feeling today? : \n")

questionResponse = input()


# ************************************************

moodFile.write("\nDaily Mood Logger!\n")
moodFile.write("-"*40)
moodFile.write(f"\n{str(formattedDate)}")
moodFile.write(f"\nYour feelings : ")
moodFile.write(f"\n{questionResponse}")

print("Program has ended. Thank you.")
time.sleep(1)
sys.exit()