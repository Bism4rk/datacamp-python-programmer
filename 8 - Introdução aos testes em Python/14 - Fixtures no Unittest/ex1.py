import unittest

class TestWord(unittest.TestCase):
    # Fixture setup method
    def setUp(self):
        # Initialize the word banana here
        self.word = 'banana'

    # Test method
    def test_the_word(self):
        # Add the tests here
        self.assertNotIn('B', self.word)
        self.assertNotIn('y', self.word)
        self.assertIn('b', self.word)
    
    # Fixture teardown method
    def tearDown(self):
        # Delete the word variable here
        del self.word

'''
O código acima demonstra como usar fixtures no unittest para configurar e limpar o estado antes e depois dos testes. A classe TestWord é um exemplo de como implementar esses métodos de configuração e limpeza - ela tem três métodos principais: setUp, test_the_word e tearDown. setUp é chamado antes de cada método de teste e é usado para criar um ambiente de teste limpo. tearDown é chamado após cada método de teste e é usado para limpar qualquer estado que possa ter sido alterado durante o teste.
'''