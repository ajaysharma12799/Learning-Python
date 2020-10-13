####################################################

# Classes

"""
    Note :- Python Object's are Dynamic Like JavaScript, So We Can Add Attributes and Methods
            Using Object Like We Add Properties and Methods using Prototype in JavaScript
"""

class Point: # Creating Class

    def __init__(self, x, y): # Creating Parametrize Constructor
        self.x = x
        self.y = y
    
    """
        Note :- There are 2 Constructor
                1. Default Constructor ( Without Parameter )
                    Eg. def __init__(self)
                
                2. Parametrized Constructor ( With Parameter )
                    Eg. def __init__(self, x, y)
    """

    @classmethod # Decorator
    def classMethod(cls): # Class Method
        print(cls)

    """
        Note :- Class Methods are Not Bound To Object, They are Bound To Class
                Class Methods use Decorator ( @classmethod )

                We Use Class Method to Create Factory-Method, Which Return Class Object Simillar to Class Constructor For Different Use Case

                Important :- Class Methods have Access To Class-State, So If They Modify
                            Anything into Class Then It Would Be Applicable To All Instance of That Class
        
        Note :- Instance Methods are Bound To Objects
    """

    def draw(self):
        print(f"X : {self.x}, Y : {self.y}")
        print(self)

point = Point(10, 20)
point.z = 200 # Adding Instance Attribute Using Object
point.draw()

####################################################

# Class vs Instance Attribute

"""
    Note :- There are 2 type of Attribute in Class
            1. Instance Attributes => Variable Defined in Methods of Class
               Eg. def __init__(self, value):
                        self.value = value # Instance Attribute
            
            2. Class Attribute => Variable Defined in Global Scope of Class
                Eg. class Point:
                        number = 10 # Class Attribute
"""

####################################################

# Magic Methods

class ABC:

    def __init__(self, x, y):
        self.x = 1
        self.y = 2
    
    def __eq__(self, other): # Magic Method For Checking If Both Object or Instance are Equal
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other): # Magic Method For Checking If Any One Object is Greater Than or Not
        return self.x > other.x and self.y > other.y

abc = ABC(1, 2)
bca = ABC(1, 2)

print(abc == bca)
print(abc > bca)

####################################################

# Private Variable

class PrivateVariable:
    def __init__(self, name):
        self.__PersonName = []
        self.name = name
    
    def pushName(self):
        self.__PersonName.append(self.name)

person = PrivateVariable("Ajay")
person.pushName()
print(person.__dict__)

####################################################

# Getter and Setter

class Product:
    def __init__(self, price):
        self.__productPrice = price
    
    def getPrice(self):
        return self.__productPrice
    
    def setPrice(self, price):
        self.__productPrice = price
    
    value = property(getPrice, setPrice)

x = Product(120)
print(x.value)

"""
    Note :- Making Getter and Setter is an Old Way, New Way is Using @property Decorator
"""

####################################################

# Getter and Setter Using Decorator

class Price:

    def __init__(self, price):
        self.__productPrice = price
    
    @property
    def Product_Price(self): # Getting Value
        return self.__productPrice
    
    @Product_Price.setter
    def Product_Price(self, price): # Setting Value
        self.__productPrice = price
    
value = Price(1200)
print(value.Product_Price)

####################################################