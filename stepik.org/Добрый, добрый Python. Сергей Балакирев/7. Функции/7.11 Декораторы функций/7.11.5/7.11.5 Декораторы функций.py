from string import ascii_lowercase
def get_strip(func):
    """Удаление лишних символов"""
    def wrapper(*args, **kwargs):
        return ''.join(func(*args, **kwargs)).replace('---', '-').replace('--', '-').rstrip('-').lstrip('-')

    return wrapper


@get_strip
def translate(s):
    """Перевод текста транслитом"""
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

    return [t.get(i, '-') if not i in ascii_lowercase and not i in '!?' else i for i in s.lower()]


print(translate('    Python -    - Это : ;.,_ круто!  '))
