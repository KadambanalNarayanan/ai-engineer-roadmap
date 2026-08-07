"""
Question 24 – Second Largest Number (Interview Favorite)

This is a very common interview question.

Given:

numbers = [45, 12, 78, 34, 90, 23]

Write a program to find the second largest number.

Expected output:

78
Requirements
Use a for loop.
Do not use sort().
Do not use max().
Use two variables:

"""

numbers = [45, 12, 78, 34, 90, 23]

largest = numbers[0]
second_largest = numbers[0]

for index in range(1, len(numbers)):
    if largest < numbers[index]:
        second_largest = largest
        largest = numbers[index]
    elif largest > numbers[index] and second_largest < numbers[index]:
        second_largest = numbers[index]
print(second_largest)
    