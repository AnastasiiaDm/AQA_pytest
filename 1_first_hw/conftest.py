import pytest
from human import Human


@pytest.fixture()
def create_female_age_30():
    return Human('Mia', 30, 'female')


@pytest.fixture()
def create_human_with_params():
    def __create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)

    yield __create_human


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: for smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: for regression tests"
    )
