import unittest

def func_factorial(number):
    if number < 0:
        raise ValueError('Factorial is not defined for negative values')
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial

class TestFactorial(unittest.TestCase):
    def test_positives(self):
        # Add the test for testing positives here
        self.assertEqual(func_factorial(5), 120)

def func_factorial(number):
    if number < 0:
        raise ValueError('Factorial is not defined for negative values')
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial

class TestFactorial(unittest.TestCase):
    def test_zero(self):
        # Add the test for testing zero here
        self.assertEqual(func_factorial(0), 1)

import unittest
def func_factorial(number):
    if number < 0:
        raise ValueError('Factorial is not defined for negative values')
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial

class TestFactorial(unittest.TestCase):
    def test_negatives(self):
      	# Add the test for testing negatives here
        with self.assertRaises(ValueError):
            func_factorial(-79)

'''
O código acima demonstra como criar uma classe de teste usando o módulo unittest em Python. Ele permite que os desenvolvedores escrevam testes para suas funções e verifiquem se elas estão se comportando conforme o esperado. O código inclui três testes: um para números positivos, um para zero e um para números negativos.
'''