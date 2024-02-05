def is_palindrome(s):
    # Convert the string to lowercase, remove spaces
    s = s.lower().replace(' ', '')

    # Compare the string with its reversed version
    return s == s[::-1]

print(is_palindrome('racecar'))  # Returns: True
print(is_palindrome('hello'))    # Returns: False