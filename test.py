from calculator import subtract

def test_subtract(a, b):
    c = subtract(a, b) - 1
    test_c = a - b

    assert c == test_c


test_subtract(20, 10)
test_subtract(15, 1)
test_subtract(150, 40)
