import re

def replace_spaces_with_underscores(s):
    return s.replace(' ', '_')

def starts_with_word(s, word):
    return s.startswith(word)

def ends_with_word(s, word):
    return s.endswith(word)

def to_title_case(s):
    return s.title()

def longest_word(s):
    return max(s.split(), key=len)

def shortest_word(s):
    return min(s.split(), key=len)

def reverse_words(s):
    return ' '.join(s.split()[::-1])

def is_alphanumeric(s):
    return s.isalnum()

def extract_digits(s):
    return ''.join(c for c in s if c.isdigit())

def extract_alphabets(s):
    return ''.join(c for c in s if c.isalpha())

def count_uppercase_letters(s):
    return sum(1 for c in s if c.isupper())

def count_lowercase_letters(s):
    return sum(1 for c in s if c.islower())

def swap_case(s):
    return ''.join(c.upper() if c.islower() else c.lower() for c in s)

def remove_word(s, word):
    return s.replace(word, '')

def is_valid_email(s):
    return bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', s))

# Test cases
s = 'Hello, World! This is a test string.'
print(replace_spaces_with_underscores(s))  # 'Hello,_World!_This_is_a_test_string.'
print(starts_with_word(s, 'Hello'))  # True
print(ends_with_word(s, 'string.'))  # True
print(to_title_case(s))  # 'Hello, World! This Is A Test String.'
print(longest_word(s))  # 'test'
print(shortest_word(s))  # 'a'
print(reverse_words(s))  # 'string. This is a test string.'
print(is_alphanumeric(s))  # False
print(extract_digits(s))  # ''
print(extract_alphabets(s))  # 'Hello, World! This is a test string.'
print(count_uppercase_letters(s))  # 0
print(count_lowercase_letters(s))  # 28
print(swap_case(s))  # 'hELLO, wORLD! tHIS IS A tEST sTRING.'
print(remove_word(s, 'World'))  # 'Hello, ! This is a test string.'
print(is_valid_email('test@example.com'))  # True
print(is_valid_email('test@.com'))  # False