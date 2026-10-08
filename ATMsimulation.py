balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful")
            print("New balance:", balance)
        else:
            print("Deposit amount must be positive")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Withdrawal amount must be positive")

        elif amount > balance:
            print("Insufficient balance")

        else:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)

    elif choice == 4:
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid choice")