def is_palindrome(text: str) -> bool:
    """Return True if text reads the same backwards."""
    cleaned_text = text.lower()
    return cleaned_text == cleaned_text[::-1]

def describe_number(n: int) -> str:
    """Classify a number as positive, negative, or zero."""
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
    
