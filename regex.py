import re
""" 
The RegEx imported library (re) will send out the  warning ´Unused import statement 'import re'´ until it has been used  
"""
regex = r"m"
# The re.match() function in Python is part of the re (regular expression) module and is used to search for a match
# of a pattern at the beginning of a string. If the pattern is found at the start of the string, re.match() returns
# a match object; otherwise, it returns None.
print(re.match(regex, "abel"))  # Return: None, because there aren't coincidence at the beginning of the string
print(re.match(regex, "Mono"))  # Return: None, because this function is capitalize sensitive
print(re.match(regex, " mona")) # Return: None, because the blanc space is a string character too
print(re.match(regex, "mana"))  # Return: <re.Match object; span=(0, 1), match='m'>, because the match start at index 0 to 1
print(re.match(regex, "mmmama"))    # Return: The same thing of the before line, because it just found the beginning match
