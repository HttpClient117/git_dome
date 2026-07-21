"""Word frequency counter module.

Provides `count_words(text) -> dict[str, int]` that counts word frequency
in a given string. Words are normalized to lowercase and stripped of
leading/trailing punctuation.
"""

import re
from collections import Counter


def count_words(text: str) -> dict[str, int]:
    """Count word frequency in the given text.

    Words are normalized to lowercase. Leading and trailing punctuation
    is stripped from each word. Words are split on whitespace.

    Args:
        text: The input string to analyze.

    Returns:
        A dict mapping each lowercase word to its occurrence count.
        Returns an empty dict for empty or whitespace-only input.

    Examples:
        >>> count_words("Hello world! Hello again.")
        {'hello': 2, 'world': 1, 'again': 1}
        >>> count_words("")
        {}
        >>> count_words("One, two; two: one!")
        {'one': 2, 'two': 2}
    """
    # Split on whitespace and filter out empty tokens
    words = text.split()

    # Normalize: lowercase and strip leading/trailing punctuation
    normalized = [
        re.sub(r"^[^\w]+|[^\w]+$", "", word).lower()
        for word in words
    ]

    # Filter out any tokens that became empty after stripping (e.g. "..." or "—")
    normalized = [w for w in normalized if w]

    return dict(Counter(normalized))


def main() -> None:
    """Demonstrate count_words with sample input."""
    demo_texts = [
        "Hello world! Hello again. The world is beautiful.",
        "To be, or not to be: that is the question.",
        "One fish, two fish, red fish, blue fish.",
        "",
        "Python Python Python",
    ]

    for text in demo_texts:
        result = count_words(text)
        print(f"Text: {text!r}")
        print(f"Result: {result}")
        print()


if __name__ == "__main__":
    main()
