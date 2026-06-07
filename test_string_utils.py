from string_utils import is_palindrome, describe_number
import pytest

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

@pytest.mark.parametrize("input, expected", [
    (5, "positive"),
    (-3, "negative"),
    (0, "zero"),
    (1, "positive"),
    (-1, "negative"),
])

def test_describe_number(input, expected):
    assert describe_number(input) == expected
