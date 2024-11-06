def custom_find(word,target_letter):
    #set index to -1
    index = 0

    #go through each letter in the word
    for letter in word:
        #does it match what we are searching for
        if letter == target_letter:
            return index
        #increment the index
        index+=1
    #there has been no match so we return a negative 1
    return -1


question = "What do you plan to do this weekend?"
print(question)
print("The first character/letter is:", question[0])
print("d is at the index position:",question.find('d'))
print("d is at the index position using our custom function:",custom_find(question, 'd'))
print("z is at the index position:",question.find('z'))

print("Convert all letters to caps", question.upper())
print("convert all letter to lower:", question.lower())

#we need to reassign because .replace is not an in place update
old_question = question
question = question.replace('t', 'JJJJJJ',1)
print("Old question:", old_question)
print("The new question is:", question)

hello_world = "hello world"
print(f"Capitalize will make {hello_world} become {hello_world.capitalize()}")

#using join to join a string
names = ["Farmer", "Amber","Shashank", "Aidan", "Lukas"]
seperator = "," #We must define how we want to combine the list into a string
print("My students are:", seperator.join(names))

word1 = "Hello"
word2 = "World"
word3 = "!"

print("The new word is", " ".join([word1, word2, word3]))

#using string format

total_student = 5
actual_students = 7
word = "Hello world. In this class there are {0} students today. But there are {1} in total".format(total_student, actual_students)

print(word)


product = "Laptop"
price = 999.99
formatted_string = "Product: %s - Price: $%.2f" % (product, price)
print(formatted_string)

print("Product: %s - Price: $%.2f" % (product, price))


