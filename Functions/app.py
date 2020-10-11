####################################################

# Functions

def greet():
    print("Hi There")
    print("Welcome Abroad")

greet()

####################################################

# Arguments and Parameters in Function

def add(num1, num2): # Parameters are Input Defined For Function
    print(num1 + num2)

add(5, 5) # Arguments are Value Passed Into Function

####################################################

# Type of Functions

"""
    Note :- We Have 2 Type of Functions
            1. Performa Task
            2. Return a Value
    
    Note :- All Function Return None By Default, Until and Unless You Explicitly Return Value

"""

def printName(firstname, lastname):
    return f"firstname : {firstname} == lastname : {lastname}"

print( printName("ajay", lastname="sharma") ) # Using Keyword Argument

####################################################

# Default Argument

def addNumber(num1, num2 = 10): # Adding Default Parameter
    print(num1 + num2)

# addNumber(5)
addNumber(3, 5)

####################################################

# *args 
"""
    Note :- *args Will Create a Tuple, Which is Non-Mutable
"""

def multiply(*numbers): # Asterisk is used For Non-Keyword Arguments ( SImply Means Can Take Variable Number of Arguments )
    total = 1
    for number in numbers:
        total *= number
    return total

print( multiply(1, 2, 3, 4, 5) )

####################################################

# **args 
"""
    Note :- **args Will Create a Dictionary
"""

def save_user(**user):
    print(user)

save_user( id=1, name="ajay sharma", roll=20 )

####################################################

# Scope ( Global and Local Variables )

message = "Global Message"

def showMessage():
    global message
    message = "Local Message"


showMessage()
print( message )

"""

Note :- Do not Change Global Variable, Only Do If It Is Necessary

"""

####################################################