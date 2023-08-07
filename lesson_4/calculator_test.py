import pytest
from calculator import Calculator

calculator  = Calculator()


@pytest.mark.parametrize( 'num_1, num_2, result', [(5,5,10), (-6, -10, -16)] )
def test_nums_pozitive_nums(num_1, num_2, result):
    calculator = Calculator()
    res = calculator.sum(num_1, num_2)
    assert res == result

def test_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_negative_and_pozitive_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9

def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

@pytest.mark.positive_test
def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)

def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0

@pytest.mark.positive_test
def test_avg_positive():
    calculator = Calculator()
    numbers = [1,2,3,4,5,6,7,8,9,5]
    res = calculator.avg(numbers)
    assert res == 5
