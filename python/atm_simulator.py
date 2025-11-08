balance = 0
for i in range (5):
    choice = int(input("Enter your choice : 1. Deposit 2. Withdraw 3. Check Balance 4. Exit "))
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print(f"Deposited: {amount} New balance: {balance}")
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance = balance - amount
            print(f"Withdrew: {amount} New balance: {balance}")
    elif choice == 3:
        print(f"Current balance: {balance}")
    elif choice == 4:
        print("Bye")
        break
    else:
        print("Invalid choice")
