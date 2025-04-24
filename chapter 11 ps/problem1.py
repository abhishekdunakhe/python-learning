class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"This is my 2D vector {self.i}, {self.j}.")
    
class ThreeDvector(TwoDvector):
    def __init__(self,i, j, k):
        super().__init__(i, j)   
        self.i = i
        self.j = j
        self.k = k
        
    def show(self):
        print(f"This is my 3D vector {self.i}, {self.j}, {self.k}.")


a = TwoDvector(3, 5)
a.show()
b = ThreeDvector(7, 4, 9)
b.show()