# import one or more classes from dateTime module
from datetime import date, time, datetime

# import pyinputplus to retrieve dates
import pyinputplus as pyip
import os, sys, time

def clearScreen():
    os.system("clear")

clearScreen()

# current date
invoiceDate = date.today()

print(invoiceDate)

# current date and time
invoiceDate2 = datetime.now()

print(f"\n\n{invoiceDate2}")

# dateTime module contains what we call constructors
# for creating date and time objects
# to use constructors, you pass arguments to them

# this is a date object
halloween = date(2024,10,31)

appointment = datetime(2023,10,28,14,30,48)

print(halloween, appointment)

print(f"\n\n{appointment: %B %d, %Y %I:%M}")

print()

# enter date and time via pyinputplus

# dateAndTime = pyip.inputDatetime("Please enter date and time : ")

# date3 = pyip.inputDate("Please enter date : ")

# time3 = pyip.inputTime("Please enter time : ")

# print(dateAndTime,date3,time3)

# calculate spans of time

# import a dateTime class called timeDelta

from datetime import timedelta

# create spans of time

threeWeeks = timedelta(weeks=3)

futureTime = invoiceDate2 + threeWeeks
print(futureTime)

paymentDueDate = date.today() + timedelta(days=30)

print(paymentDueDate)