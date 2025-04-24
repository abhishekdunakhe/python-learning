# If we want's to run piece of code after successfully try block execution.

try:
    a = int(input("Enter a number..."))
    print(a)

except Exception as e:
    print(e)

else:
    print("I'm inside else.")