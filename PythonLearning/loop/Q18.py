"""

Question 16 – Find the Largest Number

Given:

numbers = [45, 12, 78, 34, 90, 23]

Write a program to find the largest number.

Expected output:

90
Requirements:
Use a for loop.
Do not use max().
Create a variable named largest.
Compare each number with largest.

"""

largest = 0
numbers = [45, 12, 78, 34, 90, 23]

for value in numbers:
    if largest < value:
        largest = value
print(largest)