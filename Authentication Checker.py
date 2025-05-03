# Define password requirements
MIN_LENGTH = 8  # Minimum length for the password

# Function to check minimum length requirement
def has_min_length(password):
    return len(password) >= MIN_LENGTH

# Function to check if there's at least one uppercase letter in the password
def has_uppercase(password):
    return any(char.isupper() for char in password)

# Function to check if there's at least one lowercase letter in the password
def has_lowercase(password):
    return any(char.islower() for char in password)

# Function to check if there's at least one digit in the password
def has_digit(password):
    return any(char.isdigit() for char in password)

# Function to check if there's at least one special character in the password
def has_special_char(password):
    return any(char in "!@#$%^&*()-_+=<>?/" for char in password)

# Function to ensure the password does not contain the username
def does_not_contain_username(password, username):
    # Convert both to lowercase to check for case-insensitive matches
    return username.lower() not in password.lower()
  def validate_password(password, username):
    errors = []  # Initialize a list to collect error messages

    # Check each password requirement and append a message if it fails
    if not has_min_length(password):
        errors.append(f"Password must be at least {MIN_LENGTH} characters long.")
    if not has_uppercase(password):
        errors.append("Password must contain at least one uppercase letter.")
    if not has_lowercase(password):
        errors.append("Password must contain at least one lowercase letter.")
    if not has_digit(password):
        errors.append("Password must contain at least one digit.")
    if not has_special_char(password):
        errors.append("Password must contain at least one special character (!@#$%^&*()-_+=<>?/).")
    if not does_not_contain_username(password, username):
        errors.append("Password should not contain the username.")

    # If there are no errors, return success message; otherwise, return all error messages
    if not errors:
        return "Password is valid and secure!"
    else:
        return "\n".join(errors)

    # Import the 're' module for regular expressions
import re

# Prompt the user to input a password and store it in the variable 'p'
p = input("Input your password")

# Set 'x' to True to enter the while loop
x = True

# Start a while loop that continues until 'x' is True
while x:  
    # Check conditions for a valid password:
    # Password length should be between 6 and 12 characters
    if (len(p) < 6 or len(p) > 12):
        break
    # Password should contain at least one lowercase letter
    elif not re.search("[a-z]", p):
        break
    # Password should contain at least one digit
    elif not re.search("[0-9]", p):
        break
    # Password should contain at least one uppercase letter
    elif not re.search("[A-Z]", p):
        break
    # Password should contain at least one special character among '$', '#', '@'
    elif not re.search("[$#@]", p):
        break
    # Password should not contain any whitespace character
    elif re.search("\s", p):
        break
    else:
        # If all conditions are met, print "Valid Password" and set 'x' to False to exit the loop
        print("Valid Password")
        x = False
        break

# If 'x' remains True, print "Not a Valid Password"
if x:
    print("Not a Valid Password")
