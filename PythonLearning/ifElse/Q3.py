"""
Write a program that:

    1. Creates a variable:
        marks = 78
    2. Prints the grade according to these rules:
        - If marks are 90 or above → "Grade A"
        - Else if marks are 75 or above → "Grade B"
        - Else if marks are 60 or above → "Grade C"
        - Otherwise → "Grade D"
    3. Requirements
        - Use if, elif, and else.
        - Arrange the conditions correctly.
        - Print only one grade.
"""

marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")