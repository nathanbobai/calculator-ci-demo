from calculator import add, divide

def test_add():
    assert add(2, 3) ==5

def test_divide():
    assert divide(4, 2) == 2

def test_subtract():
    assert subtract(6, 5) == 1
