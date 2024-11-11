#there are two ways you can create a dictionary

#approach 1
print("Using approach 1")
students = dict()
print(students)

#approach 2
print("Using approach 2")
students = {}
print(students)

#creating dictionary with some data
student1_data = {
    "name":"John doe",
    "id":123457,
    "gpa":4.0,
    "is_suspend":False
}

print(student1_data)
print("The name of student 1 is:", student1_data["name"])
print("Change the gpa")
student1_data["gpa"] = 3.9
print("Student 1 data after changing the GPA")
print(student1_data)

print("Student 1 after is_on_dean_list")
student1_data["is_on_dean_list"] = True
print(student1_data)

#deleting is_on_dean_list key
del student1_data["is_on_dean_list"]
#notice, you can also use pop--> student1_data.pop("is_on_dean_list")
print("student 1 data after deleting the 'is_on_dean_list' key")
print(student1_data)

print("Check if the key 'name' is in the dictionary")
if "name" in student1_data:
    print("The key name is in the dictionary")
else:
    print("The key name is not in the dictionary")



keys = student1_data.keys()

print("The keys are:", keys)
print("the values are:", student1_data.values())

#you can check if something is in the values using in
if 123457 in student1_data.values():
    print("123457 is in the values")
else:
    print("123457 is not in the values")

#looping through a dictionary
print("Looping with keys only")
for key in student1_data:
    print(student1_data[key])

#looping with key and value
print("Looping with key and value")
for key,value in student1_data.items():
    print(f"{key}--->{value}")

print(student1_data["some_key_that_doesnt_exist_will_blow_up"])