t = str.maketrans({'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'})


def dec(chars=' !?'):
    def outer(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs).replace(chars, '-').replace('---', '-').replace('--', '-')

        return wrapper
    return outer


@dec()
def translit(s):
    """Транслит строки"""
    return s.lower().translate(t).replace(' ', '-')


print(translit('простЩчков ап! R???--- !?'))

