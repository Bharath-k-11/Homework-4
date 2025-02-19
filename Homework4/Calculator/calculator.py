"""
Advanced Calculator with functionality to maintain a history of calculations.
"""

from Calculator.calculation import Calculation
from Calculator.calculations import Calculations

class Calculator:
    """Performs arithmetic operations and tracks the results in history."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Executes addition and appends the result to history."""
        calc = Calculation(lambda x, y: x + y, a, b)
        Calculations.add_calculation(calc)
        return calc.get_result()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Executes subtraction and appends the result to history."""
        calc = Calculation(lambda x, y: x - y, a, b)
        Calculations.add_calculation(calc)
        return calc.get_result()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Executes multiplication and appends the result to history."""
        calc = Calculation(lambda x, y: x * y, a, b)
        Calculations.add_calculation(calc)
        return calc.get_result()

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Executes division and appends the result to history. Raises ZeroDivisionError if b is zero."""
        if b == 0:
            raise ZeroDivisionError("Error: Attempted to divide by zero.")
        calc = Calculation(lambda x, y: x / y, a, b)
        Calculations.add_calculation(calc)
        return calc.get_result()
