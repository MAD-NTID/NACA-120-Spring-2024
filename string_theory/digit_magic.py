SECRET_PIN = 0000

while True:
    pin = input("Enter your pin numbers:")
    if not pin.isdigit():
        print("Really? Pin numbers are digits only!")
        continue
    if int(pin) == SECRET_PIN:
        print("Welcome, here is 1 million dollars!")
        break
    
    print("Incorrect pin!")