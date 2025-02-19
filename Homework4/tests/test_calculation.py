"""
Unit tests for the Calculations class and its methods.
"""

import operator
import pytest
from Calculator.calculations import Calculations
from Calculator.calculation import Calculation


def setup_function():
    """Reset history before each test."""
    Calculations.clear_history()


def test_add_calculation():
    """Ensure a calculation can be added to history."""
    calc = Calculation(operator.add, 4, 6)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0].get_result() == 10


def test_clear_history():
    """Verify that clearing the history removes all calculations."""
    Calculations.add_calculation(Calculation(operator.add, 3, 5))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0


def test_get_history():
    """Check that calculation history is correctly retrieved."""
    calc1 = Calculation(operator.add, 3, 2)
    calc2 = Calculation(operator.mul, 3, 4)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    history = Calculations.get_history()
    assert len(history) == 2
    assert history[0].get_result() == 5


def test_get_last_calculation():
    """Ensure the last calculation in history is returned correctly."""
    calc1 = Calculation(operator.sub, 8, 5)
    calc2 = Calculation(operator.truediv, 12, 4)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    last_calc = Calculations.get_last_calculation()
    assert last_calc.get_result() == 3.0  # 12 / 4


def test_get_last_calculation_empty():
    """Ensure None is returned when retrieving from an empty history."""
    assert Calculations.get_last_calculation() is None


def test_invalid_operand_types():
    """Ensure TypeError is raised for invalid operands."""
    with pytest.raises(TypeError):
        Calculation(operator.add, "x", 7)

    with pytest.raises(TypeError):
        Calculation(operator.mul, None, 10)


def test_division_by_zero():
    """Ensure division by zero returns infinity."""
    calc = Calculation(operator.truediv, 9, 0)
    assert calc.get_result() == float('inf')
    