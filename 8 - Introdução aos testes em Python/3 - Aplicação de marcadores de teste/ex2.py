import pytest

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0

# Add the pytest marker decorator here
@pytest.mark.xfail
def test_fails():
    # Write any assert test that will fail
    assert multiple_of_two(528) is False

'''
O código acima demonstra como usar o marcador xfail do pytest para indicar que um teste deve falhar. Isso pode ser útil em situações em que você está trabalhando em um recurso que ainda não está completo ou em um bug que ainda não foi corrigido.
'''