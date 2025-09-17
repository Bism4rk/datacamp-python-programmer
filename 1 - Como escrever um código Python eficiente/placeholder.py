# Write some very inefficient code
def inefficient_function(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result

# Write some very efficient code with list comprehension
def efficient_function(n):
    return [i * j for i in range(n) for j in range(n)]