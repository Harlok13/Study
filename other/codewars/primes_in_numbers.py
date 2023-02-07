def prime_factors(number):
    """Представляет факторизованное число в сокращенной форме записи."""
    from collections import Counter
    prime_num = Counter(get_prime_numbers(number))

    primfac = [f'({primnum}**{count})' if count > 1 else f'({primnum})'
               for primnum, count in prime_num.items()]

    return ''.join(primfac)


def get_prime_numbers(number):
    """Раскладывает число на простые множители."""
    pr = 2
    primfac = []
    while pow(pr, 2) <= number:
        while number % pr == 0:
            primfac.append(pr)
            number = number / pr
        i = pr + 1
    if number > 1:
        primfac.append(int(number))
    return primfac


if __name__ == '__main__':
    print(get_prime_numbers(86240))
    print(prime_factors(86240))
