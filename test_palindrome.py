import pytest
from palindrome import is_palindrome


def test_simple_palindrome():
    """Basic palindromes with lowercase letters only."""
    assert is_palindrome("racecar") is True
    assert is_palindrome("madam") is True
    assert is_palindrome("level") is True


def test_non_palindrome():
    """Strings that are not palindromes."""
    assert is_palindrome("hello") is False
    assert is_palindrome("world") is False
    assert is_palindrome("python") is False


def test_case_insensitivity():
    """Palindromes should be case-insensitive."""
    assert is_palindrome("Racecar") is True
    assert is_palindrome("MadAm") is True
    assert is_palindrome("Level") is True


def test_spaces_ignored():
    """Spaces should be ignored."""
    assert is_palindrome("race car") is True
    assert is_palindrome("a man a plan a canal panama") is True
    assert is_palindrome("never odd or even") is True


def test_punctuation_ignored():
    """Punctuation should be ignored."""
    assert is_palindrome("racecar!") is True
    assert is_palindrome("madam, I'm Adam!") is True
    assert is_palindrome("A man, a plan, a canal: Panama!") is True


def test_empty_string():
    """An empty string is a palindrome."""
    assert is_palindrome("") is True


def test_single_character():
    """A single character is a palindrome."""
    assert is_palindrome("a") is True
    assert is_palindrome("Z") is True


def test_numbers_in_string():
    """Strings containing numbers should work."""
    assert is_palindrome("12321") is True
    assert is_palindrome("12345") is False


def test_only_spaces_and_punctuation():
    """Strings with only spaces/punctuation are effectively empty."""
    assert is_palindrome("   ") is True
    assert is_palindrome("!@#$") is True
