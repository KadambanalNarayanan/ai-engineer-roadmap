"""


Write a program for a simple login check.

Given:

    correct_username = "admin"
    correct_password = "python123"

    username = "admin"
    password = "python123"

Rules:

    1. If the username is correct:
        -Check if the password is correct.
        -If both match, print:
            Login successful.
        -If password is wrong, print:
            Incorrect password.
    2. If username is wrong, print:
        Invalid username.

Requirements:
-Use nested if.
-Do not use and.
-Use string comparison.


"""

correct_username = "admin"
correct_password = "python123"

username = "admin"
password = "python123"

if username is correct_username:
    if password is correct_password:
        print("Login succesful.")
    else:
        print("Incorrect password")
else:
    print("Invalid user name")