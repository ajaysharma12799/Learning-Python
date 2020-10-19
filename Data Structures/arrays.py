from array import array

"""
    Note :- There are TypeCode in Python Array's Which Represent Value Stored into Array
            i => Integer [ Signed Int ]
            I => Integer [ UnSigned Int ]
            f, d => Float
            u => Character 
"""

value = array("i", [1,2,3,4,5])

print(value)
print( value.buffer_info() ) # Print Array Address and Number of Value Stored

"""
    Note :- All Operation and Methods Work Simillar Like They Work in List
"""

# Inserting Value in Array

arr = array("i", [])
n = int(input("Enter Size of Array : "))
for i in range(n):
    val = int(input("Enter Array value : "))
    arr.append(val)
print(arr)