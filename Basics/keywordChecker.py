import keyword

keys = [ "for", "while", "tanisha", "break", "sky",
         "elif", "assert", "pulkit", "lambda", "else",
         "sakshar" ] # array of String which contain keywords and other string

# FUnction to check whether string contained in array contain any reserved word or not
for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i] + "is a Python Keyword")
    else:
        print(keys[i] + "is not a Python Keyword")

# Function to print all keyword in python
def printAllKeyword():
    keywords = keyword.kwlist
    for key in keywords:
        print(key)

printAllKeyword()