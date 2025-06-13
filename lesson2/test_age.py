import pytest

from lesson2.task2 import AgeValidator


@pytest.fixture
def age_validator_obj():
    return AgeValidator()


def test_age1(age_validator_obj):
    assert age_validator_obj.is_adult(20) == True


@pytest.mark.parametrize("age, expected", [
    (17, False),
    (18, True),
    (19, True),
])
def test_age(age_validator_obj, age, expected):
    assert age_validator_obj.is_adult(age) == expected
