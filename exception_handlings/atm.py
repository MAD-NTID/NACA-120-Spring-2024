balance = 30000

def menu():
    print("Menu\n==============")
    print("1.Deposit\n2.Withdraw\n3.View fund")

while True:
    try:
        menu()
        choice = input("Choice:")
        if choice == "1":
            amount = int(input("amount:"))
            balance+=amount
            print("successful added")
            print(f"new balance;{balance}")
        elif choice == "2":
            pass
        elif choice == "3":
            print(balance)
    except ValueError:
        print("Enter a digit!")
    except KeyboardInterrupt:
        print("Thank you for using our system.")
        print("Good bye!!!")
        exit(0)
    except Exception as e:
        print(f"An unknown exception occurred:{e}")
        print("try again")

