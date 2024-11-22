def sum_recursive(n):

    #set up the base case
    if n == 0:
        return 0

    #prevent negative n
    if n < 0:
        return 0

    #recursively call the function
    #we will keep track of the previous n + the sum of the next n-1
    return n + sum_recursive(n-1)

def sum_recursive_count_up(n):
    if n > 300:
        return 0
    if n == 300:
        return 300
    
    return n + sum_recursive_count_up(n+1)


result = sum_recursive(300)
result2 = sum_recursive_count_up(1)


print(result)
print(result2)