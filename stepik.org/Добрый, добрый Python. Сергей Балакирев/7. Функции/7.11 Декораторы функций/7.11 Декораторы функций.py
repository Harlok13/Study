import time


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("---  some actions ---")
        result = func(*args, **kwargs)
        print("---  some actions ---")
        return result

    return wrapper


def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"


f = func_decorator(some_func)

tagged = f("python", "h1")
print(tagged)








def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"time: {dt} sek")
        return result

    return wrapper


@test_time
def get_nod_fast(a, b):
    while b > 0: a, b = b, a % b
    return a


@test_time
def get_nod_slow(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# get_nod_slow = test_time(get_nod_slow)
# get_nod_fast = test_time(get_nod_fast)

res1 = get_nod_slow(2, 100000000)
res2 = get_nod_fast(2, 100000000)
print(res1, res2)
