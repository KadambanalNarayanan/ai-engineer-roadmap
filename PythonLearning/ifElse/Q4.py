"""
Write a program that:

    1. Creates these variables:
        age = 25
        has_license = True

    2. If the person is 18 or older and has a driving license, print:
        You can drive.

    Otherwise, print:
        You cannot drive.

Requirements
    Use if...else.
    Use the logical operator and.
    Use >= for the age check.
"""

age = 25
has_license = True

if age >= 18 and has_license is True:
    print("You can drive")
else:
    print("You cannot drive")