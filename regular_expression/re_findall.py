import re

phone_number_regular_expression = r'\d{3}-?\d{3}-?\d{4}'
example_phone_number="Hello world! My phone number is 585-312-2574! also 5853131397 and 585-313-1356"
#example_phone_number="garbage"


phone_number = re.findall(phone_number_regular_expression,example_phone_number)
#print(phone_number)
if phone_number == None:
    print("No phone number was found!")
else:
    #print(phone_number)
    for number in phone_number:
        print(number)
    