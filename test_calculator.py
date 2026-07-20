"""Tests for the calculator module."""

import math

import pytest

from calculator import add, divide, multiply, subtract


class TestAdd:
    """Tests for the add function."""

    def test_positive_numbers(self) -> None:
        assert add(2.0, 3.0) == 5.0

    def test_negative_numbers(self) -> None:
        assert add(-2.0, -3.0) == -5.0

    def test_mixed_signs(self) -> None:
        assert add(-2.0, 3.0) == 1.0

    def test_zero(self) -> None:
        assert add(0.0, 5.0) == 5.0
        assert add(5.0, 0.0) == 5.0

    def test_floats(self) -> None:
        assert math.isclose(add(0.1, 0.2), 0.3)


class TestSubtract:
    """Tests for the subtract function."""

    def test_positive_numbers(self) -> None:
        assert subtract(10.0, 3.0) == 7.0

    def test_negative_numbers(self) -> None:
        assert subtract(-5.0, -2.0) == -3.0

    def test_mixed_signs(self) -> None:
        assert subtract(2.0, -3.0) == 5.0

    def test_zero(self) -> None:
        assert subtract(5.0, 0.0) == 5.0
        assert subtract(0.0, 5.0) == -5.0

    def test_floats(self) -> None:
        assert math.isclose(subtract(0.3, 0.1), 0.2)


class TestMultiply:
    """Tests for the multiply function."""

    def test_positive_numbers(self) -> None:
        assert multiply(4.0, 5.0) == 20.0

    def test_negative_numbers(self) -> None:
        assert multiply(-4.0, -5.0) == 20.0

    def test_mixed_signs(self) -> None:
        assert multiply(-4.0, 5.0) == -20.0

    def test_zero(self) -> None:
        assert multiply(7.0, 0.0) == 0.0
        assert multiply(0.0, 7.0) == 0.0

    def test_by_one(self) -> None:
        assert multiply(42.0, 1.0) == 42.0


class TestDivide:
    """Tests for the divide function."""

    def test_positive_numbers(self) -> None:
        assert divide(10.0, 2.0) == 5.0

    def test_negative_numbers(self) -> None:
        assert divide(-10.0, -2.0) == 5.0

    def test_mixed_signs(self) -> None:
        assert divide(-10.0, 2.0) == -5.0

    def test_float_result(self) -> None:
        assert math.isclose(divide(10.0, 3.0), 3.3333333333333335)

    def test_zero_dividend(self) -> None:
        assert divide(0.0, 5.0) == 0.0

    def test_division_by_zero_raises(self) -> None:
        with pytest.raises(ZeroDivisionError, match="Division by zero"):
            divide(10.0, 0.0)
