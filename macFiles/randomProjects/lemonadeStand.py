import time

print('Lemonade Stand')
print()
cupsSold = input('How many cups did you sell? : ')

cupPrice = input('How much did each cup sell for? : ')

totalEarnings = int(cupsSold) * float(cupPrice)


print()
print('You made $' + format(totalEarnings, ',.2f') + ' today from lemonade sales!')

time.sleep(5)
