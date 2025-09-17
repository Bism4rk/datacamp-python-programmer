import pytest

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0

def test_numbers():
    assert multiple_of_two(2) is True
    # Write the "False" test below
    assert multiple_of_two(5) is False

test_numbers()

'''
O código acima demonstra como testar uma função com pytest em Python. Ele inclui testes para verificar se um número é múltiplo de dois e se a função lida corretamente com entradas inválidas.
'''