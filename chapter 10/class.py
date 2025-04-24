class Employee:
    lang = "python"
    salary = 8000

abhi = Employee()
abhi.name= "Abhi"
print(abhi.name, abhi.lang, abhi.salary)

abhishek = Employee()
abhishek.name = "Abhishek"  # instance variable
print(abhishek.name,abhishek.lang,abhishek.salary)


# here name is instance attribute, and lang, salary attribute directly belongs to class