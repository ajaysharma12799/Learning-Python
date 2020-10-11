####################################################

# Loops

"""

Note :- There are 3 Type of Loop
1. For Loop
2. Nested Loop
3. While Loop

Note :- There are Another Variant of Each Loop's With Else Statement Also.

"""

# 1. For Loop
for number in range(3): # By Default Start From 0 and Exclude Last Index
    print("Attempt", number + 1)

"""

range(start, end, steps) => {
    start : starting index
    end : ending index
    steps : number of steps or jump range function will be doing
}

"""

"""

Note :- We Have Jump Statement in Python
        1. break => Will Terminate Loop
        2. continue => Will Continue Iterating Loop ( Force Loop to Continue its Iteration )
        3. pass => Will Do Nothing, Simply Ignore ( Mostly Used To Place Future Code )

"""

# 2. Nested Loop
for i in range(5): # Outer Loop
    for j in range(3): # Inner Loop
        print( f"${i} : {j}" )

print( type(range(5)) ) # Will Return Iterable Object

"""

Note :- We Have Some of Complex Types
1. range
2. string
3. list


Note :- We Can Iterate over Iteratable

"""

# 3. While Loop

numbers = 100
while number > 0:
    print(numbers)
    numbers //= 2

####################################################