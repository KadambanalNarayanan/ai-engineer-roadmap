"""

This combines everything you've learned.

Write a program for an online shopping website.

Given:

amount = 1200
is_member = True

Rules
    1. If the amount is ₹1000 or more:
        - If the customer is a member, print:
            You get a 20% discount.
        -Otherwise, print:
            You get a 10% discount.

    2. If the amount is less than ₹1000, print:
        No discount available.
    Requirements
        -Use nested if.
        -Do not use and.
        -Use comparison operators.
        -Write clean, readable code.

"""

amount = 1200
is_member = True
if amount > 1000:
    if is_member :
        print("You get 20% discount.")
    else:
        print("You get 10% discount")
else:
    print("No discount available")
        