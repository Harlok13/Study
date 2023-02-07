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




