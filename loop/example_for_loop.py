#without putting down the start, the default start value will be 0
print("stop")
for i in range(10):
    print(i)

#we can also define where to start
print("start,stop")
for i in range(1,10):
    print(i)

#using the kth value
print("using kth")
for i in range(1,10,2):
    print(i)

print("The length")
print(len(range(1,3)))

#print from 1 to 5
"""
for num = 1 to 5
    print(num)
end for
"""
print("number 1 to 5")
for num in range(5):
    #we add 1 because of the zero based counting
    print(num+1)

user_input = input("Enter a sentence:")

print("Each character you typed:")
for letter in user_input:
    print(letter)
