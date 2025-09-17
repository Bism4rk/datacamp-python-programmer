import pytest

@pytest.fixture
def prepare_data():
    return [i for i in range(10)]

def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data

# Coloque pytest ex3.py no terminal
# cd/ -> cd C:\Users\reich\Downloads\datacamp-python-programming\"4 - Introdução aos testes em Python"\"2 - Chamando o Pytest a partir da ILC" -> aí o pytest

'''
O código acima demonstra como usar fixtures no pytest para preparar dados de teste. As fixtures permitem que você defina um conjunto de dados ou estado que pode ser reutilizado em vários testes, tornando seus testes mais limpos e eficientes. Além disso, as fixtures podem ajudar a reduzir a duplicação de código e a melhorar a legibilidade dos testes. O código também dá instruções sobre como executar os testes a partir do terminal.
'''