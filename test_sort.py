from sort import sort
import pytest

def test_standard():
    assert sort(10, 10, 10, 5) == 'STANDARD'

def test_special_heavy():
    assert sort(10, 10, 10, 25) == 'SPECIAL'

def test_special_bulky():
    assert sort(1000, 1000, 1, 5) == 'SPECIAL'

def test_rejected():
    assert sort(1000, 1000, 1, 25) == 'REJECTED'

def test_edge_case_exactly_bulky():
    assert sort(100, 100, 100, 5) == 'SPECIAL'

def test_edge_case_exactly_heavy():
    assert sort(10, 10, 10, 20) == 'SPECIAL'

def test_invalid_width_type():
    with pytest.raises(TypeError):
        sort("100", 10, 10, 5)

def test_invalid_mass_type():
    with pytest.raises(TypeError):
        sort(10, 10, 10, "heavy")

def test_missing_arguments():
    with pytest.raises(TypeError):
        sort(10, 10, 10)

def test_none_input():
    with pytest.raises(TypeError):
        sort(None, 10, 10, 5)