sentence = input("Enter a sentence:")
target = input("Enter the word to count:")

#break up the words 
delimeter = " "
words = sentence.split(delimeter)

count = 0
for word in words:
    if word == target:
        count = count + 1


if count == 0:
    print(f"No match was found for {target}. The count is zero, zip, nada, nothing!")
else:
    print(f"The word {target} appeared in the sentence {count} time(s).")