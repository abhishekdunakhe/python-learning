class employee:
    name = "Abhishek"
    salary = 8000

    def get_info(self):
        print(f"The salaray of {self.name} is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Afternoon..!")

abhishek = employee()
abhishek.greet()
abhishek.get_info() 
# employee.get_info(abhishek) # this both meanings are same

# we wants to add self in function for collect object.
# we call the function with static method which does not required object.