from contextlib import nullcontext as does_not_raise

import pytest

from unit_tests.calculator import Calculator


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (4, 0, 1, pytest.raises(ArithmeticError, match="На ноль делить нельзя"))
        ]
    )
    def test_sum(self, x, y, res, expectation):
        with expectation:
            assert Calculator().div(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (4, "0", 4, pytest.raises(TypeError)),
            (0, 2, 2, does_not_raise()),
            (1, -2.5, -1.5, does_not_raise()),
        ]
    )
    def rest_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().sum(x, y) == res
