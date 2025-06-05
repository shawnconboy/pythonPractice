import time, os, sys, random

os.system("clear")

def calculateDebitCredit(con):
    """ This function calculates credit/debit fee """
    if con == "y":
        return 15
    else:
        return 0
    
def calculatePayPlan(pay):
    """ This function calculates payment plan fee """
    if pay == 'y':
        return 30
    else:
        return 0
    
def calculateDistanceFee(onlineHours):
    onlineFee = int(onlineHours) * 21
    return onlineFee

# main program

# prime the loop
def main():
    keepGoing = 'y'

    # start my loop
    while keepGoing.lower() == 'y':
        os.system("clear")
        print()
        print(f"Tuition Calculator")
        print("-"*35)
        print()
        convene = input("Are you paying with card?(Y/N) : ")
        payment = input("Are you setting up a payment plan?(Y/N) : ")
        online = int(input("Enter number of hybrid/online classes : "))
        totalCost = calculateDebitCredit(convene) + calculatePayPlan(payment) + calculateDistanceFee(online)

        print()
        print(f"Your total fees cost is {totalCost:,.2f}")
        keepGoing = input("Would you like to keep going?(Y/N) : ")
    

main()