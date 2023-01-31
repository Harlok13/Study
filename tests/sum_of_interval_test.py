from unittest import TestCase
from librarys_modules.unittest_.examples.sum_of_interval import sum_of_intervals


class SumOfIntervalsTest(TestCase):
    """Тесты для проверки суммы интервалов"""
    def test_type_param(self):
        self.assertIsInstance(sum_of_intervals([[21, 34], [4, 10], [32, 56]]), list)
