"""
Input:
    A string

Output:
    True if the string is a palindrome, otherwise False.

Description:
    Check whether the given string is a palindrome.
"""

# Read the input string from the user.
input_string = input("Enter a string: ")

# Check if the string is equal to its reverse.
if input_string == input_string[::-1]:
    print(True)
else:
    print(False)