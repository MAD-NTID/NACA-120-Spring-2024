import re

phone_number_regular_expression = r'\d{3}-?\d{3}-?\d{4}'
example_phone_number="Hello world! My phone number is 585-312-2574!"
#example_phone_number="garbage"


phone_number = re.search(phone_number_regular_expression,example_phone_number)
#print(phone_number)
if phone_number == None:
    print("No phone number was found!")
else:
    extracted = phone_number.group()
    print(extracted)