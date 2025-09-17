import pytest

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0

def test_zero():    
  	# Add a context for an exception test here
    with pytest.raises(ValueError):
      	# Check zero input below
        multiple_of_two(num=0)

'''
O código acima demonstra como testar uma função e levantar exceções apropriadas em Python. Ele inclui testes para verificar se um número é múltiplo de dois e se a função lida corretamente com entradas inválidas.
'''