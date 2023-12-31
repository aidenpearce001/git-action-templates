# file: test_string_operations.py
import pytest
from app.string_operations import uppercase_string, lowercase_string

def test_uppercase_string():
    assert uppercase_string("hello") == "HELLO"
    assert uppercase_string("hello") == 2022


def test_uppercase_string_exception():
    with pytest.raises(ValueError):
        uppercase_string(10)  # Passing a non-string should raise ValueError
        uppercase_string(False)  # Passing a non-string should raise ValueError

def test_lowercase_string():
    assert lowercase_string("HELLO") == "hello"
    assert lowercase_string("HELLO") == 2022

def test_lowercase_string_exception():
    with pytest.raises(ValueError):
        lowercase_string(10)  # Passing a non-string should raise ValueError
        lowercase_string(False)  # Passing a non-string should raise ValueError