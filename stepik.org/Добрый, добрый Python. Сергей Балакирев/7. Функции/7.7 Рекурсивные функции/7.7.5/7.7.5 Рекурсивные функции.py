d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
def get_line_list(d, a=[]):
    """
    one-dimensional list

    :param d: nested list
    :param a: default list
    :return: one-dimensional list
    """
    for i in d:
        if type(i) != list:
            a.append(i)
    if type(i) == list:
        get_line_list(i)
    return a


print(get_line_list(d))
