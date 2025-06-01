import time

milesDriven = float(input('How many miles were driven? : '))
gallonsUsed = float(input('How many gallons of gas were used? : '))
pricePerGallon = float(input('How much was gas per gallon? : '))
passengerAmount = int(input('How many passengers total? : '))

totalGasCost = gallonsUsed * pricePerGallon

eachPassengerDue = totalGasCost / passengerAmount


print()
print('The total gas cost for the trip is $' + str(totalGasCost) + '.')

print('The total due for each passenger is $' + str(eachPassengerDue) + '.')