import time, sys, os, random

os.system("clear")

secretNumber = random.randint(1,20)
name = input("Hello. What's your name? : ")

print(f"Hello {name}. Guess a number between 1 and 20.")

for guesses in range(1,7):
    guess = int(input())

    
    if guess > secretNumber:
        print("You're guess was too high.")
    elif guess < secretNumber: 
        print("Your guess was too low.")
    else:
        break

if guess == secretNumber:
    print("Congratulations. You guessed correctly.")
else:
    print("Aww. You ran out of tries.")
    print(f"The number was {secretNumber}")