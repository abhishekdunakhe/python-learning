class programmer:
    company = "Microsoft"
    def __init__(self, name , salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

abhi = programmer("Abhishek", 8000, 413104)
print(abhi.name, abhi.salary, abhi.pincode)

a = programmer("A", 12000, 413103)
print(a.name, a.salary, a.pincode)