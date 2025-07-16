# This program calculates your bonus based on sick days


import time

bonus = [500, 500, 300, 300, 100, 100, 0]

print()
print()
print()

days = int(input('How many sick days did you have? : '))
bonusAmt = bonus[days]

print(f"Your bonus amount is ${bonusAmt}.")

# # Determine bonus amount
# if sickDays <= 1:
#     bonus = 500
# elif sickDays <=3:
#     bonus = 300
# elif sickDays <=5:
#     bonus = 100
# else:
#     bonus = 0

# print()
# print('You missed ' + str(sickDays) + ' sick day(s).')
# print()
# print('Your bonus is $' + format(bonus, '.2f') + '.')
# print()
# print()
# print()

