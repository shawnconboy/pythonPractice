# Create a program that prompts the user to enter an invoice date in MM/DD/YY format. 
# Then it displays the invoice date, the due date (30 days from invoice date) and the current date. 
# If the invoice is overdue, the program displays a message that indicates the number of days overdue. 
# Otherwise, the program displays a message that indicates the number of days until it is due.



from datetime import datetime, timedelta, date
import pyinputplus as pyip
import os, sys, time

def clearScreen():
    os.system("clear")

def getInvoiceDate():
    ''' function to retrieve data from user '''
    invoiceDate = pyip.inputDate("Enter invoice date mm/dd/yy : ")
    return invoiceDate

clearScreen()

def main():
    print("Invoice Due Date")
    print()

    response = "y"

    while response == "y":
        invoice = getInvoiceDate()

        #calculate due date and days overdue
        dueDate = invoice + timedelta(days=30)
        currentDate = date.today()

        daysOverdue = (currentDate - dueDate).days

        #display results
        dateFormat = '%B %d, %Y'
        print (f'Invoice date: {invoice:{dateFormat}}')
        print (f'Due date: {dueDate:{dateFormat}}')
        print (f'Current date: {currentDate:{dateFormat}}')

        if daysOverdue > 0:
            print(f"This invoice is {daysOverdue} day(s) overdue.")
        else:
            daysDue = daysOverdue * -1
            print(f"This invoice is due in {daysDue} day(s).")

        response = input("\nWould you like to run again? (Y/N) : ")

main()

print("Program has ended. Thank you.")
time.sleep(1)
sys.exit()