"""Tests for the unit converter module."""

import math

import pytest

from converter import celsius_to_fahrenheit, fahrenheit_to_celsius, km_to_miles


class TestCelsiusToFahrenheit:
    """Tests for celsius_to_fahrenheit."""

    def test_boiling_point(self) -> None:
        """100°C should be 212°F."""
        assert math.isclose(celsius_to_fahrenheit(100.0), 212.0)

    def test_freezing_point(self) -> None:
        """0°C should be 32°F."""
        assert math.isclose(celsius_to_fahrenheit(0.0), 32.0)

    def test_negative(self) -> None:
        """-40°C should be -40°F."""
        assert math.isclose(celsius_to_fahrenheit(-40.0), -40.0)

    def test_body_temperature(self) -> None:
        """37°C should be 98.6°F."""
        assert math.isclose(celsius_to_fahrenheit(37.0), 98.6)


class TestFahrenheitToCelsius:
    """Tests for fahrenheit_to_celsius."""

    def test_boiling_point(self) -> None:
        """212°F should be 100°C."""
        assert math.isclose(fahrenheit_to_celsius(212.0), 100.0)

    def test_freezing_point(self) -> None:
        """32°F should be 0°C."""
        assert math.isclose(fahrenheit_to_celsius(32.0), 0.0)

    def test_negative(self) -> None:
        """-40°F should be -40°C."""
        assert math.isclose(fahrenheit_to_celsius(-40.0), -40.0)

    def test_body_temperature(self) -> None:
        """98.6°F should be 37°C."""
        assert math.isclose(fahrenheit_to_celsius(98.6), 37.0)

    def test_roundtrip(self) -> None:
        """Roundtrip conversion should return the original value."""
        original = 75.0
        converted = celsius_to_fahrenheit(fahrenheit_to_celsius(original))
        assert math.isclose(converted, original)


class TestKmToMiles:
    """Tests for km_to_miles."""

    def test_ten_km(self) -> None:
        """10 km should be approximately 6.21371 miles."""
        assert math.isclose(km_to_miles(10.0), 6.21371)

    def test_zero(self) -> None:
        """0 km should be 0 miles."""
        assert math.isclose(km_to_miles(0.0), 0.0)

    def test_marathon(self) -> None:
        """A marathon (42.195 km) should be about 26.2 miles."""
        miles = km_to_miles(42.195)
        assert 26.0 < miles < 26.5

    def test_roundtrip(self) -> None:
        """Roundtrip conversion should be consistent."""
        km = 50.0
        miles = km_to_miles(km)
        km_back = miles / 0.621371
        assert math.isclose(km, km_back)
