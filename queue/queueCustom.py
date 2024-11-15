#create a list to keep track of all elements
queue = []

"""
    check if the queue is empty
"""
def is_empty():
    if len(queue) == 0:
        return True
    else:
        return False

"""
    Show the element that is at the front
"""
def peek():
    return queue[0]

"""
    remove the first element
"""
def dequeue():
    return queue.pop(0)

"""
    Add an element to the back of the queueue
"""
def enqueue(element):
    queue.append(element)

"""
    returs the size of the elements in the queue
"""
def size():
    return len(queue)

"""
    peek to see what is at the back
"""
def peek_back():
    back_index = size() - 1
    return queue[back_index]
    #you can simpify the whole thing using the pythonic's way -1 return queue[-1]