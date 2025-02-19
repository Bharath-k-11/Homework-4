"""
Unit tests for main.py, ensuring 100% test coverage.
"""

import sys
import subprocess
import pytest
from main import calculate

@pytest.mark.parametrize("num1, num2, operation, expected_output", [
    ("8", "6", "add", "The result of 8 add 6 is equal to 14"),
    ("12", "5", "subtract", "The result of 12 subtract 5 is equal to 7"),
    ("7", "9", "multiply", "The result of 7 multiply 9 is equal to 63"),
    ("18", "3", "divide", "The result of 18 divide 3 is equal to 6"),
    ("15", "0", "divide", "An error occurred: Cannot divide by zero"),
    ("20", "5", "unknown", "Unknown operation: unknown"),
    ("x", "2", "add", "Invalid number input: x or 2 is not a valid number."),
    ("4", "y", "subtract", "Invalid number input: 4 or y is not a valid number.")
])
def test_calculate(num1, num2, operation, expected_output):
    """Tests the calculate function directly."""
    assert calculate(num1, num2, operation) == expected_output

@pytest.mark.parametrize("num1, num2, operation, expected_output", [
    ("8", "6", "add", "The result of 8 add 6 is equal to 14"),
    ("12", "5", "subtract", "The result of 12 subtract 5 is equal to 7"),
    ("7", "9", "multiply", "The result of 7 multiply 9 is equal to 63"),
    ("18", "3", "divide", "The result of 18 divide 3 is equal to 6"),
    ("15", "0", "divide", "An error occurred: Cannot divide by zero"),
    ("20", "5", "unknown", "Unknown operation: unknown"),
    ("x", "2", "add", "Invalid number input: x or 2 is not a valid number."),
    ("4", "y", "subtract", "Invalid number input: 4 or y is not a valid number.")
])
def test_main_script(num1, num2, operation, expected_output):
    """Tests command-line execution of main.py."""
    result = subprocess.run(
        [sys.executable, "main.py", num1, num2, operation],
        capture_output=True,
        text=True,
        check=True  # Explicitly setting check=True to satisfy Pylint
    )
    assert expected_output in result.stdout

def test_main_script_usage():
    """Tests the script without enough arguments to trigger the usage message."""
    result = subprocess.run(
        [sys.executable, "main.py", "8", "6"],
        capture_output=True,
        text=True,
        check=False  # No need to enforce an error on expected failure case
    )
    assert "Usage: python main.py <num1> <num2> <operation>" in result.stdout
