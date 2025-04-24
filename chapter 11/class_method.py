class employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class value is {cls.a}")


emp = employee()
emp.a = 45

emp.show()
# employee.show(emp)