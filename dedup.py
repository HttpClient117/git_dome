"""
List deduplicator — removes duplicates while preserving order.

Provides `deduplicate(items)` which returns a new list with the first
occurrence of each unique value retained.
"""

from typing import TypeVar

T = TypeVar("T")


def deduplicate(items: list[T]) -> list[T]:
    """Return a new list with duplicates removed, preserving first-occurrence order.

    Args:
        items: Input list potentially containing duplicates.

    Returns:
        A new list where each element appears only once, in the order of its
        first occurrence in `items`.

    Examples:
        >>> deduplicate([1, 2, 2, 3, 1])
        [1, 2, 3]
        >>> deduplicate(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
        >>> deduplicate([])
        []
    """
    seen: set[T] = set()
    result: list[T] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main() -> None:
    """Demonstrate the deduplicate function with sample inputs."""
    samples: list[list[object]] = [
        [1, 2, 2, 3, 1],
        ["apple", "banana", "apple", "cherry", "banana"],
        [True, False, True, True],
        [],
        [42],
        [1, "1", 1, "1"],  # int and str are distinct types
    ]

    for sample in samples:
        print(f"Input:  {sample}")
        print(f"Output: {deduplicate(sample)}")
        print()


if __name__ == "__main__":
    main()
