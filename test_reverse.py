"""Tests for reverse.py string reversal utilities."""

import unittest

from reverse import reverse_string, reverse_words


class TestReverseString(unittest.TestCase):
    """Tests for reverse_string()."""

    def test_empty_string(self) -> None:
        self.assertEqual(reverse_string(""), "")

    def test_single_char(self) -> None:
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self) -> None:
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_simple_word(self) -> None:
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_with_spaces(self) -> None:
        self.assertEqual(reverse_string("abc def"), "fed cba")

    def test_with_special_chars(self) -> None:
        self.assertEqual(reverse_string("a!b@c#"), "#c@b!a")

    def test_unicode(self) -> None:
        self.assertEqual(reverse_string("café"), "éfac")

    def test_numbers_as_string(self) -> None:
        self.assertEqual(reverse_string("12345"), "54321")

    def test_leading_trailing_spaces(self) -> None:
        self.assertEqual(reverse_string("  hello  "), "  olleh  ")


class TestReverseWords(unittest.TestCase):
    """Tests for reverse_words()."""

    def test_empty_string(self) -> None:
        self.assertEqual(reverse_words(""), "")

    def test_single_word(self) -> None:
        self.assertEqual(reverse_words("hello"), "hello")

    def test_two_words(self) -> None:
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_multiple_words(self) -> None:
        self.assertEqual(
            reverse_words("the quick brown fox"),
            "fox brown quick the",
        )

    def test_extra_spaces(self) -> None:
        self.assertEqual(
            reverse_words("  hello   world  "),
            "world hello",
        )

    def test_tabs_and_newlines(self) -> None:
        self.assertEqual(
            reverse_words("hello\tworld\nfoo"),
            "foo world hello",
        )

    def test_single_char_words(self) -> None:
        self.assertEqual(reverse_words("a b c"), "c b a")

    def test_unicode_words(self) -> None:
        self.assertEqual(
            reverse_words("hola mundo café"),
            "café mundo hola",
        )

    def test_numbers_as_words(self) -> None:
        self.assertEqual(reverse_words("1 2 3 4"), "4 3 2 1")


if __name__ == "__main__":
    unittest.main()
