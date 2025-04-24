'''
***
**
*
'''

n = 3

def printStar(n):
    if(n == 0):
        return
    print(f"*" * n)
    printStar(n-1)
printStar(5)