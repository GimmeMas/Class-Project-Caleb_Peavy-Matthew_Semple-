import re

def check_password_strength(password):
    # Define the criteria for a strong password
    length_criteria = len(password) &gt;= 8
    digit_criteria = re.search(r"\d", password)
    uppercase_criteria = re.search(r"[A-Z]", password)
    lowercase_criteria = re.search(r"[a-z]", password)
    special_char_criteria = re.search(r"[!@#$%^&amp;*(),.?\":{}|&lt;&gt;]", password)

    # Check if all criteria are met
    if length_criteria and digit_criteria and uppercase_criteria and lowercase_criteria and special_char_criteria:
        return "Strong"
    else:
        return "Weak"

# Example usage
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"The password strength is: {strength}")
# This code checks if the password meets the following criteria:
# 1. At least 8 characters long
# 2. Contains at least one digit
# 3. Contains at least one uppercase letter
# 4. Contains at least one lowercase letter
# 5. Contains at least one special character

if x:
    print("Not a Valid Password")
