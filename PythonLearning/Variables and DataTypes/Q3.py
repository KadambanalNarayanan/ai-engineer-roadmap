'''
This question introduces one of the most important Python concepts.
Write a program that:
    1. Create a variable:
        x = 100
    2. Assign another variable:
        y = x
    3.Print:
        - x
        - y
        - id(x)
        - id(y)
    4. Finally, print the result of:
        - print(x is y)

'''

x = 100
y = x
print(x)
print(y)
print(id(x))
print(id(y))
print(x is y)


'''
Additional checks
'''
print("Changing value of y")
y = 200
print(id(x))
print(id(y))
print(x is y)
