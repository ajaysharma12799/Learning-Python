####################################################
import math
# Numbers

integer = 1000 # Integer
floating = 4.99 # Float or Decimal
imaginary = 1 + 5j # Complex Numbers or Imaginary Numbers

####################################################

# Operations on Number

print( 10 + 3 )
print( 10 - 3 )
print( 10 * 3 )
print( 10 / 3 ) # Return Floating Value
print( 10 // 3 ) # Return Integer Value
print( 10 % 3 )
print( 10 ** 3 ) # Return Exponent, Which is Left to the Power of Right ( 10^3 )

####################################################

# ShortHand Operators

x = 10
x += 3

print(x) # We can use Shorthand Operator With Every Operator Except ( Modulous and Exponent )

####################################################

# Number Functions

print( round(2.9) )
print( abs(-2.9) )
print( math.ceil(2.2) ) # Using Function From External Module

""" 
    Note :- We Dont Have Many Functions To Work With Numbers, So In That Case We Need 
            To Use External Math Module
"""

####################################################

# Type Conversion

x = input("Enter value") # Return String
convertedInt = int(x) # Type Conversion into Int
convertedFloat = float(x) # Type Conversion into Float
convertedBool = bool(x) # Type Conversion into Boolean
convertedString = str(x) # Type Conversion into String, But We Don't Need to Use It as By Default it is String

print( type(x) )

"""
    Truthy and Falsy Value
    Falsy Value are :-
    {
        "" : Empty Strings
        0 : Zero
        None : Nothing 
    }

    Note :- Except Falsy value all are Truthy Values
"""

####################################################