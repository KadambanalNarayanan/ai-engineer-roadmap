"""
Write a program to print the multiplication table of 7.

Expected output:

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
Requirements:
Use a for loop.
Use range().
Store the table number in a variable:
number = 7
Use an f-string for formatting.

"""

number = 7

for index in range(1, 11):
    print(f"{number} x {index} = {number*index}")