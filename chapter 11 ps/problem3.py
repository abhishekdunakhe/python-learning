class Employee:
    salary = 8000

    @property
    def increment(self):
        return self.incrementedSalary

    @increment.setter
    def increment(self,value):
        print(value)
        self.incrementedSalary = self.salary + self.salary * (value/100)


e = Employee()
e.increment = 25
print(e.increment)