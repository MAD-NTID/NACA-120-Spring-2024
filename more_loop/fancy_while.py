repeat = True

while repeat: #same as while repeat == True
    sentence = input("Enter a sentence:")
    print(f"You typed:{sentence}")
    #set repeat to false if the user entered EXIT
    if sentence == "EXIT":
        repeat = False
