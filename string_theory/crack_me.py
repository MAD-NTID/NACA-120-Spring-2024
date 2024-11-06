PASSWORD = "topS3cret"

while True:
    print("The password is:", PASSWORD)
    password = input("Enter the password:")
    password = password.replace(PASSWORD, '') #strip out the topS3cret
    print("THe new password after stripping is:", password)
    if password == PASSWORD:
        print("Welcome clever master!")
    else:
        print("Not so clever!")