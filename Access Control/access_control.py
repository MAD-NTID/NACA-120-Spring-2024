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

user_input = input("Enter your password:")
if user_input == CORRECT_PASSWORD or user_input == CORRECT_PASSWORD_TWO:
    print("Welcome admin")

else:
    print("Incorrect username or password!")