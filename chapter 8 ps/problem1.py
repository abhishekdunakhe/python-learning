
def greaterNumber(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c

a = int(input("Enter Number..."))
b = int(input("Enter Number..."))
c = int(input("Enter Number..."))
print(f"The greatest number is {greaterNumber(a,b,c)}")