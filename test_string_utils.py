from string_utils import is_palindrome

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