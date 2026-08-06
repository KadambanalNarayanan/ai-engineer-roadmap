"""

Now let's practice the third logical operator: not.

Write a program that:
    1. Creates:
        is_logged_in = False
    2. If the user is not logged in, print:
        Please login first.

    Otherwise, print:
        Welcome back!

Requirements:
Use if...else.
Use the not operator.
Do not compare directly like is_logged_in == False.

"""

is_logged_in = False
if not is_logged_in:
    print("Please login first.")
else:
    print("Welcome back!")