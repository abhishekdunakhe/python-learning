class Employee:
    langauge = "Python"
    salary = 8000

abhi = Employee()
abhi.langauge = "JavaScript"
print(abhi.langauge, abhi.salary)

# the langauge in output is JavaScript because instance attribute takes over class attributes