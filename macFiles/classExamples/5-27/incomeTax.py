import sys, time, os

os.system('clear')
# This is a program to calculate income tax from clients
print()
print("Income Tax Time LLC")
print("__________________________")
print()
print()

# priming read
response = 'y'

# This loop will work for multiple users.
while response.lower() == 'y':

    # Take user info each time.
    name = input("Please enter your name : ")
    gross = float(input("Please enter your gross income : "))
    dependents = int(input("Please enter number of dependents : "))

    taxableIncome = gross - 10000 - (3000 * dependents)

    # If statement to decide tax bracket
    if taxableIncome < 10001:
        percentTax = 0.1
    elif taxableIncome < 40001:
        percentTax = 0.12
    elif taxableIncome < 86501:
        percentTax = 0.22
    else:
        percentTax = 0.32

    # Display user info
    print(f'Hello, {name}.')
    print("Your total taxable in come is $ " + format(taxableIncome,',.2f')+ ".")
    print(f"That puts you at %{percentTax}, percent being taxed.")

    # Update read
    print()
    response = input("Do you want to enter another person's info? (Y/N) : ")

print("Program has ended.")
sys.exit()