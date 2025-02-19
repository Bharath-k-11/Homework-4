"""
Module for performing arithmetic calculations and storing results.
"""

from typing import Callable


class Calculation:
    """Represents a single calculation for an arithmetic operation."""
    def __init__(self, operation: Callable[[float, float], float], num1: float, num2: float):
        """
        Initializes a Calculation object.

        :param operation: A function representing the arithmetic operation.
        :param num1: First number (int or float).
        :param num2: Second number (int or float).
        """
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Both numbers must be of type int or float")

        self.operation = operation
        self.first_number = num1
        self.second_number = num2

        try:
            self.result = self.operation(self.first_number, self.second_number)
        except ZeroDivisionError:
            self.result = float('inf')  # Handle division by zero gracefully

    def get_result(self) -> float:
        """Returns the computed result of the calculation."""
        return self.result

    def __repr__(self):
        """Returns a readable string representation of the calculation."""
        operation_name = self.operation.__name__ if hasattr(self.operation, '__name__') else "undefined_operation"
        return f"Calculation({self.first_number} {operation_name} {self.second_number} = {self.result})"

    @staticmethod
    def from_tuple(data: tuple):
        """
        Creates a Calculation object from a tuple.

        :param data: Tuple in the format (operation, num1, num2)
        :return: Calculation instance
        """
        if not isinstance(data, tuple) or len(data) != 3:
            raise ValueError("Tuple must contain exactly three elements: (operation, num1, num2)")
        return Calculation(*data)
