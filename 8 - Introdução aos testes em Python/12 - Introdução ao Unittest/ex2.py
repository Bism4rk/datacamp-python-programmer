import unittest, math

def is_prime(num):
    if num == 1: return False
    up_limit = int(math.sqrt(num)) + 1
    for i in range(2, up_limit):
        if num % i == 0:
            return False
    return True

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 17 is prime
        self.assertTrue(is_prime(17))

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 6 is not prime
        self.assertFalse(is_prime(6))

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 1 is not prime
        self.assertFalse(is_prime(1))


'''
O código acima demonstra como criar classes de testes booleanos usando o módulo unittest em Python. Ele inclui três testes para a função is_prime: um para verificar se um número primo é identificado corretamente, outro para verificar se um número não primo é identificado corretamente, e um terceiro para garantir que o número 1 não seja considerado primo. Esses testes ajudam a garantir que a função is_prime funcione conforme o esperado.
'''