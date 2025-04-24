age:int = 25

def greeting(name : str):
    return f"{name} is {age} old."

print(greeting("Abhishek"))



def sum(a : int, b : int):
    c = a + b
    print(type(c))
    return f"The sum of {a} and {b} is {c}"
    
sum(2,3)