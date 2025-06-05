#Program to calculate gpa
import time
response = 'y'
while response.lower () == 'y':
    print ('What is your name? ') # ask for their name
    name = input ()
    print ('How many credit hours have your earned? ')
    hours = input ()
    hours = float (hours)
    print ('How many quality points do you have?')
    points = float (input ())
    try:
        gpa = points / hours
        print (f'Your gpa is {gpa:.2f}')
    # except ZeroDivisionError:
    except:
        print("Please enter a number greater than 0.")
        continue
    time.sleep (5)
    response = input ('Do you wish to continue ')
print ('Program ended')