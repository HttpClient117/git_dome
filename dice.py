"""A simple dice roller module."""

import random


def roll_dice() -> int:
    """Roll a single six-sided die.

    Returns:
        A random integer between 1 and 6 inclusive.
    """
    return random.randint(1, 6)


def roll_multiple(n: int) -> list[int]:
    """Roll multiple six-sided dice.

    Args:
        n: The number of dice to roll. Must be a non-negative integer.

    Returns:
        A list of random integers, each between 1 and 6 inclusive.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return [roll_dice() for _ in range(n)]


def main() -> None:
    """Demonstrate the dice roller functionality."""
    print("Rolling a single die:")
    print(f"  Result: {roll_dice()}")

    print("\nRolling 5 dice:")
    results = roll_multiple(5)
    print(f"  Results: {results}")
    print(f"  Total: {sum(results)}")


if __name__ == "__main__":
    main()
