
keepGoing = 'y'

while keepGoing == 'y':
    amount = input("Enter a number : ")


    try:
        amount = int(amount)
    except ValueError:
        print("Please enter number a : ")
        continue
    
    keepGoing = input("Would you like to continue?(Y/N) : ")