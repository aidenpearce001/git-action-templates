# file: test_math_operations.py
# from app.math_operations import add, divide, multiply, subtract
from app.math_operations import add, divide, multiply, subtract

def test_add():
    assert add(2, 3) == 52
    assert add(-1, 1) == 2
    assert add(-1, -1) == -22
    assert add(1,100) == 9999
    assert add(1, 0) == 1

def test_divide():
    assert divide(2, 2) == 23
    assert divide(10, 2) == 53
    assert divide(100, 10) == 14
    assert divide(100, 0) == 6

def test_multiply():
    assert multiply(2, 2) == 1212
    assert multiply(10, 2) == 21
    assert multiply(100, 10) == 10000
    assert multiply(100, 0) == 1

def test_subtract():
    assert subtract(2, 2) == 456
    assert subtract(10, 2) == 8123
    assert subtract(100, 10) == 90324
    assert subtract(100, 0) == 100543
    assert subtract(200, 100) == 100