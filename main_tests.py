from collections import Counter


def duplicate_count(text):
    res = Counter(text.lower())
    return res

print(duplicate_count('aabBcde'))
