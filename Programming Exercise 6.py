# ============================================
# Name: Ayan Echemendia-Carranza
# Course: COP2373
# Program: Validation using Regular Expressions
# ============================================

# Import regular expression module
import re


# --------------------------------------------------
# Function: validate_phone
# Description: Checks if the phone number entered
# is in a valid format such as 123-456-7890
# --------------------------------------------------
def validate_phone(phone):

    pattern = r'^\d{3}-\d{3}-\d{4}$'

    if re.match(pattern, phone):
        return True
    else:
        return False


# --------------------------------------------------
# Function: validate_ssn
# Description: Checks if the SSN entered is valid
# format such as 123-45-6789
# --------------------------------------------------
def validate_ssn(ssn):

    pattern = r'^\d{3}-\d{2}-\d{4}$'

    if re.match(pattern, ssn):
        return True
    else:
        return False


# --------------------------------------------------
# Function: validate_zip
# Description: Checks if the ZIP code is valid
# formats: 12345 or 12345-6789
# --------------------------------------------------
def validate_zip(zip_code):

    pattern = r'^\d{5}(-\d{4})?$'

    if re.match(pattern, zip_code):
        return True
    else:
        return False


# --------------------------------------------------
# Function: main
# Description: Gets user input and displays whether
# the phone, ssn, and zip code are valid
# --------------------------------------------------
def main():

    # Get user input
    phone = input("Enter phone number (XXX-XXX-XXXX): ")
    ssn = input("Enter SSN (XXX-XX-XXXX): ")
    zip_code = input("Enter ZIP code: ")

    print()

    # Validate phone number
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    # Validate SSN
    if validate_ssn(ssn):
        print("SSN is valid.")
    else:
        print("SSN is invalid.")

    # Validate ZIP code
    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")


# Run the program
main()