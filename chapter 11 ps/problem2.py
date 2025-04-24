class Animals:
    def __init__(self):
        print("This is animal class.")
    
class pets(Animals):
    print(f"This is pets class from animal.")

class Dog(pets):
    print(f"This is dogs from pets.")

    @staticmethod
    def bark():
        print(f"I am dog. I'll bark.")

d = Dog()
d.bark()


