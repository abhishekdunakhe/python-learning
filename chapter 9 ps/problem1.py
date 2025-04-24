f = open("chapter 9 ps/poem.txt")
content = f.read()
if("kjmj" in content):
    print("Is Present..!")
else:
    print("Not Present..!")
# print(content)
f.close()