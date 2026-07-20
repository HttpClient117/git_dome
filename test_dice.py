"""Tests for the dice roller module."""

import pytest

from dice import roll_dice, roll_multiple


class TestRollDice:
    """Tests for roll_dice()."""

    def test_returns_int(self) -> None:
        """roll_dice() should return an integer."""
        result = roll_dice()
        assert isinstance(result, int)

    def test_returns_value_in_range(self) -> None:
        """roll_dice() should return a value between 1 and 6 inclusive."""
        for _ in range(100):
            result = roll_dice()
            assert 1 <= result <= 6

    def test_distribution_covers_all_values(self) -> None:
        """After many rolls, all values 1-6 should appear."""
        results = {roll_dice() for _ in range(1000)}
        assert results == set(range(1, 7))


class TestRollMultiple:
    """Tests for roll_multiple()."""

    def test_returns_list(self) -> None:
        """roll_multiple() should return a list."""
        result = roll_multiple(3)
        assert isinstance(result, list)

    def test_zero_dice_returns_empty_list(self) -> None:
        """Rolling 0 dice should return an empty list."""
        result = roll_multiple(0)
        assert result == []

    def test_count_matches_n(self) -> None:
        """The number of results should match the requested count."""
        for n in (1, 2, 5, 10):
            result = roll_multiple(n)
            assert len(result) == n

    def test_all_values_in_range(self) -> None:
        """All rolled values should be in the 1-6 range."""
        result = roll_multiple(50)
        assert all(1 <= val <= 6 for val in result)

    def test_negative_n_raises_valueerror(self) -> None:
        """Negative n should raise ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            roll_multiple(-1)

    def test_result_is_independent(self) -> None:
        """Multiple rolls should not all be identical (probabilistic)."""
        result = roll_multiple(20)
        assert len(set(result)) > 1
