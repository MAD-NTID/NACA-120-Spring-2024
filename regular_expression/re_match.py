import re

def start_with(start,text):
    regex_pattern = r''+start
    result = re.match(regex_pattern, text)
    if result == None:
        return False
    return True


text = "RIT is a great university....Maybe? Well, it is"
print(text.startswith("RIT"))
print(start_with("RIT", text))