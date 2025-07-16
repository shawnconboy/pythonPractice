# This program will ask a user for their name, total credit hours being taken and calculate their total tuition cost.
# This program was made by Shawn Conboy on May 20th 2025

# This will allow for delay prior to program closing so user can see output.
import time


# Program begins here.
print()
print()

# Ask user for name
name = input('Please enter your name : ')

# Assing tuition value, and ask for total credit hours
tuition = 198
creditHours = int(input('How many credit hours are you taking? : '))


# Calculate tuition cost by converting credit hours to an int to do arithmetic
totalPrice = tuition * creditHours

# Display output showing summary of program
print()
print('Hi ' + name + '. Your tuition is $' + format(totalPrice, ',.2f') )

time.sleep(5)
