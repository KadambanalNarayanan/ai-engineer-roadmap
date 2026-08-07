"""

Question 12 – continue in a Loop

Now let's learn continue.

Write a program that prints numbers from 1 to 10, but skips even numbers.

Expected output:

1
3
5
7
9
Requirements:
Use a for loop.
Use range().
Use continue.
Do not use a nested if.

"""

for i in range(1,10):
    if i%2 == 0:
        continue
    print(i)
