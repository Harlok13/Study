from re import fullmatch


# def strip_comments(strng, markers=None):
#     lst = strng.split('\n')
#     for k, v in enumerate(lst):
#         for m in markers:
#             if m in v:
#
#                 lst[k] = v.partition(m)[0].rstrip(' '.join(markers))
#     return '\n'.join(lst)


def strip_comments(strng, markers=None):
    sentences = strng.split('\n')
    for marker in markers:
        sentences = [sentence.split(marker)[0].rstrip() for sentence in sentences]
    return '\n'.join(sentences)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

amount = 10
# def foo(amount):
#     if amount > 1:
#         # print(cost)
#         print(36.4 * foo(amount-1))



def factorial_recursive(n):
    print(round(n*34.6, 1))
    if n == 1:
        return 34.6
    else:
        return 34.6*factorial_recursive(n-1)

# foo(10)
print(factorial_recursive(10))
