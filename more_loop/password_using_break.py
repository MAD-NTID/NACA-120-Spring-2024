CORRECT_PASSWORD="Shh$3cret"


while True:
    password = input("Enter the password:")
    if password == CORRECT_PASSWORD:
        break #this will force the program to quit the loop(not the program)


print("Welcome admin!")