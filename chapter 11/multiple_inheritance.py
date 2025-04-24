class employee:
    company = "setoo"

    def emp(self):
        print(f"I am employee in {self.company}.")


class Coder:
    langauge = "python"

    def coding(self):
        print(f"I am {self.langauge} developer.")


class Manager(employee,Coder):
    designation = "manager"

    def manager(self):
        print(f"Im {self.designation} in {self.company} with skills {self.langauge} developer.")


a = employee()

a.emp()


b = Manager()

b.emp()
b.coding()
b.manager()