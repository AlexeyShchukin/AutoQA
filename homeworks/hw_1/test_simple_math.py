import pytest

from homeworks.hw_1.simple_math import SimpleMath


@pytest.fixture()
def simple_math():
    return SimpleMath()

def test_square(simple_math):
    assert simple_math.square(4) == 16

def test_cube(simple_math):
    assert simple_math.cube(-3) == -27
