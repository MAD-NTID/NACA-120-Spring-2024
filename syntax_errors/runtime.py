def divide(num1, num2):
    return num1/num2


while True:
    number1 = input("Enter the first number:")
    number2 = input("Enter the second number:")

    #check if digit before attempting to convert
    if number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number2)

        if number2 == 0:
            print("Bruh, your math is not mathing!")
            continue
    else:
        print("Seriously? Just enter digits!!")
        continue
    

    res = divide(number1,number2)

    print(f"The result is {res}")

