class employee:

    a = 2

    def show(self):
        print(f"The value of a is {self.a}")

    @property
    def name(self):
        return f"{self.firstName} {self.lastName}"

    @name.setter
    def name(self, value):
        self.firstName = value.split(" ")[0]
        self.lastName = value.split(" ")[1]

obj = employee()
obj.show()
obj.name = "Abhishek Dunakhe"
print(obj.name)