from src.math_operations import add, subtract
def test_add():
    assert add(2, 3) == 5
    assert add(3, 4) == 7
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(4, 3) == 1
    assert subtract(0, 0) == 0
    assert subtract(2.5, 1.5) == 1.0