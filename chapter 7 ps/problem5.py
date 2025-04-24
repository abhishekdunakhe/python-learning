
# factorial means 
# 5! =  1 * 2 * 3 * 4 * 5

n = int(input("Enter Number..."))

fact = 1
for i in range(1, n+1):
    fact *= i

print(fact) 
