import re

def is_valid_password(password):
    # Check if the password contains at least one lowercase letter (a-z)
    if not re.search(r'[a-z]', password):
        return False

    # Check if the password contains at least one digit (0-9)
    if not re.search(r'[0-9]', password):
        return False

    # Check if the password contains at least one uppercase letter (A-Z)
    if not re.search(r'[A-Z]', password):
        return False

    # Check if the password contains at least one special character from $, #, @
    if not re.search(r'[$#@]', password):
        return False

    # Check if the password has a minimum length of 6 characters
    if len(password) < 6:
        return False

    # If all conditions are met, the password is valid
    return True

# Input from the user
user_password = input("Enter a password: ")

# Check the validity of the password
if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is not valid. Please make sure it satisfies all the criteria.")
