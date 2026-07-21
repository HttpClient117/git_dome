"""test_beacon - Simple beacon test module."""


def add(a, b):
    """Return the sum of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b


# --- Tests ---


def test_add_positive_integers():
    """Test add with two positive integers."""
    assert add(2, 3) == 5


def test_add_negative_integers():
    """Test add with negative integers."""
    assert add(-2, -3) == -5


def test_add_mixed_signs():
    """Test add with mixed positive and negative numbers."""
    assert add(10, -4) == 6


def test_add_zero():
    """Test add with zeros."""
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5


def test_add_floats():
    """Test add with floating point numbers."""
    assert add(1.5, 2.5) == 4.0
    assert add(0.1, 0.2) == 0.30000000000000004  # IEEE 754 floating point


if __name__ == "__main__":
    import sys

    # Simple test runner
    tests = [
        test_add_positive_integers,
        test_add_negative_integers,
        test_add_mixed_signs,
        test_add_zero,
        test_add_floats,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            print(f"PASSED: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAILED: {test.__name__} - {e}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed out of {len(tests)} tests")
    sys.exit(0 if failed == 0 else 1)
