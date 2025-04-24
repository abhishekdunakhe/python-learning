try:
    a = int(input("Enter number..."))
    b = int(input("Enter number..."))
    print(a/b)
except ZeroDivisionError as z:
    print(z)