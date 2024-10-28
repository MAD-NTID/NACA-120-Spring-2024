#create a empty list
names = [] 
print("names:", names)

#create a list with 3 majors
majors = ["Computer Science", "Cybersecurity", "Software Engineering"]
print("0ld majors:", majors)

#looping through the majors
print("The majors are:")
for major in majors:
    print(major)


print("The majors are(using index and range):")
for index in range(len(majors)):
    print(majors[index])
print("The majors are(using while loop):")
index = 0
while index < len(majors):
    print(majors[index])
    index+=1

print("The first major is " + majors[0])

#total elements in the list
size = len(majors)
size_two = len(names)

print("Major total:", size)
print("names total:", size_two)
print("names total:", len(names))

#change computer science to WMC
majors[0] = "WMC"
print("New m@jors:", majors)

#out of range example. This will not
#work because list counts from 0 - (max-1)
# print(majors[3])


names.append("Shashank")
names.append("Skylar")
names.append("Dylan")
names.insert(1, "Amber")
names.append("Skylar")
print("The names after append are:", names)

#deleting an element
names.remove("Skylar")
print("The names after remove are:", names)

vicitm = names.pop(2)
print("The victim is:", vicitm)
print("The names after pop are:", names)

names.reverse()
print("The names in reverse:", names)

#sorting
names.sort()
print("The sorted names(a-z):", names)
names.sort(reverse=True)
print("The sorted names(z-a):", names)


