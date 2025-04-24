a1 = int(input("Enter Number one: "))
a2 = int(input("Enter Number two: "))
a3 = int(input("Enter Number three: "))
a4 = int(input("Enter Number four: "))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print(f"Greatest Number is {a1}")

elif(a2 > a1 and a2 > a3 and a2 > a4):
    print(f"Greatest Number is {a2}")

elif(a3 > a1 and a3 > a2 and a3 > a4):
    print(f"Greatest Number is {a3}")

elif(a4 > a1 and a4 > a2 and a4 > a3):
    print(f"Greatest Number is {a3}")

else:
    print("Khatm")