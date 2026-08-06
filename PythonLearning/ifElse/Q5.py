"""

Write a program that:

    1. Creates:
        is_weekend = True
        is_holiday = False
    2. If it is a weekend OR a holiday, print:
        You can relax today.

    Otherwise print:
        You have to work today.

Requirements:
    Use if...else.
    Use the or operator.
    Do not use nested if.

"""

is_weekend = True
is_holiday = False

if is_holiday or is_weekend:
    print("You can relax today.")
else:
    print("You have to work today.")