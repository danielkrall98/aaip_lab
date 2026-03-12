from aaip.ex3 import Person, Student

# Demo of Person Class (Instance from String)
person_string = "Alice,26,Street 1"
alice = Person.from_string(person_string)
print(alice.greet())

# Demo of Student Class
bob = Student("Bob", 22, "Street 2", "PLUS")
print(bob.greet())
