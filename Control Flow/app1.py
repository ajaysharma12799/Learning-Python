####################################################

# Comparasion Operators

print( 10 > 2 )
print( 10 >= 3 )
print( 10 < 2 )
print( 10 <= 2 )
print( 10 == "10" )
print( 10 != "10" )

####################################################

# Conditional Statement

temperature = 35
if temperature > 35:
    print("It's Warm")
    print("Drink More Water")
elif temperature > 20:
    print("It's Nice Weather")
    print("Drink Sufficient Amount Water")
else :
    print("It's Cold")

####################################################

# Ternay Operator

age = 22
message = "Eligible" if age > 18 else "Not Eligible"
print(message)

####################################################

# Logical Operators

"""

Note :- Evaluation of Conditional if Done From Left To Right

"""

"""
    We Have 3 Logical Operator
    1. and
    2. or
    3. not
"""

high_income = True
good_credit = True

if high_income and good_credit: # Will Give True If Both are True
    print("Eligible For Loan")
else:
    print("Not Eligible For Loan")

"""
# Will Give False If One is True and Second is False

if high_income or good_credit: 
    print("Eligible For Loan")
else:
    print("Not Eligible For Loan")

"""

"""

# not => Will Be Reverse of Condition, If True then False or If False then True

"""

####################################################