class Person:
    def __init__(self, name:str, age:int, address:str):
        self.name = name
        self.age = age
        self.address = address

    def greet(self):
        return f"Hello, {self.name}!"
    
    # Create a Person from a String
    @classmethod #Decorator
    def from_string(cls, person_string:str):
        name, age, address = person_string.split(',')
        return cls(name, int(age), address)

# Extends Person
class Student(Person):
    def __init__(self, name:str, age:int, address:str, university:str):
        super().__init__(name, age, address)
        self.university = university

    def greet(self):
        return f"Hello, {self.name} from {self.university}"