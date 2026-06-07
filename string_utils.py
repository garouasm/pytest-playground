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
    
def can_drive(has_license: bool, is_sober: bool) -> bool:
    """Can drive only with a license AND being sober."""
    return has_license and is_sober