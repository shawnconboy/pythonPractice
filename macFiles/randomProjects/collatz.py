import time, sys

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = number * 3 + 1
    print(result)
    time.sleep(0.1)
    return result

try:
    number = int(input('Please enter a number: '))
    while number != 1:
        number = collatz(number)
except KeyboardInterrupt:
    sys.exit()
