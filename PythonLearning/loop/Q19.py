"""
Question 17 – Count Occurrences

Given:

numbers = [1, 2, 3, 2, 4, 2, 5]
search = 2

Write a program to count how many times search appears.

Expected output:

3
Requirements:
Use a for loop.
Use a counter variable named count.
Do not use .count().

"""

numbers = [1, 2, 3, 2, 4, 2, 5]
search = 2
count = 0

for value in numbers:
    if value == search:
        count+=1
print(count)