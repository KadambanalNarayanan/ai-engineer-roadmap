"""

Write a program for an ATM withdrawal.

Given:
    balance = 5000
    withdraw_amount = 3000

Rules:
    1. First check if the withdrawal amount is positive (> 0).
    2. If it is positive, then check whether the balance is enough.
    3. If balance is enough, print:
        Withdrawal successful.
    4. If balance is not enough, print:
        Insufficient balance.
    5. If withdrawal amount is zero or negative, print:
        Invalid withdrawal amount.

Requirements:
-Use nested if.
-Use else.
-Use comparison operators.
-Do not use and yet (we are practicing nesting).

"""

balance = 5000
withdraw_amount = 3000
if withdraw_amount > 0:
    if balance > withdraw_amount:
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")
else:
    print("Invalid withdrawal amount")