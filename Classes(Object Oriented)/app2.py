####################################################

# Inheritance

class Animal: # Base Class
    def __init__(self):
        self.age = '1year'
    
    def eat(self):
        print("Eat")

class Fish(Animal): # Child Class Extending Base Class
    def __init__(self):
        super().__init__() # Calling Base Class Constructor
        self.weight = '12kg'

    def swim(self):
        print("Swim")
    
    def eat(self): # Method Overriding
        print('Fish Eat Fish Food')

animal = Animal()
fish = Fish()

animal.eat()
fish.swim()
fish.eat()

print(fish.age)
print(fish.weight)

####################################################

# Multi-Level Inheritance

"""
Note :- Multi-Level Inheritance Is Worst Case and It Bring Complexity to Software

        Example :- GrandFather => Father => Son

"""

####################################################

# Multiple Inheritance

class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Person, Employee):
    # def greet(self):
    #     print("Manager Greet")
    pass

manager = Manager()
manager.greet()

"""
    Note :- In Multiple Inheritance Which Constructor will be Called
            Example :- When Manager Class Call greet() Method then If greet() method is present
                       in Manager Class then it is called and if not present so the first class which is extended like in this 
                       case Person class is extending so if greet() is present in it then it is called like ways it goes on
"""

####################################################