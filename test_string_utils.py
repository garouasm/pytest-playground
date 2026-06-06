from string_utils import is_palindrome, describe_number

def test_normal_palindrome():
    assert is_palindrome("ana") == True

def test_not_palindrome():
    assert is_palindrome("casa") == False

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_palindrome_with_capital():
    assert is_palindrome("Ana") == True

def test_positive_number():
    assert describe_number(5) == "positive"

def test_negative_number():
    assert describe_number(-3) == "negative"

def test_zero_number():
    assert describe_number(0) == "zero"
