def show_Balance():
    print(f"Your Balance is ₹{balance:.2f}") #balance:.2f means decimal value(0.00)
    print(" ")

def deposit():
    amount = float(input("Enter Deposit Amount :"))
    print(" ")

    if amount < 0:
        print("Invalid Amount!")
        print(" ")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter Withdraw Amount :"))
    print(" ")

    if amount > balance:
        print("Insufficient Balance!")
        print(" ")
    elif amount < 0:
        print("Give Amount Above 0!")
        print(" ")
        return 0
    else:
        return amount
    
balance = 0
is_running = True

while is_running :
    print("Banking Program")
    print(" ")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print(" ")

    choice = int(input("Enter your choice :"))
    print(" ")

    if choice == 1:
        show_Balance()
    elif choice == 2:
        balance = balance + deposit()
    elif choice == 3:
        balance = balance - withdraw()
    elif choice == 4:
        is_running = False
    else:
        print("Invalid Input!")
        print(" ")

print("Transaction Completed!")