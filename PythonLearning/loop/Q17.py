"""
Next Level: Real-World Loop Problem
Question 15 – Find the Sum of Numbers

Write a program to calculate the sum of numbers from 1 to 10.

Expected output:

55
Requirements:
Use a for loop.
Use a variable named total.
Do not directly calculate 1+2+3....
Update total inside the loop.

"""

sum = 0
for i in range(1,11):
    sum+=i
print(sum)