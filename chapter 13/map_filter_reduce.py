from functools import reduce
# map function
l = [2,4,3,6]
square = lambda x : x*x
squareList = map(square, l)
print(list(squareList))

# filter function

def even(n):
    if(n%2 == 0):
        return True
    return False

evenList = filter(even, l)
print(list(evenList))

# reduce
def sum(a, b):
    return a + b

print(reduce(sum, l))