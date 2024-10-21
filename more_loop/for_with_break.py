print("=============================")
print("||       Word checker        ||")
print("=============================")

print("\n")
sentence = input("Enter a sentence:")
target = input("What would you like to search for:")
delimeter = " "


words = sentence.split(delimeter)
found_match = False
for word in words:
    if word == target:
        #we found a match so we have to update the found_match to true
        found_match = True
        break

#show the user the result of the search
if found_match == True:
    print(f"We found a match for {target} in the sentence!")
else:
    #print("No match was for " + target+ " was found")
    #print("No match for", target, "was found")
    print(f'No match for {target} was found!')