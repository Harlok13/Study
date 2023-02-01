from librarys_modules.pytest_.utils import division
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (20, 5, 4),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division(a, b, expected_result):
    """Проверка на корректные значения при делении"""
    assert division(a, b) == expected_result


@pytest.mark.parametrize('expected_exception, divisionable, divider',
                         [(ZeroDivisionError, 10, 0),
                          (TypeError, 20, '2')])
def test_zero_division(divisionable, divider, expected_exception):
    """Проверка на генерацию исключений"""
    with pytest.raises(expected_exception):
        division(divisionable, divider)

