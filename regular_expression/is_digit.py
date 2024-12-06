import re


#using the built in python
str_example = "123"
print(str_example.isdigit())

#use regex to achieve the same thing

def is_digit(input_data):
    regex = r'^\d+$'
    match = re.search(regex, input_data)
    if match == None:
        return False
    else:
        return True

print(is_digit(str_example))