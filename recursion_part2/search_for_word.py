words = ["Hello", "world", "my", "name", "is", "Spy"]

#approach 1
def search_word_rec(target,index):
    if index < 0:
        return False

    #remember list are 0 based so if we past the len then it is not in the list
    if index >= len(words):
        return False
    
    if words[index] == target:
        return True
    
    index = index + 1
    return search_word_rec(target,index)


print(search_word_rec("Hello", 0))
print(search_word_rec("YOLO",0))

def search_rec_2(target,all_words):
    if len(all_words) == 0:
        return False
    
    if all_words[0] == target:
        return True

    return search_rec_2(target, all_words[1:])


print(search_rec_2("Hello", words))
print(search_rec_2("YOLO",words)) 
