import datetime
import time
import validate_string as v



def test_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper


@test_time
def cycle(iter_obj):
    return [item for item in iter_obj if not (isinstance(item, str) and item.isalpha())]


@test_time
def filter_(iter_obj):
    return list(filter(lambda item: not (isinstance(item, str) and item.isalpha()), iter_obj))


if __name__ == '__main__':


    res1 = cycle(v.list_in)
    res2 = filter_(v.list_in)
