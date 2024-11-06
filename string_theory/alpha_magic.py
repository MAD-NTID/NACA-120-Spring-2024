while True:
    word = input("Enter some alpha:")
    if not word.isalpha():
        print("You must enter only ALPHA!")
        continue
    
    print("well done!")