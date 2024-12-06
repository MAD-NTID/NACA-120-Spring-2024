import re

def show_last_four_ssn(ssn):
    regex_pattern = r'\d{3}-?\d{2}-?'
    asterik="***-**-"
    result = re.sub(regex_pattern,asterik, ssn)
    return result

top_secret_ssn= "123-45-6789"
last_four_ssn = show_last_four_ssn(top_secret_ssn)

print(f'The full ssn:{top_secret_ssn} and the last 4 is:{last_four_ssn}')

ssn_list = [
    "123-45-6789",
    "987-65-4321",
    "456-78-1234",
    "234-56-7890",
    "345-67-8901",
    "876-54-3210",
    "567-89-0123",
    "678-90-1234",
    "345-12-6789",
    "890-12-3456"
]

for ssn in ssn_list:
    last_four_ssn = show_last_four_ssn(ssn)
    print(last_four_ssn)
