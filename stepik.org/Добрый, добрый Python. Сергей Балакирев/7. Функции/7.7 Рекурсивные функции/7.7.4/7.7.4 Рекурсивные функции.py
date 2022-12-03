def fact_rec(n):
    """
    factorial calc

    :param n: integer
    :return: factorial n
    """
    return n * fact_rec(n-1) if n else 1


print(fact_rec(6))
