'''
    sum(8) = 1+2+3+4+5+6+7+8
    sum(n) = n + sum (n-1)
'''

def sum(n):
    if(n == 1):
        return 1
    
    return n + sum(n -1) 

print(sum(4))