class Demo:
    a = 4

o = Demo()
print(o.a) # This takes value from class because instance variable is not added ye
o.a = 0    # Instance variable added
print(o.a) # This takes value from Instance varible. 
print(Demo.a)
# but original value of a = 4 in class does not changes