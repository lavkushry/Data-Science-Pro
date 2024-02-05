#Count the number of vowels in a string.
# def reverse_string(s):
#     return s[::-1]
#
# def is_palindrome(s):
#     return s.lower() == s[::-1].lower()
#
# def to_uppercase(s):
#     return s.upper()
#
# def to_lowercase(s):
#     return s.lower()
#
# def count_vowels(s):
#     return sum(1 for c in s if c.lower() in 'aeiou')
#
# def count_consonants(s):
#     return sum(1 for c in s if c.lower() not in 'aeiou')
#
# def remove_whitespaces(s):
#     return s.replace(' ', '')
#
# def string_length(s):
#     return sum(1 for _ in s)
#
# def contains_word(s, word):
#     return word in s.split()
#
# def replace_word(s, old_word, new_word):
#     return s.replace(old_word, new_word)
#
# def count_occurrences(s, word):
#     return s.split().count(word)
#
# def find_first_occurrence(s, word):
#     try:
#         return s.split().index(word)
#     except ValueError:
#         return -1
#
# def find_last_occurrence(s, word):
#     words = s.split()
#     return len(words) - 1 - words[::-1].index(word)
#
# def split_string(s):
#     return s.split()
#
# def join_words(words):
#     return ' '.join(words)

# Test caseslo,', 'World!', 'This', 'is', 'a', 'test', 'string.']))  # 'Hello, World! This is a test string.'

def countVowel(s):
    # Convert the string to lowercase, remove spaces
    return sum(1 for c in s if c.lower() in 'aeiou')


print(countVowel('Racecaraeiou'))