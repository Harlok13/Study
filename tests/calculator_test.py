from unittest import TestCase, main
from librarys_modules.unittest.examples.calculator import calculator


class CalculatorTest(TestCase):
    """Тесты для проверки калькулятора"""

    def test_add(self):
        """Проверка на сложение"""
        self.assertEqual(calculator('2+2'), 4)

    def test_mul(self):
        """Проверка на умножение"""
        self.assertEqual(calculator('5*3'), 15)

    def test_sub(self):
        """Проверка на вычитание"""
        self.assertEqual(calculator('32-16'), 16)

    def test_truediv(self):
        """Проверка на деление"""
        self.assertEqual(calculator('25/5'), 5.)
        self.assertEqual(calculator('20/5'), 4.)

    def test_no_operator(self):
        """Проверка исключения при отсутствии оператора"""
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual("Выражение должно содержать хотя бы один знак"
                         "  ('+', '*', '-', '/')", e.exception.args[0])

    def test_two_operators(self):
        """Проверка на исключение при двух одинаковых операторах"""
        with self.assertRaises(ValueError) as e:
            calculator('3+3+3')
        self.assertEqual("Выражение должно содержать 2 целых числа"
                         " и один оператор", e.exception.args[0])

    def test_many_operators(self):
        """Проверка на исключение при разных операторах"""
        with self.assertRaises(ValueError) as e:
            calculator('3/3*3')
        self.assertEqual("Выражение должно содержать 2 целых числа"
                         " и один оператор", e.exception.args[0])

    def test_no_ints(self):
        """Проверка на исключение, если строка содержит не целые числа"""
        with self.assertRaises(ValueError) as e:
            calculator('5.7+5.2')
        self.assertEqual("Выражение должно содержать 2 целых числа"
                         " и один оператор", e.exception.args[0])

    def test_strings(self):
        """Проверка на исключение, если вместо целых чисел строки"""
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual("Выражение должно содержать 2 целых числа"
                         " и один оператор", e.exception.args[0])


if __name__ == '__main__':
    main()
