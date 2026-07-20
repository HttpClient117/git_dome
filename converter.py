"""Unit converter module.

Provides functions for converting between common units of measurement.
"""


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit.

    Args:
        c: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.
    """
    return (c * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius.

    Args:
        f: Temperature in degrees Fahrenheit.

    Returns:
        Temperature in degrees Celsius.
    """
    return (f - 32.0) * 5.0 / 9.0


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles.

    Args:
        km: Distance in kilometres.

    Returns:
        Distance in miles.
    """
    return km * 0.621371


def main() -> None:
    """Demonstrate the unit converter functions."""
    print("Unit Converter Demo")
    print("-" * 30)

    # Temperature conversions
    c_temp = 100.0
    f_temp = celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}°C = {f_temp}°F")

    f_temp2 = 212.0
    c_temp2 = fahrenheit_to_celsius(f_temp2)
    print(f"{f_temp2}°F = {c_temp2}°C")

    # Distance conversion
    km = 10.0
    miles = km_to_miles(km)
    print(f"{km} km = {miles} miles")


if __name__ == "__main__":
    main()
