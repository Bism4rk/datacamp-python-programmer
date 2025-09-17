import pandas as pd
import pytest

# Fixture to read the dataframe
@pytest.fixture
def get_df():
    return pd.read_csv('https://assets.datacamp.com/production/repositories/6253/datasets/757c6cb769f7effc5f5496050ea4d73e4586c2dd/laptops_train.csv')

# Integration test function
def test_get_df(get_df):
    # Check the type
    assert type(get_df) == pd.DataFrame
    # Check the number of rows
    assert get_df.shape[0] > 0

# Coloque pytest ex2.py no terminal
# cd\"4 - Introdução aos testes em Python"\"9 - Testes de recursos com o Pytest" -> aí o pytest

'''
O código acima demonstra como fazer um teste de integração utilizando o Pytest em uma função que lê um DataFrame com o Pandas. O Pytest é uma ferramenta poderosa para a realização de testes em Python, permitindo a verificação de funcionalidades de forma simples e eficaz. Ele facilita a identificação de problemas e a validação de resultados esperados, tornando o processo de desenvolvimento mais robusto e confiável. No código, a fixture `get_df` é utilizada para fornecer um DataFrame para o teste, que verifica se o objeto retornado é do tipo `pd.DataFrame` e se contém pelo menos uma linha.
'''