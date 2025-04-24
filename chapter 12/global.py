a = 100

def func():
    global a
    a = 10
    print(a)
    return 

func()
print(a)
