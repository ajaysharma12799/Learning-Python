"""
    In this we will be using end, sep and format method in print function
"""

# using end, if we will not use end then our print function will end at new line
"""
    name = input("Enter Name : ")
    age = input("Enter Age : ")

    print(name, age, end=" ")
"""
# using sep, this is used to seperate data in print function
number = int(input("Enter Range : "))
for i in range(1, number + 1):
    print(i, sep='@', end=" ")