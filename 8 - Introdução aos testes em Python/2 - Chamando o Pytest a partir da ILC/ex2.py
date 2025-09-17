# Import the pytest library
import pytest

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0

def test_numbers():
    assert multiple_of_two(2) == True
    assert multiple_of_two(3) == False

def test_zero():    
    with pytest.raises(ValueError):
        multiple_of_two(0)


# Coloque pytest ex1.py -k "numbers" no terminal
# cd/ -> cd C:\Users\reich\Downloads\datacamp-python-programming\"4 - Introdução aos testes em Python"\"2 - Chamando o Pytest a partir da ILC" -> aí o pytest

'''
O código acima demonstra como testar uma função e levantar exceções apropriadas em Python. Ele inclui testes para verificar se um número é múltiplo de dois e se a função lida corretamente com entradas inválidas. Além disso, há instruções para executar os testes usando o pytest a partir do terminal, e também para filtrar testes específicos pelo nome por meio da opção -k.
'''