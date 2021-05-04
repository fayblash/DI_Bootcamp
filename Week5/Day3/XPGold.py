# Exercise 1 : Regular Expression #1
# Instructions
# Hint: Use the RegEx (module)
import re
# Use the regular expression module to extract numbers from a string.

# Example
def return_numbers(string):
     print ("".join(re.findall('\d+', string)))
# return_numbers('k5k3q2g5z6x9bn') 
# // Excepted output : 532569
return_numbers('k5k3q2g5z6x9bn')


# Exercise 2 : Regular Expression #2
# Instructions
# Hint: Use the RegEx (module)

# Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
# The name should contain only letters.
# The name should contain only one space.
# The first letter of each name should be upper cased.
def validate_name(name):
    pattern = '[A-Z]+[a-z]+$'
    # ^([A-Z]+\s)*[a-zA-Z0-9]+$
    if re.search(pattern, name):
        return True
    else:
        return False
your_name=input("Please enter your full name: ")
print(validate_name(your_name))
# Exercise 3: Python Password Generator
# Instructions
# Create a Python program that will generate a good password for you.

# Program flow:

# Ask the user to type in the number of characters that the password should have (password length) – between 6 and 30 characters.
# Validate the input. Make sure the user is inputing a number between 6 to 30. Create a loop which will continue to ask the user for an input until they enter one which is valid.



# Generate a password with the required length.

# Print the password with a user-friendly message which reminds the user to keep the password in a safe place!

# Rules for the validity of the password
import rstr

pw_string="[A-Z]\d[a-z][@#$%^&+=]"
i=4
pw_length=int(input("Enter a number between 6 and 30: "))
while i<pw_length:
    pw_string+="[A-Za-z\d@$%^&+=]"
    i+=1
print(rstr.xeger(pw_string))


# Each password should contain:
# At least 1 digit (0-9)
# At least 1 lower-case character (a-z)
# At least 1 upper-case character (A-Z)
# At least 1 special character (eg. !, @, #, $, %, ^, _, …)
# Once there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.

# Create a test function first!

# Do the following steps 100 times, with different password lengths:
# Generate a password.
# Test the password to ensure that:
# it fulfills all the requirements above (eg. it has at least one digit, etc.)
# it has the specified length.