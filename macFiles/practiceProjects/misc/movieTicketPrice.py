import time

age = int(input('How old are you? : '))


if age < 12:
    price = 7
elif age >= 65:
    price = 8
else:
    isStudent = input('Are you a student? (yes or no) : ').strip().lower()
    
    if isStudent == 'yes':
        price = 10
    else:
        price = 12

print('Your movie ticket price is: $' + str(price))

