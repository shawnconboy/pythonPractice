import time, os, sys, random

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

# rock paper scissors in console

playerScore = 0
playerChoice = ""

computerScore = 0
computerChoice = 0

# menu
def header():
    clearScreen()
    print("Rock, Paper, Scissors")
    print("-"*45)
    print()

choices = ["rock", "paper", "scissors"]
    

clearScreen()
header()

playGame = input(f"Would you like to play a game?(y/n) : ").lower()

while playGame == "y": 
    header()

    # play game code here
    playerChoice = input("Make your choice.\n\nrock\npaper\nscissors\n\n")

    computerChoice = random.choice(choices)

    print()

    if playerChoice == "rock":
        if computerChoice == "rock":
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print("It's a draw!")
        elif computerChoice == "paper":
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print(f"{computerChoice.capitalize()} beats {playerChoice}. Computer Wins.")
        else:
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print("You win!")
    elif playerChoice == "paper":
        if computerChoice == "paper":
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print("It's a draw!")
        elif computerChoice == "scissors":
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print(f"{computerChoice.capitalize()} beats {playerChoice}. Computer Wins.")
        else:
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print("You win!")
    elif playerChoice == "scissors":
        if computerChoice == "scissors":
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print("It's a draw!")
        elif computerChoice == "paper":
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print(f"{computerChoice.capitalize()} beats {playerChoice}. Computer Wins.")
        else:
            print(f"You chose {playerChoice}. Computer chose {computerChoice}.")
            print("You win!")
    else:
        print("Invalid entry")
    
    playGame = input("Would you like to play again?(y/n) : ")
