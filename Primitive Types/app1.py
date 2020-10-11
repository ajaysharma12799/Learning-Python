####################################################

#   Data Types

students_count = 1000 # Integer Type
rating = 4.99 # Floating Type
isPublished = True # Boolean Type
course_name = "Python Programming" # String Type

####################################################

# Strings

print( len(course_name) ) # Length of String
print( course_name[0] ) # Extract Single Character From String and From Start
print( course_name[-1] ) # Extract Single Character From String and From End
print( course_name[0:3] ) # Slicing String, Exclude Last Index Which is Passed 
print( course_name[:] ) # Will Return Exact Copy of String

####################################################

# Escape Sequence

# \" => To Include Double Quote into String
# \' => To Include Single Quote into String
# \\ => To Include BackSlash into String
# \n => To Include New-Line into String

student_name = "Ajay \"Sharma" # BackSlash Used to Escape To Character
print(student_name)

####################################################

# String Formatting

first_name = "Ajay"
last_name = "Sharma"
print( f"FirstName : {first_name} \nLastName : {last_name}" )

####################################################

# String Functions

print( course_name.upper() ) # Convert String into UpperCase, but does not affect original String
print( course_name.lower() ) # Convert String into LowerCase, but does not affect original String
print( course_name.title() ) # Convert String First Letter into UpperCase
print( course_name.strip() ) # Remove White Space From Both Side of String
print( course_name.lstrip() ) # Remove White Space From Left Side
print( course_name.rstrip() ) # Remove White Space From Right Side
print( course_name.find("pro") ) # Find Specific String Passed Into and Return Index
print( course_name.replace("p", "j") )
print( "pro" in course_name ) # Boolean Value if Given String is Present in it
print( "Swift" not in course_name ) # Boolean Value if Given String is not Present in it

####################################################