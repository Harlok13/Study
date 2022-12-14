from re import fullmatch


def count_smileys(arr):
    return len([i for i in arr if fullmatch(r'[:;][-~]?[\)D]', i)])


arr = [';D', ':-(', ':-)', ';~)']
print(count_smileys(arr))
