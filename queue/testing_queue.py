import queueCustom as queue


print("The current size is:", queue.size())
print("The queue is empty:", queue.is_empty())
print("Adding strawberry to the queue")
queue.enqueue("strawberry")
print("The current size is:", queue.size())
print("The queue is empty:", queue.is_empty())
print("What is at the front?:", queue.peek())
print("Adding strawberry to the banana")
queue.enqueue("banana")
print("What is at the front?:", queue.peek())
print("What is at the back?:", queue.peek_back())

print("Removing the front element")
element = queue.dequeue()
print(f"The element {element} was removed from the front")
print("What is at the front now?:", queue.peek())