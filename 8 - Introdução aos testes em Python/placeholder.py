import pytest

def square_numbers(number):
    return number * number

def test_square_numbers():
    assert square_numbers(2) == 4
    assert square_numbers(3) == 9
    assert square_numbers(-1) == 1
    assert square_numbers(5) == square_numbers(-5)

test_square_numbers()

def division(a, b):
    return a / b

def test_raises():
    with pytest.raises(ZeroDivisionError):
        division(15, 0)

test_raises()