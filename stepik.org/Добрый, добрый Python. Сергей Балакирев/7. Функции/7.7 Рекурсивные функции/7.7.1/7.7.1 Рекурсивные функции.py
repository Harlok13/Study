def get_rec_N(n):
    """
    num sequence

    :param n: integer
    :return: num sequence
    """

    if n > 0:
        get_rec_N(n - 1)
        print(n)


print(get_rec_N(8))
