class employee:
    company = "setoo"
    def __init__(self):
        print("employee")
    a=1

class Coder(employee):
    langauge = "python"
    def __init__(self):
        print("coder")
    b = 2

class Manager(Coder):
    designation = "manager"

    def __init__(self):
        super().__init__()
        print("manager")
    c = 3

b = Manager()
print(b.a, b.b, b.c)