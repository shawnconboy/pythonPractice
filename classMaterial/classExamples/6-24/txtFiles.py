import time, os, sys


def clearScreen():
    os.system("clear")

# change default directory for text files

clearScreen()

os.chdir("/Users/shawnconboy/Desktop")

sonnetFile = open("sonnet01.txt", "w")
sonnetFile.write("Hey Dude")


sonnetFile.close()

time.sleep(3)
sys.exit()