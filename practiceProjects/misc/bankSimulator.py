import time, os, sys
os.system("clear")
option = 0
balance = 0

while option != 3:
    print("\t\tBank of The Ville")
    print("\t_________________________________")
    print()

    print(f"\tBalance     {balance:>12,.2f}")
    print()

    print("\t1. Deposit")
    print("\t2. Withdraw")
    print("\t3. Exit")

    print()
    option = float(input("\tSelect an option : "))

    print()
    if option == 1:
        print("\tDeposit Selected.")
        depositAmount = float(input("\tDeposit amount : $"))
        balance += depositAmount
        print()
        print(f"\tYou deposited ${depositAmount:,.2f}.")
        time.sleep(1)
    elif option == 2:
        print("\tWithdraw Selected.")
        withdrawAmount = float(input("\tWithdraw amount : $"))
        balance -= withdrawAmount
        print()
        print(f"\tYou withdrew ${withdrawAmount:,.2f}.")
        time.sleep(1)

    elif option == 3:
        print("\tExiting ATM ", end="")
        for dot in range(5):
            time.sleep(0.1)
            print(".", end="")
            sys.stdout.flush()
        print()
        print()
        print()
        print()
        time.sleep(3)
       
        break

    os.system("clear")
sys.exit()

