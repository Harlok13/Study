Given a positive number `n > 1` find the prime factor decomposition
 of `n`. The result will be a string with the following form :
```
 "(p1**n1)(p2**n2)...(pk**nk)"
 ```
with the p(i) in increasing order and n(i) empty if n(i) is 1.
```
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
```

# Solution
```python
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
        pr = pr + 1
    if number > 1:
        primfac.append(int(number))
    return primfac
```

# Tests for solution
```python
import pytest

from other.codewars.primes_in_numbers import prime_factors, get_prime_numbers


@pytest.mark.parametrize('test_data', [(86240, "(2**5)(5)(7**2)(11)"),
                                       (7775460, "(2**2)(3**3)(5)(7)(11**2)(17)"),
                                       (7919, "(7919)")])
def test_prime_factors(test_data):
    """
    prime_factors(<num>) должен возвращать строковое представление
    числа, разложенного на простые множители.
    """
    return_value = prime_factors(test_data[0])
    expected_value = test_data[1]
    assert return_value == expected_value


@pytest.mark.parametrize('test_data', [(86240, [2, 2, 2, 2, 2, 5, 7, 7, 11]),
                                       (7775460, [2, 2, 3, 3, 3, 5, 7, 11, 11, 17]),
                                       (7919, [7919,])])
def test_prime_numbers(test_data):
    """
    get_prime_numbers(<num>) должен возвращать число, разложенное
    на простые множители.
    """
    return_value = get_prime_numbers(test_data[0])
    expected_value = test_data[1]
    assert return_value == expected_value
```
