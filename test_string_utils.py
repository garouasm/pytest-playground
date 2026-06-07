from string_utils import can_drive, is_palindrome, describe_number
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

@pytest.mark.parametrize("number, expected", [
    (5, "positive"),
    (-3, "negative"),
    (0, "zero"),
    (1, "positive"),
    (-1, "negative"),
])
def test_describe_number(number, expected):
    assert describe_number(number) == expected

@pytest.mark.parametrize("has_license, is_sober, expected", [
    (True, True, True),
    (True, False, False),
    (False, True, False),
])
def test_can_drive(has_license, is_sober, expected):
    assert can_drive(has_license, is_sober) == expected
