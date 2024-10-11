CORRECT_PIN="1234"
CORRECT_USERNAME="Bruce Wayne"

def verify_pin(pin):
    if pin == CORRECT_PIN:
        return True
    else:
        return False

def verify_username(username):
    if username == CORRECT_USERNAME:
        return True
    else:
        return False


def main():
    print("Hello stranger.....")
    pin = input("Enter the pin:")
    username = input("Enter the username:")

    if verify_pin(pin) == True and verify_username(username):
        print("Opening the cave......")
        print("Welcome home master Bruce!")
    else:
        print("You evil person....You thought this would work?")
        print("Here is a last favor before your death.....")
        print("Bruce Wayne is batman!")
        print("Opening the death trap!")
        print("Enjoy your not so glourious death")
        print("Bye forever!")


main()