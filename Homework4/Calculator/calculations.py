"""
Module for managing a record of past calculations.
"""

from typing import List, Optional
from Calculator.calculation import Calculation

class Calculations:
    """Handles the storage and management of calculation history."""

    # History list to store calculation objects
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Adds a calculation to the history list."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieves all stored calculations from history."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Removes all calculations from history."""
        cls.history.clear()

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        """Fetches the most recent calculation, or None if no history exists."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history_length(cls) -> int:
        """Returns the total number of calculations in history."""
        return len(cls.history)

    @classmethod
    def is_history_empty(cls) -> bool:
        """Checks whether the history list is empty."""
        return not cls.history
