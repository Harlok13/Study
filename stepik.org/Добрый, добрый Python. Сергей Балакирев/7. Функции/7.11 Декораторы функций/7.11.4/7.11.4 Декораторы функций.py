
def get_dic(func):
    def wrapper(*args, **kwargs):
        return dict(zip(*func(*args, **kwargs)))
    return wrapper


@get_dic
def get_lst(s1, s2):
    return s1.split(), s2.split()


print(get_lst('house river tree car', 'дом река дерево машина'))
