####################################################

# List

"""
    Note :- We can Create List Using 2 ways
            1. Using Square Bracket []
            2. Using list() Function, Take Iterable as Parameter
"""

letter = ['a', 'b', 'c'] # List of Character
numbers = [1, 2, 3, 4] # List of Numbers
matrix = [ [1, 2], [3, 4] ]
combinedList = letter + numbers # Will Concat Both List
numberList = list(range(20)) # Using list() Method

print(matrix)
print(combinedList)
print(numberList)
print( len(numberList) ) # Length of List

####################################################

# Accessing Item in List

print( letter[0] ) # Print First Item of List
print( letter[-1] ) # Print Last Item of List

####################################################

# Unpacking List

"""
    Note:- While Unpacking List, Total Number of Element on Left Side Should Be Always Equal to Total Number of Element in List
"""

first, second, third, fourth = numbers # Long Process
first, *other = numbers # Storing Left Numbers in Variable- Argument
first, *other, last = numbers # If We Want First, Last and Others to be Stored Into Variable-Argument

print(first, other)

####################################################

# Iterate Over List

for char in letter: # Normal Iteration over List
    print(char)

for index, char in enumerate(letter): # Used When We Want Index Also With Value, Because enumerate Will Return Tuple Which Contain Index and Value eg. (0, 'a;)
    print(index, char)

####################################################

# Add or Remove Item From List

letter.append('d') # Add at Last of List
letter.insert(0, '-') # Add at Specific Index

print(letter)

letter.pop(0) # Remove From Last of List Using Index
letter.remove('d') # Remove First Occurrence of Matched Character, Used When We Don't Know Index

print(letter)

del letter[0:2] # Delete Any Number of Item From List

print(letter)

####################################################

# Sorting List

num = [3, 51, 2, 8, 6]
num.sort() # Sort in Ascending Order
num.sort(reverse=True) # Sort in Descending Order

####################################################

# Sorting a List of Tuples
items = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 20)
]

def sortItem(items):
    return items[1]

items.sort(key=sortItem) # Sort In Ascending Order
items.sort(key=sortItem, reverse=True) # Sort In Descending Order

print(items)

####################################################

# Lamdba Function

"""
    Note :- Lambda Function are Anonymous Function

    Syntax :- lambda parameter:expression
    Example :- lambda number:number + 1

    Note :- lambda is Keyword
"""

foods = [
    ("Food-1", 10),
    ("Food-2", 9),
    ("Food-3", 20)
]

foods.sort( key= lambda foods:foods[1] ) # Lambda Function to Sort In Ascending Order
foods.sort( key= lambda foods:foods[1], reverse=True ) # Lambda Function to Sort In Descending Order

print(foods)

####################################################

# Map Function 

"""
    Note :- map Function Will Tak 2 Parameter One is CallBack Function Which is used To Perform Task on Each Individual Element of Iterable and Second Paramter is Iterable
            map Function Return map Object which is also Iterable
            Syntax : map(callback, iterable)
            example : map(lambda item : item + 1, [1,2,3,4,5])
"""

products = [
    ("Apple", 100),
    ("Ball", 20),
    ("Cat", 150)
]

productPrices = list( map(lambda item : item[1], products) )
print(productPrices)

####################################################

# Filter Function

"""
    Note :- filter Function Will Tak 2 Parameter One is CallBack Function Which is used To Perform Task on Each Individual Element of Iterable and Second Paramter is Iterable
            filter Function Return filter Object which is also Iterable
            Syntax : filter(callback, iterable)
            example : filter(lambda item : item % 2 == 0, [1,2,3,4,5])
"""

naturalNumbers = list(range(1, 21))
evenNumbers = list( filter(lambda element : element % 2 == 0, naturalNumbers) )
print(evenNumbers)

####################################################

# List Comprehension

"""

    Note :- We Can Perform Every Task using List COmprehension, That We Achieve using map() and filter() Function
    Syntax : [ expression : iterable ]

"""

####################################################

# Zip Function

"""
    Note :- Used To Combine One or More List and Create List of Tuple
    Syntax :- zip(iterable1, iterable2, .....), Will Return Zip Object which is Iterable
    Example :- zip([1,2,3], [4,5,6])
    O/P :- [ (1, 4), (2, 5), (3, 6) ]
"""

list1 = [1,2,3]
list2 = [4,5,6]
print( list( zip(list1, list2) ) )

####################################################