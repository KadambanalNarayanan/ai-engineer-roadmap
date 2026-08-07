"""
Question 23 – Reverse a String (Interview Favorite)

Given:

text = "Python"

Write a program to 
print the string in reverse.

Expected output:

nohtyP
Requirements
Use a for loop.
Do not use slicing ([::-1]).
Do not use reversed().
Create an empty string:
reverse = ""
Build the reversed string one character at a time.

"""

text = "Python"
reverse = ""
for index in range(len(text)-1, -1, -1):
    reverse+=text[index]
print(reverse)