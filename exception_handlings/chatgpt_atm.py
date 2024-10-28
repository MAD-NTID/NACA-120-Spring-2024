balance = 30000
pin = "1234"  # Set a default PIN

def menu():
    print("\nMenu\n==============")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View balance")
    print("4. Exit")

def verify_pin():
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempts left.")
    print("Too many incorrect attempts. Exiting.")
    exit(1)

def deposit():
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            balance += amount
            print("Successfully added.")
            print(f"New balance: {balance}")
            break
        except ValueError as e:
            print("amount to deposit must be an number")

def withdraw():
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if amount > balance:
                raise ValueError("Insufficient funds.")
            balance -= amount
            print("Withdrawal successful.")
            print(f"New balance: {balance}")
            break
        except ValueError as e:
            print("amount to withdraw must be a number")

def view_balance():
    print(f"Current balance: {balance}")

while True:
    try:
        verify_pin()
        while True:
            menu()
            choice = input("Choice: ")
            if choice == "1":
                deposit()
            elif choice == "2":
                withdraw()
            elif choice == "3":
                view_balance()
            elif choice == "4":
                print("Thank you for using our system. Goodbye!")
                exit(0)
            else:
                print("Invalid choice. Please select a valid option.")
    except KeyboardInterrupt:
        print("\nThank you for using our system. Goodbye!")
        exit(0)
    except Exception as e:
        print(f"An unknown exception occurred: {e}. Please try again.")