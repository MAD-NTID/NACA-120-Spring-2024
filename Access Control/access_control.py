CORRECT_PASSWORD = "topS3cret"
CORRECT_PASSWORD_TWO = "admin#1!"
""""
user_input = input("Enter your password:")
if user_input == CORRECT_PASSWORD:
    print("Welcome admin")
elif user_input == CORRECT_PASSWORD_TWO:
    print("Welcome admin")
else:
    print("Incorrect username or password!")
"""

#get the input from the user and store it in a variable called user_input
user_input = input("Enter your password:")
#check to see if the user type the correct password
if user_input == CORRECT_PASSWORD or user_input == CORRECT_PASSWORD_TWO:
    #the user type the correct password, so we welcome them
    print("Welcome admin")

else:
    #user type the incorrect password
    print("Incorrect username or password!")

    print("Welcome to python programming")