# import random
# import sys


# # name = 'Shawn'

# # if name == 'Shawn':
# #     print('Hello ' + name)
# # else:
# #     print('hello, stranger')
# # # sys.exit()

# # print('My name is')
# # for i in range(5):
# #     print('Jimmy five times (' + str(i + 1) + ')')

# # total = 0
# # for num in range(101):
# #     total = total + num
# # print(total)

# # dog = 'rocko'

# # dogCounter = 0
# # while dogCounter < 5:
# #     print(dog)
# #     dogCounter += 1

# # students = 0

# # for i in range (10,15):
# #     print(i+1)
# #     i += 1

# # for i in range(0, 105, 5):
# #     print(i)

# # for i in range(5):
# #     print(random.randint(1,10))


# randNum = random.randint(1,20)
# userGuess = 0

# print('I am thinking of a number from 1 to 20')
# print('Take a guess')
# userGuess = int(input())


# if userGuess == randNum:
#     print('Correct.')
# elif userGuess > randNum:
#     print('Too High')
# else:
#     print('Too low')
















# import random

# # declare variables

# secretNumber = random.randint(1,20)

# print('Guess the number between 1 and 20')

# for i in range(5): 
#     print("What's your guess?")
#     userGuess = int(input())

#     if userGuess > secretNumber:
#         print('Too high')
#     elif userGuess < secretNumber:
#         print('Too low')
#     else:
#         print('correct')
#         break

# if userGuess != secretNumber:
#     print("You failed. the secret number was " + str(secretNumber))














import random
import os



# declare variables

wins = 0
losses = 0
draw = 0

playerScore = 0
computerScore = 0

os.system('clear')


print('Rock, Paper, Scissors')
while True:
   
    print ('Enter your move (R)ock, (P)aper, (S)cissors, or (Q)uit')
    userChoice = input().strip().lower()

    if userChoice == 'q':
        print('Thanks for playing')
        break
    elif userChoice == 'r' or userChoice == 'p' or userChoice == 's':
        continue
    else:
        print('Invalid entry')