class employee:
    name = "Abhishek"
    salary = 8000

    def __init__(self, name, salary, language): # dunder method in py 
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")


    def get_info(self):
        print(f"The salaray of {self.name} is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Afternoon..!")

abhishek = employee("Abhishek", 8000, "py")
abhishek.lang = "python"
print(abhishek.name, abhishek.salary, abhishek.language)
abhishek.get_info()