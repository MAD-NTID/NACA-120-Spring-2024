# word = "I love unicorns!"

# print(word.split(" "))

# #without using in
# match = False
# for element in word.split(" "):
#     if element == "unicorn":
#         match = True

# print(match)

# #using "in" to find a match   
# print("unicorn" in word)
# print("student" in word)


#this is the same code from search_magic.py but this time we use "in"
magics = ['unicorn', 'rainbow', 'easter egg','stuff']

while True:
    found = False
    target = input("What do you want to search for:")
    #use in to see if there is a match
    if target in magics:
        found = True

    if found:
        print("We found a match for", target)
    else:
        print("No match was found for", target)