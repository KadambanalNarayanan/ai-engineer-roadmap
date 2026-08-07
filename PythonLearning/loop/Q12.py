"""

Question 11 – break in a for Loop

Write a program that searches for a number in a list.

Given:

numbers = [10, 20, 30, 40, 50]

Search for:

search = 30

Rules:

Loop through the list.
If the number is found, print:
    Number found
Stop the loop immediately using break.
If the loop finishes without finding the number, print:
    Number not found
Requirement:

Use:
for loop
break
else with the for loop (Python's special loop else)

"""

numbers = [10, 20, 30, 40, 50]
search = 30
for value in numbers:
    if value == search:
        print("Number found")
        break
else:
    print("Number not found")
    
