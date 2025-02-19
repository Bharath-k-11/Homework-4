"""
Unit tests for the Calculations class and its methods.
"""
import operator
from Calculator.calculations import Calculations
from Calculator.calculation import Calculation


def setup_function():
    """Reset history before each test."""
    Calculations.clear_history()


def test_add_calculation():
    """Verify that a calculation is added to the history correctly."""
    calc = Calculation(operator.add, 5, 7)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0].get_result() == 12


def test_clear_history():
    """Verify that history can be cleared."""
    Calculations.add_calculation(Calculation(operator.mul, 2, 8))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0


def test_get_history():
    """Verify that the history of calculations is correctly retrieved."""
    calc1 = Calculation(operator.add, 3, 2)
    calc2 = Calculation(operator.mul, 4, 5)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    history = Calculations.get_history()
    assert len(history) == 2
    assert history[0].get_result() == 5
    assert history[1].get_result() == 20


def test_get_last_calculation():
    """Ensure the last calculation is retrieved correctly."""
    calc1 = Calculation(operator.sub, 9, 4)
    calc2 = Calculation(operator.truediv, 8, 2)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    last_calc = Calculations.get_last_calculation()
    assert last_calc.get_result() == 4.0  # 8 / 2


def test_get_last_calculation_empty():
    """Ensure None is returned when history is empty."""
    assert Calculations.get_last_calculation() is None


def test_get_history_length():
    """Ensure the history length is calculated correctly."""
    assert Calculations.get_history_length() == 0  # Empty initially

    Calculations.add_calculation(Calculation(operator.sub, 10, 5))
    assert Calculations.get_history_length() == 1

    Calculations.add_calculation(Calculation(operator.mul, 7, 3))
    assert Calculations.get_history_length() == 2


def test_is_history_empty():
    """Ensure the history empty check works as expected."""
    assert Calculations.is_history_empty() is True  # Initially empty

    Calculations.add_calculation(Calculation(operator.add, 9, 2))
    assert Calculations.is_history_empty() is False  # Now it has one item

    Calculations.clear_history()
    assert Calculations.is_history_empty() is True  # After clearing


def test_calculation_persistence():
    """Ensure that calculations persist correctly in the history."""
    calc1 = Calculation(operator.add, 4, 6)
    calc2 = Calculation(operator.mul, 5, 5)

    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    assert Calculations.get_history_length() == 2
    assert Calculations.get_last_calculation().get_result() == 25  # 5 * 5


def test_clear_and_re_add():
    """Test clearing history and adding new calculations again."""
    Calculations.add_calculation(Calculation(operator.sub, 12, 6))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

    calc = Calculation(operator.truediv, 18, 3)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0].get_result() == 6.0
