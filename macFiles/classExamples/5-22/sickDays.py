# This program calculates your bonus based on sick days


import time

print()
print()
print()
sickDays = int(input('How many sick days did you have? : '))

# Determine bonus amount
if sickDays <= 1:
    bonus = 500
elif sickDays <=3:
    bonus = 300
elif sickDays <=5:
    bonus = 100
else:
    bonus = 0

print()
print('You missed ' + str(sickDays) + ' sick day(s).')
print()
print('Your bonus is $' + format(bonus, '.2f') + '.')
print()
print()
print()