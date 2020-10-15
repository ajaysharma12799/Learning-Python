print("Importing My Custom Module")

def find_Index(toSearch, array):
    for i, value in enumerate(array):
        if value == toSearch:
            return value
    return "Not Found"