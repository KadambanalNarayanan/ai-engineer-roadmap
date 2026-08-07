"""
Question 13 – Nested Loops (Important)

Now we enter a powerful topic: nested loops.

Write a program to print this pattern:

*
**
***
****
*****
Requirements:
Use nested for loops.
Do not manually write the stars.
Outer loop controls rows.
Inner loop controls stars in each row.

"""

for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print("")