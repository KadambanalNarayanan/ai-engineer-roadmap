"""

Write a program that keeps asking for a password until the correct password is entered.

Given:

correct_password = "python123"

The program should:

    1. Ask the user:
        Enter password:
    2. If the password is correct, print:
        Access granted

    and stop the loop.

    3. If the password is wrong, print:
        Incorrect password. Try again.

    and ask again.

Requirements:
    -Use a while loop.
    -Use input().
    -Use break to exit the loop when the password is correct.

"""
correct_password = "python123"
while 1:
    input_password = input("Enter the password:")
    if input_password == correct_password:
        print("Access Granted")
        break;
    print("Incorrect password. Try again")
