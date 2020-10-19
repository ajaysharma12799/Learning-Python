"""
    Note :- This File Contain Numpy Basics That is Required For Me To Complete My Work, Rest I Will Be Updating Later
"""

"""
    Numpy :- Used to Work With Multi-Dimensional Arrays, General Purpose Array Processing Package
    Note :- Array class in Numpy is called ndarray

    Note :- We Can Create Array From Any Sequence Like List, Tuple, etc
    Note :- The Type of Resultant Array is Explictely Deduced From The Given Sequence


"""
import numpy as np

# Creating Different Type of Array

arr1 = np.array([9,8,7,6,5]) # Single Dimensional Array or Rank-1 Array

arr2 = np.array([[1,2,3,4,5], [5,4,3,2,1]]) # Multi-Dimensional Array or Rank-2 Array

arr3 = np.array((10, 20, 30)) # Array using Tuple


print( arr1 )
print( arr2 )
print( arr3 )

# Some Array Operation

print( 'Adding 1 To Each Element : ', arr1 + 1)
print( 'Subtract 1 To Each Element : ', arr1 - 1)
print( 'Multiply 2 To Each Element : ', arr1 * 2)
print( 'Exponent 2 To Each Element : ', arr1 ** 2)

# Unary Operators

"""
    Note :- Many Unary Operator are Provided as Part of ndarray Class, These Include [ sum, min, max ]
            Important :- Unary Operator Can be Applied Row-Wise or Column-Wise Using [ axis ],
                         If axis is 0 then it is column-wise and If asix is 1 then it is row-wise
"""

print( "Sum of Array : ", arr1.sum() )
print( "Max Element of Array : ", arr2.max() )
print( "Min Element of Array : ", arr3.min() )

# Binary Operators

"""
    Note :- These Operator Work on Element Wise in Array
"""

num1 = np.array([[1,2,3], [4,5,6]])

num2 = np.array([[3,2,1], [6,5,4]])

print( "Addition of 2 Matrix Element-Wise : ", num1 + num2 )
print( "Subtraction of 2 Matrix Element-Wise : ", num1 - num2 )
print( "Multiplication of 2 Matrix Element-Wise : ", num1 * num2 )