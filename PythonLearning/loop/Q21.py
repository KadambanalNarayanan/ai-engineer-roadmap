"""
Question 19 – Prime Number Checker

A prime number is a number that is divisible only by:

1
itself

Examples:

2 → Prime
3 → Prime
4 → Not Prime (divisible by 2)
5 → Prime

Write a program to check whether a given number is prime.

Given:

number = 17

Expected output:

Prime number
Requirements:
Use a for loop.
Use % operator.
Use break.
Use a flag variable (example: is_prime = True).
Do not use any built-in prime checking functions.

💡 Logic hint:

Assume the number is prime.
Check divisibility from 2 up to number - 1.
If divisible, change the flag and stop the loop.

"""

number = 17

for val in range(2,number):
    if number%val == 0:
        print(f"Not Prime(divisible by {val})")
        break
else:
    print("Prime Number")