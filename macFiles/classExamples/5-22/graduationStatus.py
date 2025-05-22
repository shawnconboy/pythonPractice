import time

name = input('Please enter your name : ')
gpa = float(input('Please enter your GPA : '))

if gpa > 2.0:
    eligible = True

if eligible == True:
    if gpa >= 4.0:
        status = 'Summa Cum Laude'
    elif gpa > 3.8:
        status = 'Manga Cum Laude'
    elif gpa >3.5:
        status = 'Cum Laude'
    elif gpa > 2.0:
        status = 'Eligible'
else:
    eligible = False
    status = 'Requirements to graduate not met.'



print(name + ' your graduation status is ' + status)

time.sleep(5)