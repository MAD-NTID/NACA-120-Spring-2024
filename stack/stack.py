#This is a list that will be use to hold all elements
elements = []

"""
    This function will return True if the
    stack is empty. False otherwise
"""
def is_empty():
    #if the length of the element is 0 then there are no elements on the stack
    if len(elements) == 0:
        return True
    else:
        return False 
    
    #return len(elements) == 0 #short cut

"""
    returns the total number of elements on the stack
"""
def size():
    return len(elements)
"""
    This function will add an element to the top of the stack
"""
def push(element):
    elements.insert(0, element)
"""
    This function will return the element at the top without
    removing it
"""
def peek():
    top = elements[0]
    return top

"""
    This function will remove and return the element from the top
"""
def pop():
    top = elements.pop(0) #remove from the top--> first index
    return top

