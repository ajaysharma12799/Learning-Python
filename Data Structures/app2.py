####################################################

# Tuples

"""
    Note :- Tuple are Read-Only or Immutable
"""

a = 1, # When we add Comma after Value Then It Will Become Tuple
b = (1, 2) # Creating Tuple Using Paranthesis
c = tuple([1, 2, 3]) # Creating Tuple From List

####################################################

# Swap Number

x = 10
y = 20
x, y = y, x # Packing and UnPacking of Tuple
"""
    Note :- Process Involved in Swapping Number is of Packing and Unpacking of Tuple
            In Right Side We are Creating Tuple
            In Left Side We are UnPacking Tuple
"""
print(x, y)

####################################################

# Set

numbers = [1, 2, 3, 1, 4, 5]
unique = set(numbers) # Creating Set Using set() method
numberSet = { 1, 2, 3, 6, 7 }

print(unique)
print( unique | numberSet ) # Union of 2 Set
print( unique & numberSet ) # Intersection of 2 Set
print( unique - numberSet ) # Difference of 2 Set

"""
    Note :- Set Does't Support Indexing
"""

####################################################

# Dictionaries

phoneBook = { "Ajay" : 1, "Sharma" : 2 } # Creating using Curly Bracket
record = dict(x=1, y=2) # Creating Dictionary using dict() Function

print(record.get('x', 0)) 
"""
    Note :-
        Will Check For Key Which is Passed and If Not Found Will Return "None", 
        But If We Don't Want to Return "None" then we can Pass Second Parameter anything that we want to Return
"""

print(record)
print(phoneBook)

####################################################

# UnPacking Operator

"""
    Note :- We Can Use * To UnPack Value From Any Iterable and ** To UnPack Value From Dictionary
"""

first = { "x": 10 }
second = { "X": 100, "y": 20 }
combined = { **first, **second } ## UnPacking Both Dictionary and Creating New Dictionary

print(*"Hello") # Will UnPack Each and Every Character of String

print(combined)

####################################################