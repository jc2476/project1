"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_is_instance():
    """Testing the Calculator"""
    calculator = Calculator()
    assert isinstance(calculator, Calculator)


def test_calculator_get_result_method():
    """Testing the Calculator"""
    calculator = Calculator()
    assert calculator.get_result() == 0


def test_calculator_result_property():
    """Testing the Calculator"""
    # Arrange
    calc1 = Calculator()
    calc2 = Calculator()

    # Act
    calc1.result = 4
    calc2.result = 2

    # Assert
    assert calc1.result == 4
    assert calc2.result == 2


def test_calculator_add_method():
    """Testing the Calculator"""
    calculator = Calculator()
    assert calculator.add(1) == 1


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.subtract(-1) == 1

def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.multiply(-1) == 1

def test_calculator_divide_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.divide(-1) == 1
