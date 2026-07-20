"""A simple calculator module with basic arithmetic operations."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a: The first operand.
        b: The second operand.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers.

    Args:
        a: The first operand (minuend).
        b: The second operand (subtrahend).

    Returns:
        The difference a - b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    Args:
        a: The first operand.
        b: The second operand.

    Returns:
        The product a * b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Args:
        a: The first operand (dividend).
        b: The second operand (divisor).

    Returns:
        The quotient a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def main() -> None:
    """Demonstrate each calculator operation with sample inputs."""
    x, y = 10.0, 3.0

    print("Calculator Demonstration")
    print("========================\n")

    print(f"add({x}, {y})       = {add(x, y)}")
    print(f"subtract({x}, {y})  = {subtract(x, y)}")
    print(f"multiply({x}, {y})  = {multiply(x, y)}")
    print(f"divide({x}, {y})    = {divide(x, y)}")

    print("\nEdge case — divide by zero:")
    try:
        divide(x, 0.0)
    except ZeroDivisionError as exc:
        print(f"  Caught expected error: {exc}")


if __name__ == "__main__":
    main()
