import unittest
from math_function import modulo_func, is_even, is_odd, sum_function, sub_function, mul_function, div_function


class test_math_function(unittest.TestCase):

    def test_modulo_func_zero(self):
        self.assertEqual(0, modulo_func(4))

    def test_modulo_func_one(self):
        self.assertEqual(1, modulo_func(3))

    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_is_odd_true(self):
        self.assertTrue(is_odd(3))

    def test_sum_function(self):
        number_a = 5
        number_b = 8
        self.assertEqual(number_a + number_b, sum_function(number_a, number_b))

    def test_sub_function(self):
        number_a = 5
        number_b = 8
        self.assertEqual(number_b - number_a, sub_function(number_b, number_a))

    def test_mul_function(self):
        number_a = 3
        number_b = 2
        self.assertEqual(number_a * number_b, mul_function(number_a, number_b))

    def test_div_function(self):
        number_a = 15
        number_b = 5
        self.assertEqual(number_a / number_b, div_function(number_a, number_b))
