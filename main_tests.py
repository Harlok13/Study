from string import ascii_uppercase as asc
from re import sub


def solution(s: str) -> str:
    camel = [i for i in s if i in asc]
    r = s
    for i in camel:
        r = sub(fr'{i}', fr' {i}', r)


    # res = sub(fr'{c[0]}', fr' {c[0]}', s)
    # res1 = [sub(fr'{i}', fr' {i}', s) for i in c]
    return r


print(solution("publicNextEyeAdjectivesChild"))
