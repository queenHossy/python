# This problem is "Vanity Plates" (plates.py) from CS50P.

# The goal is to check if a custom vanity license plate meets Massachusetts rule

# 1. Length: Must contain between 2 and 6 characters (letters/numbers).

# 2. Start: Must start with at least two letters.

# 3. Number Placement: Numbers must come at the end, not in the middle. (e.g., AAA222 is valid, but AAA22A is invalid).

# 4. First Number Rule: The first number used cannot be a '0' (e.g., CS05 is invalid, but CS50 is valid).

# 5. No Punctuation: No spaces, periods, commas, or special marks allowed.


def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Rule 1: length must be between 2 and 6 characters
def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

# Rule 2: must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

# Rule 5: no spaces, punctuation, or special characters (must be alphanumeric)
    if not s.isalnum():
        return False
# Rule 4&3: check number placement and first number rule
    i = 0
    while i < len(s):
        if s[i].isdigit(): # Look for the first digit in the string
# Rule 4: The first digit cannot be '0'
            if s[i] == '0':
                return False

# Rule 3: All characters after the first digit must also be digits
            if not s[i:].isdigit():
                return False

# Break out of the loop once numbers are verified
            break
        i += 1
    return True

if __name__ == "__main__":
      main()


# How the Validation Rules Work
# 2 <= len(s) <= 6: Handles length limits. Rejects inputs like "GOODBYE" (7 characters) shown in your screenshot.
# s.isalnum(): Rejects symbols or spaces, such as "HELLO, WORLD" (which contains a comma and space).
#  s[0].isalpha() and s[1].isalpha(): Ensures the plate starts with two letters. Rejects inputs like "50CS" or "C50".
# s[i] == '0': Ensures the first number isn't a zero (e.g., "CS05" is invalid).
# s[i:].isdigit(): Ensures that once a number appears, every character until the end of the plate is also a number (e.g., "CS50P" is invalid because P appears after 50).
