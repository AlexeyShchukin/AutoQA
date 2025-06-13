# Протестируйте is_even и is_odd для чисел: 0, 1, 2, -1, -2.
import pytest

from lesson2.task1 import EvenOddChecker


@pytest.fixture()
def checker():
    return EvenOddChecker()


def test_is_even1(checker):
    assert checker.is_even(0) == True
    assert checker.is_even(2) == True
    assert checker.is_even(-2) == True


def test_is_odd1(checker):
    assert checker.is_odd(1) == True
    assert checker.is_odd(-1) == True


@pytest.mark.parametrize("n, expected", [
    (0, True),
    (1, False),
    (2, True),
    (-3, False),
    (-4, True),
])
def test_is_even(checker, n, expected):
    assert checker.is_even(n) == expected


@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, True),
    (2, False),
    (-3, True),
    (-4, False),
])
def test_is_odd(checker, n, expected):
    assert checker.is_odd(n) == expected