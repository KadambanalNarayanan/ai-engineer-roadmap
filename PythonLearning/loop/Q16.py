"""
Question 14 – Nested Loop Pattern (Number Pattern)

Write a program to print:

1
12
123
1234
12345
Requirements:
Use nested for loops.
Do not print each number manually.
Outer loop controls rows.
Inner loop prints numbers.

"""

for i in range(1,6):
    for j in range(1, i+1):
        print(j, end="")
    print("")