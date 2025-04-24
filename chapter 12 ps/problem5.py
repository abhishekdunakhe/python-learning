n = int(input("Enter number..."))

tableList = [i*n for i in range(1,11)]

with open("chapter 12 ps/table.txt", "a") as f:
    f.write(str(tableList) + "\n")