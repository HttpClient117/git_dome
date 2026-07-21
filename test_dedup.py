"""Tests for dedup.deduplicate."""

import unittest
from dedup import deduplicate


class TestDeduplicate(unittest.TestCase):
    """Test suite for the deduplicate function."""

    def test_empty_list(self) -> None:
        """An empty list should return an empty list."""
        self.assertEqual(deduplicate([]), [])

    def test_single_element(self) -> None:
        """A single-element list should be unchanged."""
        self.assertEqual(deduplicate([42]), [42])
        self.assertEqual(deduplicate(["hello"]), ["hello"])

    def test_no_duplicates(self) -> None:
        """A list with no duplicates should be unchanged."""
        self.assertEqual(deduplicate([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_all_duplicates(self) -> None:
        """A list where every element is the same should have one element."""
        self.assertEqual(deduplicate([5, 5, 5, 5]), [5])

    def test_mixed_duplicates(self) -> None:
        """Duplicates interspersed should preserve first-occurrence order."""
        self.assertEqual(deduplicate([1, 2, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(deduplicate(["a", "b", "a", "c"]), ["a", "b", "c"])

    def test_order_preserved(self) -> None:
        """First occurrence of each value should be retained."""
        self.assertEqual(
            deduplicate([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
            [3, 1, 4, 5, 9, 2, 6],
        )

    def test_strings(self) -> None:
        """Works with strings."""
        self.assertEqual(
            deduplicate(["apple", "banana", "apple", "cherry", "banana"]),
            ["apple", "banana", "cherry"],
        )

    def test_booleans(self) -> None:
        """Works with booleans."""
        self.assertEqual(deduplicate([True, False, True, True]), [True, False])

    def test_mixed_types(self) -> None:
        """Int 1 and str '1' are distinct types and both retained."""
        result = deduplicate([1, "1", 1, "1"])
        self.assertEqual(result, [1, "1"])

    def test_returns_new_list(self) -> None:
        """The function should return a new list, not mutate the input."""
        original = [1, 2, 2, 3]
        result = deduplicate(original)
        self.assertEqual(original, [1, 2, 2, 3])
        self.assertIsNot(result, original)

    def test_none_values(self) -> None:
        """None values should be handled correctly."""
        self.assertEqual(deduplicate([None, 1, None, 2]), [None, 1, 2])

    def test_large_list(self) -> None:
        """Handles a large list with many duplicates efficiently."""
        large = list(range(1000)) * 3
        result = deduplicate(large)
        self.assertEqual(result, list(range(1000)))
        self.assertEqual(len(result), 1000)


if __name__ == "__main__":
    unittest.main()
