# this program will calculate tips at 15 and 20 %
# users enters amount of their bill

# this program was written by Shawn Conboy on May 20th 2025

import time

response = 'y'.lower()

while response == 'y'.lower():
    bill = input('Please enter your bill amount : ')

    # calculate tip amounts

    tip15 = float(bill) * 0.15          # This is the 15% tip

    tip20 = float(bill) * 0.20          # This is the 20% tip

    amount15 = tip15 + float(bill)

    amount20 = tip20 + float(bill)

    # Display results

    print()

    print ('The amount of your tip if you tip 15% is $' + format(tip15, ',.2f') + ' And the total amount is ' +  format(amount15, ',.2f'))

    print ('The amount of your tip if you tip 15% is $' + format(tip20, ',.2f') + ' And the total amount is ' +  format(amount20, ',.2f'))

    print()

    time.sleep(5)

    response = input("Do you want to calculate another tip?(Y/N) : ")