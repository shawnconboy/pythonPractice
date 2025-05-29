import time 

name = input('Please enter your name : ')
grade = float(input('Please enter numeric grade: '))


if grade < 69.5:
    letterGrade = 'F'
elif grade < 79.5:
    letterGrade = 'C'
elif grade < 89.5:
    letterGrade = 'B'
else:
    letterGrade = 'A'

print('Hello '+ name + '. Your letter grade is ' + letterGrade + '.')

time.sleep(5)