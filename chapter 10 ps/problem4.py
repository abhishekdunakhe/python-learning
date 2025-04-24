class Calculator:

    def __init__(self, n):
        self.n = n
        # print(n)

    def square(self):
        print(self.n * self.n)

    def cube(self):
        print(self.n * self.n * self.n)

    def square_root(self):
        print(self.n ** 1/2)

    @staticmethod
    def hello():
        print("Hello there...")


a = Calculator(4)
a.hello()
a.square()
a.cube()
a.square_root()