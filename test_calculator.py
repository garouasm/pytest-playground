"""Tests for the calculator module.

Each function starting with `test_` is one check that pytest runs.
"""

from calculator import add, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(10, 4) == 6
