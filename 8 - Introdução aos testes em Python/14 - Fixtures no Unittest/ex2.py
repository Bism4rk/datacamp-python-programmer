import unittest

def check_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def create_data():
    return ['level', 'step', 'peep', 'toot']

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        # Initialize data here
        self.data = create_data()
    
    def test_func(self):
        expected_result = [True, False, True, True]
        data_checked = list(map(check_palindrome, self.data))
        # Verify the checked data here
        self.assertEqual(data_checked, expected_result)

    def tearDown(self):
        # Clear the data here
        self.data.clear()

'''
O código acima demonstra mais uma vez como usar fixtures no unittest para configurar e limpar o estado antes e depois dos testes. A classe TestPalindrome é um exemplo de como implementar esses métodos de configuração e limpeza - ela tem três métodos principais: setUp, test_func e tearDown. setUp é chamado antes de cada método de teste e é usado para criar um ambiente de teste limpo. tearDown é chamado após cada método de teste e é usado para limpar qualquer estado que possa ter sido alterado durante o teste.
'''