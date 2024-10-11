"""
    This function will print hello human
    When we create a function, we only define the function but have not used it yet
"""
def say_hello(name):
    print("Hello " + name + "...Nice to meet you huuuuuman")


def call_my_magic_function():
    print("Unicorn incoming!!!!")


def box():
    print("===================================")
    print("||                               ||")
    print("||                               ||")
    print("||                               ||")
    print("||                               ||")
    print("||                               ||")
    print("===================================")


"""
    This is a function that takes two numbers
    add them up and return the result

    because return the result, we can assign it to a variable if needed
"""
def sum(num1,num2):
    result = num1+num2
    return result

def hello(word):
    print("Hello "+ word)

#add a main function
def main():
    #prompt the user for a word
    word = input("Please enter a word:")
    #pass the word to hello
    hello(word)

#call the main
main()






#sum_of_two_numbers = sum(3,6)
#print("The result of the numbers are:",sum_of_two_numbers)

#print(sum(3,6))

"""
    This is a function that takes two numbers
    add them up and print the result in the function
    THE FUNCTION DOESNT RETURN ANYTHING

"""
def sum_print_in_function(num1, num2):
    result = num1+num2
    print(result)

#sum_print_in_function(3,6)



    

#box()

#now we call/invoke the function
#say_hello("Kemoy")

#call_my_magic_function()



