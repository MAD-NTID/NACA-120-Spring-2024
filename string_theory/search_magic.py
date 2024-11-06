magics = ['unicorn', 'rainbow', 'easter egg','stuff']

while True:
    found = False
    target = input("What do you want to search for:")
    #loop through each of the magic and compare them
    for magic in magics:
        #did we find a match?
        #force both to lowercase or uppercase to ignore case sensitivity
        if magic.lower() == target.lower():
            found = True
            break
    
    if found:
        print("We found a match for", target)
    else:
        print("No match was found for", target)

    
    