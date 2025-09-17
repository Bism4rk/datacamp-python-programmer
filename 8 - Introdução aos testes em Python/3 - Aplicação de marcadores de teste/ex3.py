import datetime, pytest

day_of_week = datetime.now().isoweekday()

def get_unique_values(lst):
    return list(set(lst))

condition_string = 'day_of_week == 6'
# Add the conditional skip marker and the string here
@pytest.mark.skipif(condition_string)
def test_function():
	# Complete the assertion tests here
    assert get_unique_values([1,2,3]) == [1,2,3]
    assert get_unique_values([1,2,3,1]) == [1,2,3]

'''
O código acima demonstra como usar o marcador skipif do pytest para pular um teste com base em uma condição. Isso pode ser útil em situações em que você deseja desativar temporariamente um teste que não é relevante em determinadas circunstâncias.
'''