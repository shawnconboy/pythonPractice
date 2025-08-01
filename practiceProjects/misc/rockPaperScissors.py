import time
import os
import sys
import random

# --------------------------
# Declare functions
# --------------------------

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    clearScreen()
    print("Rock, Paper, Scissors")
    print("-" * 45)
    print()

def printChoices():
    print("Make your choice:")
    for option in choices:
        print(f"\t{option}")
    print()

def printResult(player, computer):
    print(f"You chose {player}. Computer chose {computer}.")

def updateScores(player, computer):
    global playerScore, computerScore
    if player == computer:
        print("It's a draw!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print(f"{player.capitalize()} beats {computer}. You win!")
        playerScore += 1
    else:
        print(f"{computer.capitalize()} beats {player}. Computer wins.")
        computerScore += 1

# --------------------------
# Game Starts
# --------------------------

choices = ["rock", "paper", "scissors"]

clearScreen()
header()

playGame = input("Would you like to play a game? (y/n): ").lower()

while playGame == "y":
    playerScore = 0
    computerScore = 0

    for roundNum in range(1, 4):
        header()
        print(f"Round {roundNum}/3")
        print(f"Player Score: {playerScore}     Computer Score: {computerScore}\n")

        printChoices()
        playerChoice = input("> ").lower().strip()
        computerChoice = random.choice(choices)

        print()

        if playerChoice not in choices:
            print("Invalid entry. Try again.")
            time.sleep(2)
            continue

        printResult(playerChoice, computerChoice)
        updateScores(playerChoice, computerChoice)

        time.sleep(2)

    # Match result
    header()
    print(f"FINAL SCORE:\nPlayer: {playerScore}   Computer: {computerScore}\n")

    if playerScore > computerScore:
        print("🏆 You win the match!\n")
    elif computerScore > playerScore:
        print("💻 Computer wins the match!\n")
    else:
        print("🤝 It's a tie!\n")

    playGame = input("Would you like to play again? (y/n): ").lower()

print("\nThanks for playing. Game ended.")
sys.exit()
