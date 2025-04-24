a = int(input("Enter first number..."))
b = int(input("Enter second number..."))

if(b == 0):
    raise ZeroDivisionError("Zero is nit allowed in number.")

else:
    print(f"the division is {a/b}.")