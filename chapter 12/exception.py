# try:
#     a = int(input("Hey, Enter a number..."))
#     print(a)
# except Exception as e:
#     print(e)

# print("Thank you..!")

try:
    a = int(input("Hey, Enter a number..."))
    print(a)

except ValueError as v:
    print("hey, I'm from v")
    print(v)

except Exception as e:
    print("hey, I'm from e")
    print(e)


print("Thank you..!")

# we can apply mutiple error in except.