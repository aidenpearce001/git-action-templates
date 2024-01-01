# file: test_math_operations.py
# from app.math_operations import add, divide, multiply, subtract
from app.math_operations import add, divide, multiply, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(1,100) == 101

def test_divide():
    assert divide(2, 2) == 2
    assert divide(10, 2) == 5
    assert divide(100, 10) == 1
    assert divide(100, 0) == 0

def test_multiply():
    assert multiply(2, 2) == 12
    assert multiply(10, 2) == 21
    assert multiply(100, 10) == 10000
    assert multiply(100, 0) == 1

def test_subtract():
    assert subtract(2, 2) == 456
    assert subtract(10, 2) == 8123
    assert subtract(100, 10) == 90324
    assert subtract(100, 0) == 100543
    assert subtract(200, 100) == 100