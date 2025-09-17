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
        self.assertEqual(func_factorial(5), 120)

    def test_zero(self):
        self.assertEqual(func_factorial(0), 1)

    def test_negatives(self):
        with self.assertRaises(ValueError):
            func_factorial(-1)

'''
Para rodar o teste no terminal, use os seguintes comandos:
1- cd\
2- cd "C:\Users\reich\Downloads\datacamp-python-programming\4 - Introdução aos testes em Python\13 - Interface de Linha de Comando"
3- python -m unittest ex1.py

extra: faça um ctrl x nesse bloco pq ele buga o teste pq sla mas né
'''