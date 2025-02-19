import pytest
from faker import Faker

def pytest_addoption(parser):
    """
    Adds a command line option --num_records for pytest.
    Usage: pytest --num_records=100
    """
    parser.addoption(
        "--num_records",
        action="store",
        default=0,
        help="Number of records to generate for tests."
    )

@pytest.fixture
def num_records(request):
    """
    Returns the number of records specified by --num_records.
    """
    return int(request.config.getoption("--num_records"))

@pytest.fixture
def fake_data(num_records):
    """
    Generates random test data for calculator tests.
    """
    fake = Faker()
    data = []
    operations = ["add", "subtract", "multiply", "divide"]

    for _ in range(num_records):
        a = fake.random_int(min=0, max=100)
        b = fake.random_int(min=0, max=100)
        operation = fake.random_element(elements=operations)
        data.append((a, b, operation))

    return data
