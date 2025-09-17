# Import the pytest library
import pytest

# Define the fixture decorator
@pytest.fixture
# Name the fixture function
def prepare_data():
    return [i for i in range(10)]

# Create the tests
def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data

'''
O código acima demonstra como usar fixtures no pytest para preparar dados de teste. As fixtures permitem que você defina um conjunto de dados ou estado que pode ser reutilizado em vários testes, tornando seus testes mais limpos e eficientes.
'''