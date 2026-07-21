"""Tests for wordcount.py."""

import pytest
from wordcount import count_words


class TestCountWords:
    """Tests for the count_words function."""

    def test_empty_string(self) -> None:
        """Empty string should return an empty dict."""
        assert count_words("") == {}

    def test_whitespace_only(self) -> None:
        """Whitespace-only input should return an empty dict."""
        assert count_words("   \t  \n  ") == {}

    def test_single_word(self) -> None:
        """A single word should count as 1."""
        assert count_words("hello") == {"hello": 1}

    def test_case_insensitive(self) -> None:
        """Words with different casing should be merged."""
        assert count_words("Hello hello HELLO") == {"hello": 3}

    def test_punctuation_stripping(self) -> None:
        """Leading/trailing punctuation should be stripped."""
        assert count_words('"hello", world!') == {"hello": 1, "world": 1}

    def test_punctuation_only(self) -> None:
        """Punctuation-only tokens should be filtered out."""
        assert count_words("... --- !!!") == {}

    def test_multiple_spaces(self) -> None:
        """Multiple consecutive spaces should be handled."""
        assert count_words("hello    world") == {"hello": 1, "world": 1}

    def test_newlines(self) -> None:
        """Newlines should be treated as whitespace."""
        assert count_words("hello\nworld\nhello") == {"hello": 2, "world": 1}

    def test_numbers(self) -> None:
        """Numbers should be treated as words."""
        assert count_words("123 456 123") == {"123": 2, "456": 1}

    def test_mixed_alphanumeric(self) -> None:
        """Mixed alphanumeric tokens should be preserved."""
        assert count_words("hello123 world456 hello123") == {
            "hello123": 2,
            "world456": 1,
        }

    def test_classic_example(self) -> None:
        """Classic word count example."""
        result = count_words("Hello world! Hello again. The world is beautiful.")
        assert result == {
            "hello": 2,
            "world": 2,
            "again": 1,
            "the": 1,
            "is": 1,
            "beautiful": 1,
        }

    def test_apostrophe_words(self) -> None:
        """Apostrophes within words should be preserved."""
        assert count_words("don't stop can't") == {
            "don't": 1,
            "stop": 1,
            "can't": 1,
        }

    def test_hyphenated_words(self) -> None:
        """Hyphens within words should be preserved."""
        assert count_words("well-known high-level well-known") == {
            "well-known": 2,
            "high-level": 1,
        }
