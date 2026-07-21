def is_palindrome(s: str) -> bool:
    """
    Return True if the given string is a palindrome, False otherwise.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring spaces, punctuation, and capitalization.

    Args:
        s: The input string to check.

    Returns:
        True if s is a palindrome, False otherwise.
    """
    # Filter to alphanumeric characters only and convert to lowercase
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]
