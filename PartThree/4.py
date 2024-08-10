# Write a program that takes a user’s bank account number as input. The program should first check if the account number is at least 12 digits long.
# If it is not, indicate(print) that the account number is invalid. If the account number is 12 digits or longer,
# check if the last 4 digits of the account number are all zeros. If they are, indicate (print) that the account number is valid. Otherwise,
# indicate(print) that the account number is invalid.

account_number = input("Enter your account number: ")

if (len(account_number) >= 12):
    if (account_number[-1] == "0" and account_number[-2] == "0" and account_number[-3] == "0" and account_number[-4] == "0"):
        print("Valid Account Number")
else:
    print("Invalid Account Number!")
