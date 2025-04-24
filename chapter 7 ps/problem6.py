
# n = int(input("Enter Number..."))

'''
for n = 5
    *
   ***
  *****
 *******
*********
'''
# end="" avoids new line in the program

n=5
for i in range(1,6):
    print(" " * (n-i), end="")
    print("8" * (i*2-1))