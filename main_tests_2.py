a = [{"text": "a", "b": {"text": "e", "again": [[1, {"text": "вот тут"}]]}}]


def findAll(where, what):
    result = {}

    def func(where, what, scope=""):
        if type(where) == dict:
            for key, value in where.items():
                cScope = f"{scope}.{key}" if scope else key
                func(value, what, cScope)
        elif type(where) == list:
            for index, value in enumerate(where):
                cScope = f"{scope}.{index}" if scope else str(index)
                func(value, what, cScope)
        else:
            if scope.endswith(what):
                result[scope] = where

    func(where, what)
    return result


result = findAll(a, "text")

for key, value in result.items():
    print(repr(key), ": ", repr(value), sep="")
