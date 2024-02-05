import string
from collections import Counter
import re

# Function 1
def extract_domain(email):
    return email.split('@')[-1].split('.')[0]

# Function 2
def remove_multiple_spaces(string):
    return ' '.join(string.split())

# Function 3
def is_valid_url(url):
    pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return bool(pattern.match(url))

# Function 4
def extract_protocol(url):
    pattern = re.compile('(http[s]?://)')
    match = pattern.match(url)
    return match.group(1) if match else None

# Function 5
def character_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Function 6
def remove_punctuation(string):
    return ''.join(char for char in string if char not in string.punctuation)

# Function 7
def is_digits_only(string):
    return string.isdigit()

# Function 8
def is_alphabets_only(string):
    return string.isalpha()

# Function 9
def string_to_list(string):
    return list(string)

# Function 10
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# Function 11
def caesar_cipher_encode(string, shift):
    encoded = ''
    for char in string:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                encoded += chr((shifted - ord('a')) % 26 + ord('a'))
            else:
                encoded += chr((shifted - ord('A')) % 26 + ord('A'))
        else:
            encoded += char
    return encoded

# Function 12
def caesar_cipher_decode(encoded, shift):
    return caesar_cipher_encode(encoded, -shift)

# Function 13
def most_frequent_word(string):
    words = string.split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]

# Function 14
def unique_words(string):
    return set(string.split())

# Function 15
def syllable_count(string):
    syllables = 0
    words = string.split()
    for word in words:
        syllables += max(1, len(re.findall(r'[aiouy]', word, re.I)))

    return syllables

# Test cases
print(extract_domain('john.doe@example.com'))  # Output: example
print(remove_multiple_spaces('Hello     World'))  # Output: Hello World
print(is_valid_url('https://www.example.com'))  # Output: True
print(extract_protocol('https://www.example.com'))  # Output: https://
print(character_frequency('Hello World'))  # Output: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
print(remove_punctuation('Hello, World!'))  # Output: Hello World
print(is_digits_only('12345'))  # Output: True
print(is_alphabets_only('Hello World'))  # Output: False
print(string_to_list('Hello World'))  # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', '