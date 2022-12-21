import time


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
def get_lst_app(var: list):
    lst = []
    for i in var:
        lst.append(i)
    return lst

@test_time
def get_lst_sum(var):
    lst = []
    for i in var:
        lst += [i]
    return lst



*var, = range(100000000)
res1 = get_lst_app(var)
res2 = get_lst_sum(var)
print(res1, res2)
