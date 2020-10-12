####################################################

# Exception

try:
    age = int(input("Enter Age : "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print(error)
else:
    print('No Exception is Thrown')
finally:
    print("Finally Block Will Always Work")

"""
    
    Note :- We Can Use "with" Statement to Handle External Resource
    
    eg :-   with open('file_path', 'w') as file: 
                file.write('hello world !') 
    
    Note :- If We are Using "with" Statement Then We Need Not To Use finally Statement

"""


####################################################

# Raising Excpetion

def calcAge(age):
    age = int(input('Enter Age : '))
    if age < 18:
        raise ValueError("Age is Less Than 18")
    else:
        print("Age is Above 18")

try:
    calcAge(-1)
except ValueError as error:
    print(error)

####################################################