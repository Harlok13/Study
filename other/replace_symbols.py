def replace_symbols(sentence: str,
                    sep: str = ' ',
                    *,
                    space: bool = True,
                    chars: str = None) -> str:
    """
    replaces all characters of a string
    with the specified operator
    """
    import re
    pattern = ''.join((i for i in sentence if not i.isalnum()))
    if chars:
        pattern = re.sub(fr'[{chars}]', '', pattern)
    result = re.sub(fr'[{pattern}]', sep, sentence)
    if space:
        return re.sub(r' +', ' ', result).rstrip()
    return result.rstrip()


if __name__ == '__main__':
    assert replace_symbols('asd .f23,sdf, 9834kjasd(@*&#(Q#$NKSH(*#') == 'asd f23 sdf 9834kjasd Q NKSH'
    assert replace_symbols('asd .f23,sdf, 9834kjasd(@*&#(Q#$NKSH(*#', space=False) == 'asd  f23 sdf  9834kjasd      Q  NKSH'
    assert replace_symbols('asd .f23,sdf, 9834kjasd(@*&#(Q#$NKSH(*#', chars='@#') == 'asd f23 sdf 9834kjasd @ # Q# NKSH #'

