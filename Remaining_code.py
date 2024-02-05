

def count_vowels(s):
    return sum(1 for c in s if c.lower() in 'aeiou')

def count_consonants(s):
    return sum(1 for c in s if c.lower() not in 'aeiou')

def remove_whitespaces(s):
    return s.replace(' ', '')

def string_length(s):
    return sum(1 for _ in s)

def contains_word(s, word):
    return word in s.split()

def replace_word(s, old_word, new_word):
    return s.replace(old_word, new_word)

def count_occurrences(s, word):
    return s.split().count(word)

def find_first_occurrence(s, word):
    try:
        return s.split().index(word)
    except ValueError:
        return -1

def find_last_occurrence(s, word):
    words = s.split()
    return len(words) - 1 - words[::-1].index(word)

def split_string(s):
    return s.split()

def join_words(words):
    return ' '.join(words)

# Test cases
s = 'Hello, World! This is a test string.'

print(count_consonants(s))  # 13
print(remove_whitespaces(s))  # 'Hello,World!Thisisateststring.'
print(string_length(s))  # 28
print(contains_word(s, 'World'))  # True
print(replace_word(s, 'World', 'Earth'))  # 'Hello, Earth! This is a test string.'
print(count_occurrences(s, 'is'))  # 2
print(find_first_occurrence(s, 'is'))  # 1
print(find_last_occurrence(s, 'is'))  # 17
print(split_string(s))  # ['Hello,', 'World!', 'This', 'is', 'a', 'test', 'string.']
print(join_words(['Hello,', 'World!', 'This', 'is', 'a', 'test', 'string.']))  # 'Hello, World! This is a test string.'