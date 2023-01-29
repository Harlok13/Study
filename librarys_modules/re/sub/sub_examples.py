import re


def split_string(sentence: str, *, sep: str = '.') -> list:
    """Делит строку по любым символам, которые не являются буквами"""
    pattern = ''.join((i for i in sentence if not i.isalpha()))
    print(pattern)
    res_strng = __import__('re').sub(fr'[{pattern}]', fr'{sep}', sentence.strip(pattern))
    return res_strng.split(sep)


if __name__ == '__main__':
    print(split_string('sdf,sdf;'))
    assert split_string('sdf,sdf;') == ['sdf', 'sdf']
    assert split_string('сколько.лет:сколько"зим') == ['сколько', 'лет', 'сколько', 'зим']
    assert split_string('не;много:не№мало!', sep='#') == ['не', 'много', 'не', 'мало']

    s = "134!%whatever5.wherever1^%$solution;solut1onal!"
    s = re.search(r"[a-zA-Z]+.*[a-zA-Z]+", s).group()
    res = re.split(r"[^a-zA-Z]+", s)
    print(res)
