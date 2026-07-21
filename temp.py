"""Temperature converter module.

Provides functions to convert between Celsius and Fahrenheit.
"""


def c_to_f(c: float) -> float:
    """Convert Celsius to Fahrenheit.

    Args:
        c: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.

    >>> c_to_f(0)
    32.0
    >>> c_to_f(100)
    212.0
    >>> c_to_f(-40)
    -40.0
    """
    return (c * 9.0 / 5.0) + 32.0


def f_to_c(f: float) -> float:
    """Convert Fahrenheit to Celsius.

    Args:
        f: Temperature in degrees Fahrenheit.

    Returns:
        Temperature in degrees Celsius.

    >>> f_to_c(32)
    0.0
    >>> f_to_c(212)
    100.0
    >>> f_to_c(-40)
    -40.0
    """
    return (f - 32.0) * 5.0 / 9.0


def main() -> None:
    """Demonstrate temperature conversions."""
    test_values_c = [-40.0, 0.0, 20.0, 37.0, 100.0]
    test_values_f = [-40.0, 0.0, 32.0, 68.0, 98.6, 212.0]

    print("Celsius → Fahrenheit")
    for c in test_values_c:
        print(f"  {c:6.1f}°C = {c_to_f(c):6.1f}°F")

    print()
    print("Fahrenheit → Celsius")
    for f_val in test_values_f:
        print(f"  {f_val:6.1f}°F = {f_to_c(f_val):6.1f}°C")


if __name__ == "__main__":
    main()
