"""
    We Will be seeing two approach for multiple input taking
    1. using String split() method
    2. using list comprehension
"""

# Using Split Method
name, age, marks = input("Enter Your Name, Age and Marks : ").split()
print("Name : {}, Age: {} and Marks : {}".format(name, age,marks))

# Using List Comprehension
numbers = [1, 2, 3, 4, 5] 
square = [ n**2 for n in numbers ] # finding square of each number
print(square)

list1 = [ 1,3,2,5,4 ]
list2 = [ 7,6,1,3,9 ]
equalElement = [ i for i in list1 for j in list2 if i == j ] # finding if both list contain equal element or not
print(equalElement)