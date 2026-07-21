"""String reversal utilities.

Provides two functions:
- reverse_string: reverses all characters in a string
- reverse_words: reverses the order of words while preserving character order within each word
"""


def reverse_string(s: str) -> str:
    """Return the string with all characters in reverse order.

    Args:
        s: The input string.

    Returns:
        The reversed string.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("abc def")
        'fed cba'
    """
    return s[::-1]


def reverse_words(s: str) -> str:
    """Return the string with the order of words reversed.

    Words are defined as sequences of non-whitespace characters.
    Whitespace between words is collapsed to a single space in the output.

    Args:
        s: The input string.

    Returns:
        The string with words in reverse order, joined by single spaces.

    Examples:
        >>> reverse_words("hello world")
        'world hello'
        >>> reverse_words("the quick brown fox")
        'fox brown quick the'
    """
    return " ".join(s.split()[::-1])


def main() -> None:
    """Demonstrate the string reversal functions."""
    test_strings = [
        "hello",
        "Hello World",
        "the quick brown fox",
        "Python is awesome",
        "  extra   spaces  ",
    ]

    print("String Reverser Demo")
    print("=" * 40)

    for s in test_strings:
        print(f"Original:      {s!r}")
        print(f"Reversed:      {reverse_string(s)!r}")
        print(f"Words reversed: {reverse_words(s)!r}")
        print("-" * 40)


if __name__ == "__main__":
    main()
