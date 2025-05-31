import time, os

os.system("clear")

billTotal = float(input("Please enter your bill total: $"))
print("Choose tip percentage:")
print("1. 15%")
print("2. 20%")

choice = input("Enter 1 or 2: ")

if choice == "1":
    tip = billTotal * 0.15
elif choice == "2":
    tip = billTotal * 0.20
else:
    tip = 0
    print("Invalid choice. No tip added.")

totalDue = billTotal + tip

print(f"\nTip amount: ${tip:.2f}")
print(f"Total amount due: ${totalDue:.2f}")
