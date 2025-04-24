class Calculator:

    def __init__(self, n):
        self.n = n
        print(n)

    def square(self):
        print(self.n * self.n)

    def cube(self):
        print(self.n * self.n * self.n)

    def square_root(self):
        print(self.n ** 1/2)

a = Calculator(4)
a.square()
a.cube()
a.square_root()
