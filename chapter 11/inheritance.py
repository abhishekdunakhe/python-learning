class employee:
    company = "setoo"

    def emp(self):
        print(f"I am employee in {self.company}.")


class Manager(employee):
    designation = "manager"

    def manager(self):
        print(f"Im {self.designation} in {self.company} with skills {self.langauge} developer.")


a = employee()
b = Manager()

a.emp()
b.emp()