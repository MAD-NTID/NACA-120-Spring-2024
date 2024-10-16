"""
    This function will take two numbers and return their sum
"""
def sum(num1, num2):
    return num1+num2

def multiply(num1, num2):
    return num1 * num2

#result = sum(5,6)
#print(result)

# print("Kemoy " + " Campbell")
# full_name = "Kemoy " + " Campbell"
# print(full_name)

#give the user the ability to type in the numbers
#approach #1
# number1 = int(input("Enter the first number:"))
# number2 = int(input("Enter the second number:"))

#modify our program to continue forever
#while True:
    # number1 = input("Enter the first number:")
    # number2 = input("Enter the second number:")

    # number1 = int(number1)
    # number2 = int(number2)

    # print("The type of number1 is:", type(number1))
    # print("The type of number2 is:", type(number2))

    # #pass the numbers to the function
    # result = sum(number1,number2)
    # #show the result
    # print(result)

# number1 = input("Enter the first number:")
# number2 = input("Enter the second number:")

# number1 = int(number1)
# number2 = int(number2)

# print("The type of number1 is:", type(number1))
# print("The type of number2 is:", type(number2))

# #pass the numbers to the function
# result = multiply(number1,number2)
# #show the result
# print(result)


#implicit convert
#smaller stuff can fit in big bucket
fbar = 3.5
num = 3
result = fbar * num
print(result)

#explicit convert the result to int
#we need to stop pouring when the small bucket is full
num = int(fbar/num)
print(num)

#you must explicit convert a num to string if you want to do concatentation
print("Hello world I am " + str(12) + " Years old")

print(int(True))
print(str(True))

