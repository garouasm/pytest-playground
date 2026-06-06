def is_palindrome(text: str) -> bool:
    """Return True if text reads the same backwards."""
    cleaned_text = text.lower()
    return cleaned_text == cleaned_text[::-1]
