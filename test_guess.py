"""Tests for the guess module."""

import pytest

from guess import check_guess, generate_secret


class TestGenerateSecret:
    """Tests for generate_secret()."""

    def test_returns_int(self) -> None:
        """generate_secret should return an int."""
        assert isinstance(generate_secret(), int)

    def test_range_lower_bound(self) -> None:
        """generate_secret should never return less than 1."""
        for _ in range(1000):
            assert generate_secret() >= 1

    def test_range_upper_bound(self) -> None:
        """generate_secret should never return more than 100."""
        for _ in range(1000):
            assert generate_secret() <= 100

    def test_randomness_covers_range(self) -> None:
        """After many calls, generate_secret should produce a variety of values."""
        results = {generate_secret() for _ in range(500)}
        # With 500 samples in [1, 100], we should hit at least 40 distinct values
        assert len(results) >= 40


class TestCheckGuess:
    """Tests for check_guess()."""

    @pytest.mark.parametrize(
        ("secret", "guess", "expected"),
        [
            (50, 75, "too high"),
            (50, 100, "too high"),
            (50, 51, "too high"),
            (50, 25, "too low"),
            (50, 1, "too low"),
            (50, 49, "too low"),
            (50, 50, "correct"),
            (1, 1, "correct"),
            (100, 100, "correct"),
            (1, 100, "too high"),
            (100, 1, "too low"),
        ],
    )
    def test_check_guess(self, secret: int, guess: int, expected: str) -> None:
        """check_guess should return the correct hint for various input pairs."""
        assert check_guess(secret, guess) == expected
