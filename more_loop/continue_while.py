# number = 1

# while number <=100:
#     if number % 2 != 0:
#         number = number + 1
#         continue

#     print(f"{number} is even number")
#     number+=1

# CORRECT_PASSWORD = "password"

# while True:
#     password = input("Enter the secret password:")
#     if password!=CORRECT_PASSWORD:
#         print("Incorrect password!")
#         continue
    
#     print("Welcome admin")
#     break

#show all numbers from 1-40 that are not multiple of 3
# for number in range(1,40):
#     if number % 3 == 0:
#         continue
#     print(number)


#your turn 4.0
CORRECT_PASSWORD = "Shh$3cret"
while True:
    password = input("Enter th password:")
    if password != CORRECT_PASSWORD:
        print("Incorrect password!")
        continue

    #if we get here the password is valid
    break
        

print("Welcome admin!")
