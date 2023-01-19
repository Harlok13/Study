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
