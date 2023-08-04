from calculator import Calculator

calculator  = Calculator()

def test_pozitive_nums():
    calculator = Calculator()
    res = calculator.sum(5, 5)
    assert res == 10

def test_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_negative_and_pozitive_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0
