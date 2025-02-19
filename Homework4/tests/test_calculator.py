'''Unit tests for the Calculator class using Faker for test data'''
import pytest
from faker import Faker
from Calculator.calculator import Calculator
from Calculator.calculations import Calculations

fake_data_generator = Faker()


@pytest.fixture(autouse=True)
def reset_history():
    """Reset calculation history before each test."""
    Calculations.clear_history()


@pytest.mark.parametrize(
    "operand_1, operand_2",
    [
    (fake_data_generator.random_int(min=-150, max=150),
    fake_data_generator.random_int(min=-150, max=150)) for _ in range(5)
    ],
)
def test_addition(operand_1, operand_2):
    """Test the addition operation with Faker-generated numbers."""
    assert Calculator.add(operand_1, operand_2) == operand_1 + operand_2


@pytest.mark.parametrize(
    "operand_1, operand_2",
    [
    (fake_data_generator.random_int(min=-150, max=150),
    fake_data_generator.random_int(min=-150, max=150)) for _ in range(5)
    ],
)
def test_subtraction(operand_1, operand_2):
    """Test the subtraction operation with Faker-generated numbers."""
    assert Calculator.subtract(operand_1, operand_2) == operand_1 - operand_2


@pytest.mark.parametrize(
    "operand_1, operand_2",
    [
    (fake_data_generator.random_int(min=-150, max=150),
    fake_data_generator.random_int(min=-150, max=150)) for _ in range(5)
    ],
)
def test_multiplication(operand_1, operand_2):
    """Test the multiplication operation with Faker-generated numbers."""
    assert Calculator.multiply(operand_1, operand_2) == operand_1 * operand_2


@pytest.mark.parametrize(
    "operand_1, operand_2",
    [
    (fake_data_generator.random_int(min=1, max=150),
    fake_data_generator.random_int(min=1, max=150)) for _ in range(5)
    ],
)
def test_division(operand_1, operand_2):
    """Test the division operation with Faker-generated numbers."""
    assert Calculator.divide(operand_1, operand_2) == operand_1 / operand_2


def test_zero_division():
    """Test that division by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(fake_data_generator.random_int(min=1, max=150), 0)
