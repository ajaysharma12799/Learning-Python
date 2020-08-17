"""
    We Will be seeing two approach for multiple input taking
    1. using String split() method
    2. using list comprehension
"""
name, age, marks = input("Enter Your Name, Age and Marks : ").split()

print("Name : {}, Age: {} and Marks : {}".format(name, age,marks))