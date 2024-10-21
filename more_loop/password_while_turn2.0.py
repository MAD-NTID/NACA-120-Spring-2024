CORRECT_PASSWORD="Shh$3cret"
repeat = True

while repeat:
    password = input("Enter the password:")
    if password == CORRECT_PASSWORD:
        print("Welcome admin")
        repeat = False
    else:
        print("Incorrect password. Thou shall not pass!!!")