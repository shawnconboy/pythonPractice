import time, sys, os
from TechWave import current_inventory

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def printheader():
    print('Welcome to TechWave Components!')
    print('-'*25)

def printmenu():
    for i in current_inventory:
        print(f"{i:<20}{current_inventory[i]:>25}")

#change directory
os.chdir("/Users/shawnconboy/Desktop")

#Start
clear_screen()
printheader()
loop_key = 'y'
while loop_key.lower() == 'y':
    customer_name = input('\nWelcome, please enter your name: ')

    receipt = open(f'TW Receipt {customer_name}.txt','w')
    receipt.write(f'{customer_name}\'s Component Invoice')
    receipt.write(f'\n***************************************\n')


    total_items = []
    total = 0

    multiple_items = 'y'
    while multiple_items.lower() == 'y':
        clear_screen()
        printheader()
        printmenu()
        print('*'*50)
        customer_order = input('Please enter an item you wish to purchase: ').title()

        quantity = int(input('How many would you like to buy?: '))#get quantity

        for i in range(quantity):
            if customer_order in current_inventory: #verify item is in the inventory
                price = current_inventory[customer_order]
                total += price
                receipt.write(f'\n{customer_order} ${price}')
            else:
                print('That item may not be on the menu please try again.')

        #calculate shipping
        if total < 50:
            shipping_fee = 7.99
        elif total < 100:
            shipping_fee = 4.99
        elif total > 100:
            shipping_fee = 0

        #calculate tax
        taxes = (total + shipping_fee) * .07
        full_total = total + shipping_fee + taxes

        #display current total
        print('\n**************************************')
        print('Shipping Fee: $' + format(shipping_fee,',.2f'))
        print('Current taxes: $' + format(taxes,',.2f'))
        print('Current subtotal: $' + format(total,',.2f'))
        print('Current total: $' + format(full_total,',.2f'))
        print('**************************************')

        #request to loop
        multiple_items = input('Do you wish to purchase more items? <y or n>: ')

    #reset screen
    clear_screen()
    printheader()
    print('Final total: $' + format(full_total,',.2f'))

    loop_key = input('Would you like to make a new order? <y or n>: ')

receipt.write('\n\nShipping Cost: $' + format(shipping_fee, ',.2f'))
receipt.write('\nTaxes: $' + format(taxes,',.2f'))
receipt.write('\nFinal Total: $' + format(full_total,',.2f'))
    
print('Thank You! Check your Sample folder for the receipt!')

receipt.write('\n\n\n * Thank You! *')
receipt.close()

time.sleep(5)