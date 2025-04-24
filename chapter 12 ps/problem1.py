try:
    with open("chapter 12 ps/file_1.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)


try:
    with open("chapter 12 ps/file_2.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("chapter 12 ps/file_3.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

print("Thank you..!")

