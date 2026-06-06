from string_utils import is_palindrome, describe_number

def test_normal_palindrome():
    assert is_palindrome("ana")

def test_not_palindrome():
    assert not is_palindrome("casa")

def test_empty_string():
    assert is_palindrome("")

def test_single_character():
    assert is_palindrome("a")

def test_palindrome_with_capital():
    assert is_palindrome("Ana")

def test_positive_number():
    assert describe_number(5) == "positive"

def test_negative_number():
    assert describe_number(-3) == "negative"

def test_zero_number():
    assert describe_number(0) == "zero"
