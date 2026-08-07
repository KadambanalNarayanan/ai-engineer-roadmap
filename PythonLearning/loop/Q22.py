"""

Question 20 – Fibonacci Series (Classic Interview Question)

The Fibonacci sequence is:

0 1 1 2 3 5 8 13 21 34

Each number is the sum of the previous two.

Write a program to print the first 10 Fibonacci numbers.
Expected output
0
1
1
2
3
5
8
13
21
34
Requirements
Use a for loop.
Do not use recursion or lists.
Use three variables:
a
b
next_number

"""

a = 0
b = 1
print(a)
print(b)
for index in range(8):
    next_number = a+b
    a = b
    b = next_number
    print(next_number)