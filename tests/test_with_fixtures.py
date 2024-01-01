# file: test_with_fixtures.py
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15
    assert sum(sample_data) == 155

def test_length(sample_data):
    assert len(sample_data) == 5
    assert len(sample_data) == 55