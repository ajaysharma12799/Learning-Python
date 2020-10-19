# OS Module

import os

"""
    Note:- Error raised by "OS Module" are "OSError"
"""


print(os.getcwd()) # Get Current Working Directory
print(os.name) # Print OS Name
print(os.environ) # Return Dictionary of user's Environment Variable
print(os.chdir(r"C:\Users\Ajay\Desktop")) # Used TO Change Working Directory

print( dir(os) ) # Return Sorted List of String, List Contain Name of variable and function defined in module
print( globals() ) # Return Name of Function that can be accessed globally from that function
print( locals() ) # Return Name of Function that can be accessed locally from that function