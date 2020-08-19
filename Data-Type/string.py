# Creating String
str1 = 'Hello' # using single quotes
str2 = "Hello World" # using double quotes
str3 = """Hello There, My Gorgeous Friend""" # using triple quotes

print(str1)
print(str2)
print(str3)

# Accessing String
name = "Ajay Sharma"
print(name[1]) # accessing single character
print(name[1:6]) # slicing 1
print(name[1:-2]) # slicing 2

# Formatting String
print("Hello Mr. {}, How are you Mrs. {}".format("Ajay", "Lulu")) # Default Order Formatting
print("{1} {0} {2}".format("Ajay", "Sharma", "Pandat")) # Positional Order Formatting
print("{i} {j} {k}".format(k="Ajay", j="Pandat", i="Sharma")) # Keyword Order Formatting

"""
String Methods
NOTE:- All String return new value they do not change origina value
"""
str = "  GeeksForGeeks  "

print(str.capitalize()) # Capatilize first character of string
print(str.count("e")) # Return number of times specific character occour
print(str.endswith("s")) # Return true if string end with specific character
print(str.find("For")) # Find first occurence of specific character
print(str.join(["Hello", "World", "Friend"])) # Take all item in iterable and join them into one string
print(str.strip()) # Trin whitespace from both side
print(str.upper()) # Convert whole string to uppercase
print(str.lower()) # Convert whole string to lowercase
print(str.replace("For", " Hello ")) # Replace old string with new string