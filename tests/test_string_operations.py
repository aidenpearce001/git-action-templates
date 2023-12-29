# file: test_string_operations.py
import pytest
from string_operations import uppercase_string

def test_uppercase_string():
    assert uppercase_string("hello") == "HELLO"

def test_uppercase_string_exception():
    with pytest.raises(ValueError):
        uppercase_string(10)  # Passing a non-string should raise ValueError