import stack


"Testings"
print("Is the stack empty?:", stack.is_empty())
print("The size of the stack is:",stack.size())
stack.push("Lebron James")
stack.push("Michael Jordan")
print("The size of the stack is now:",stack.size())
print("The top element is:",stack.peek())
print(f"The top {stack.pop()} was removed from the top")
print("The top new element is:",stack.peek())