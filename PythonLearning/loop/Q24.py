"""
Question 22 – Nested Multiplication Tables

Now let's combine nested loops with formatted output.

Write a program that prints the multiplication tables from 2 to 5.

Expected output:

Table of 2
2 x 1 = 2
2 x 2 = 4
...
2 x 10 = 20

Table of 3
3 x 1 = 3
...
3 x 10 = 30

Table of 4
...

Table of 5
...
Requirements
Use nested for loops.
Outer loop should iterate through table numbers (2 to 5).
Inner loop should iterate through multipliers (1 to 10).
Print a blank line after each table for readability.

"""

for number in range (2, 6):
    print(f"Table of {number}")
    for index in range (1, 11):
        print(f"{index} x {number} = {index*number}")
    print("")