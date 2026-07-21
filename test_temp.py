"""Tests for the temp.py temperature converter module."""
import math

import pytest

from temp import c_to_f, f_to_c


class TestCelsiusToFahrenheit:
    """Tests for c_to_f()."""

    def test_freezing_point(self) -> None:
        """0°C should be 32°F."""
        assert c_to_f(0.0) == 32.0

    def test_boiling_point(self) -> None:
        """100°C should be 212°F."""
        assert c_to_f(100.0) == 212.0

    def test_negative_40(self) -> None:
        """-40°C should be -40°F (the crossover point)."""
        assert c_to_f(-40.0) == -40.0

    def test_body_temperature(self) -> None:
        """37°C should be approximately 98.6°F."""
        result = c_to_f(37.0)
        assert math.isclose(result, 98.6, rel_tol=1e-9)

    def test_room_temperature(self) -> None:
        """20°C should be 68°F."""
        assert c_to_f(20.0) == 68.0

    def test_absolute_zero_approx(self) -> None:
        """-273.15°C should be approximately -459.67°F."""
        result = c_to_f(-273.15)
        assert math.isclose(result, -459.67, rel_tol=1e-9)

    def test_positive_large(self) -> None:
        """Large positive value should convert correctly."""
        assert c_to_f(1000.0) == 1832.0

    def test_negative_large(self) -> None:
        """Large negative value should convert correctly."""
        assert c_to_f(-1000.0) == -1768.0


class TestFahrenheitToCelsius:
    """Tests for f_to_c()."""

    def test_freezing_point(self) -> None:
        """32°F should be 0°C."""
        assert f_to_c(32.0) == 0.0

    def test_boiling_point(self) -> None:
        """212°F should be 100°C."""
        assert f_to_c(212.0) == 100.0

    def test_negative_40(self) -> None:
        """-40°F should be -40°C (the crossover point)."""
        assert f_to_c(-40.0) == -40.0

    def test_body_temperature(self) -> None:
        """98.6°F should be approximately 37°C."""
        result = f_to_c(98.6)
        assert math.isclose(result, 37.0, rel_tol=1e-9)

    def test_room_temperature(self) -> None:
        """68°F should be 20°C."""
        assert f_to_c(68.0) == 20.0

    def test_absolute_zero_approx(self) -> None:
        """-459.67°F should be approximately -273.15°C."""
        result = f_to_c(-459.67)
        assert math.isclose(result, -273.15, rel_tol=1e-9)

    def test_positive_large(self) -> None:
        """Large positive value should convert correctly."""
        assert f_to_c(2120.0) == 1160.0

    def test_negative_large(self) -> None:
        """Large negative value should convert correctly."""
        assert f_to_c(-148.0) == -100.0


class TestRoundTrip:
    """Round-trip conversion tests."""

    @pytest.mark.parametrize("celsius", [-100.0, -40.0, -10.0, 0.0, 15.0, 25.0, 37.0, 100.0, 500.0])
    def test_c_to_f_to_c(self, celsius: float) -> None:
        """Converting C→F→C should return the original value."""
        result = f_to_c(c_to_f(celsius))
        assert math.isclose(result, celsius, rel_tol=1e-9)

    @pytest.mark.parametrize("fahrenheit", [-148.0, -40.0, 0.0, 32.0, 68.0, 98.6, 212.0, 500.0])
    def test_f_to_c_to_f(self, fahrenheit: float) -> None:
        """Converting F→C→F should return the original value."""
        result = c_to_f(f_to_c(fahrenheit))
        assert math.isclose(result, fahrenheit, rel_tol=1e-9)
