"""
Question 18 – Find Even and Odd Numbers

Given:

numbers = [10, 15, 20, 25, 30, 35]

Write a program that prints:

Even numbers:
10
20
30

Odd numbers:
15
25
35
Requirements:
Use a for loop.
Use % operator.
Use if-else.
Do not create separate lists.

"""

numbers = [10, 15, 20, 25, 30, 35]

print("Even numbers:")

for value in numbers:
    if value % 2 == 0:
        print(value)

print("Odd numbers:")

for value in numbers:
    if value % 2 != 0:
        print(value)