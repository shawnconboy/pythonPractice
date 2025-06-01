import time

name = input('What is your name? : ')
boxesSold = int(input('How many boxes of cookies did you sell? : '))

cookiePrice = 4.75

totalSold = cookiePrice * boxesSold

print()
print(name + ', you sold (' + str(boxesSold) + ') boxes and raised $' + format(totalSold, ',.2f') + ' for the fundraiser!' )

time.sleep(5)