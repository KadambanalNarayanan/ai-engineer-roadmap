"""
Now improve the password system.

Requirements:

Maximum 3 attempts allowed.
After 3 wrong attempts, print:
Account locked
If the password is correct within 3 attempts, print:
Access Granted

Given:

correct_password = "python123"
Rules:
Use a while loop.
Use a counter variable.
Use break.
Use if...else.

"""

correct_password = "python123"
attempts = 0
while 1:
    print(f"Attempt {attempts + 1}")
    input_password = input("Enter password: ")
    if input_password == correct_password:
        print("Access Granted")
        break
    else:
        attempts+=1
        if attempts > 3:
            print("Account locked")
            break
