import time

name = input('What is your name? : ')

height = int(input('What is your height in inches? : '))

weight = int(input('What is your weight in lbs? : '))

bmi = (weight * 703) / (height* height)

print ('Hello ' + name)
print ('Your BMI is ' + format(bmi, '.2f'))

if bmi < 18.5:
    print('You are underweight')
elif bmi < 25:
    print('You are at a normal weight')
elif bmi < 30:
    print('You are overweight')
else:
    print('You are obese')
