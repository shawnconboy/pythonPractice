import time

print()
print()
print()

name = input('Please enter your name : ')
creditHours = int(input('Please enter total credit hours : '))


print('Hello ' + name + '.')
if creditHours < 12:
    print("You are not a full time student, therefore you can not make the Dean's List")
    eligibility = False
else:
    gpa = float(input('Please enter your GPA : '))
    eligibility = True

    if eligibility == True:
        if gpa < 3.5:
             print('You did not make the list.')
        else:
            print('You made the list! Congrats.')

print()
print()
print()

time.sleep(5)